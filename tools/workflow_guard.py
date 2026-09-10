"""Read-only preflight for input boundaries and version-bound review decisions."""
import argparse
import hashlib
import json
from pathlib import Path
import re


def unit(value):
    if not isinstance(value, str) or not re.fullmatch(r'EP[0-9]{2}(?:-S[0-9]{2})?', value):
        raise ValueError('INVALID_UNIT')
    return value.split('-')


def safe_path(root, relative):
    root = Path(root).resolve(strict=True)
    raw = Path(relative)
    if raw.is_absolute() or not relative or re.search(r'(^|[/\\])\.\.([/\\]|$)|:', relative):
        raise ValueError('PATH_OUTSIDE_PROJECT')
    candidate = root / raw
    if not candidate.resolve().is_relative_to(root):
        raise ValueError('PATH_OUTSIDE_PROJECT')
    # Do not follow junctions or symlinks even if they point back into the root.
    cursor = root
    for part in raw.parts:
        cursor = cursor / part
        if cursor.is_symlink() or (cursor.exists() and getattr(cursor.lstat(), 'st_file_attributes', 0) & 0x400):
            raise ValueError('LINK_NOT_ALLOWED')
    return candidate


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def review_state(root, receipt):
    """Receipts are local review records, not signatures or professional approval."""
    if not isinstance(receipt, dict):
        raise ValueError('INVALID_RECEIPT')
    if receipt.get('status') != 'PASS' or receipt.get('blockers') != []:
        return 'BLOCKED'
    inputs = receipt.get('inputs')
    outputs = receipt.get('outputs')
    if not isinstance(inputs, dict) or not inputs or not isinstance(outputs, dict) or not outputs:
        raise ValueError('MISSING_VERSION_BINDINGS')
    for mapping in (inputs, outputs):
        for relative, expected in mapping.items():
            if not isinstance(relative, str) or not isinstance(expected, str) or not re.fullmatch('[a-f0-9]{64}', expected):
                raise ValueError('INVALID_VERSION_BINDING')
            path = safe_path(root, relative)
            if not path.is_file() or digest(path) != expected:
                return 'STALE'
    return 'CURRENT'


def retry_decision(revisions, passed):
    if type(revisions) is not int or revisions < 0 or type(passed) is not bool:
        raise ValueError('INVALID_REVIEW_STATE')
    return 'PASS' if passed else 'NEEDS_USER_DECISION' if revisions >= 2 else 'REVISE'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    u = sub.add_parser('unit')
    u.add_argument('value')
    r = sub.add_parser('review')
    r.add_argument('receipt')
    r.add_argument('--root', default='.')
    args = parser.parse_args()
    try:
        if args.command == 'unit':
            result = {'unit': unit(args.value), 'valid': True}
        else:
            receipt_path = safe_path(args.root, args.receipt)
            result = {'state': review_state(args.root, json.loads(receipt_path.read_text(encoding='utf-8')))}
        print(json.dumps(result))
        return 0 if result.get('state', 'CURRENT') == 'CURRENT' else 1
    except (ValueError, OSError, TypeError) as exc:
        print(json.dumps({'error': str(exc)}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
