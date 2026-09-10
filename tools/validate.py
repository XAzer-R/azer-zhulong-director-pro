"""Offline package validation. Does not call a model or create project data."""
import hashlib
import json
from pathlib import Path
import re


def validate(root):
    root = Path(root)
    errors = []
    config = json.loads((root / 'project.json').read_text(encoding='utf-8'))
    role_files = list((root / '.claude/agents').glob('*.md'))
    roles = {p.stem for p in role_files}
    if roles != set(config['roles']):
        errors.append('ROLE_SET_MISMATCH')
    skills = {p.parent.name for p in (root / '.claude/skills').glob('*/SKILL.md')}
    for p in role_files + list((root / '.claude/skills').rglob('SKILL.md')):
        s = p.read_text(encoding='utf-8')
        parts = s.split('---', 2)
        if not s.startswith('---\n') or len(parts) < 3:
            errors.append('MISSING_FRONTMATTER:' + p.relative_to(root).as_posix())
            continue
        head = parts[1]
        for field in ['name', 'description']:
            if not re.search(r'^' + field + r':\s*\S', head, re.M):
                errors.append('MISSING_FIELD:' + field + ':' + p.name)
        name = re.search(r'^name:\s*(\S+)', head, re.M)
        expected_name = p.stem if p in role_files else p.parent.name
        if name and (p in role_files or p.parent.parent == root / '.claude/skills') and name.group(1) != expected_name:
            errors.append('NAME_MISMATCH:' + p.relative_to(root).as_posix())
        if 'skills:' in head:
            m = re.search(r'^skills:\n((?:  - [^\n]+\n?)+)', head, re.M)
            if not m:
                errors.append('INVALID_SKILLS_LIST:' + p.name)
            else:
                for skill in re.findall(r'  - (\S+)', m.group(1)):
                    if skill not in skills:
                        errors.append('MISSING_SKILL:' + skill)
    files = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts]
    for p in files:
        relative = p.relative_to(root).as_posix()
        if p.suffix in ('.png', '.jpg', '.mp4', '.wav', '.zip', '.rar', '.sqlite', '.db'):
            errors.append('UNEXPECTED_ASSET:' + relative)
        if p.suffix == '.json':
            try:
                json.loads(p.read_text(encoding='utf-8'))
            except (ValueError, UnicodeError):
                errors.append('INVALID_JSON:' + relative)
        if p.suffix != '.md':
            continue
        text = p.read_text(encoding='utf-8')
        for imported in re.findall(r'^@([^\s]+)$', text, re.M):
            if not (root / imported).is_file():
                errors.append('MISSING_IMPORT:' + imported)
        for ref in set(re.findall(r'`([^`\n]+)`', text)):
            if not ref.startswith('.claude/') or any(c in ref for c in '{}<>* |') or not Path(ref).suffix:
                continue
            if not (root / ref).exists():
                errors.append('MISSING_REFERENCE:' + ref)
        if re.search(r'(?i)\b[CDEK]:[\\/]|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{24,}', text):
            errors.append('SENSITIVE_PATTERN:' + relative)
    assembly = json.loads((root / '.codex/component-assembly.json').read_text(encoding='utf-8'))
    for record in assembly['files']:
        p = root / record['path']
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != record['sha256']:
            errors.append('ASSEMBLY_HASH_MISMATCH:' + record['path'])
    return {'ok': not errors, 'files_checked': len(files), 'roles': len(roles), 'skills': len(skills), 'errors': errors}


if __name__ == '__main__':
    result = validate(Path(__file__).resolve().parents[1])
    print(json.dumps(result, ensure_ascii=True, indent=2))
    raise SystemExit(0 if result['ok'] else 1)
