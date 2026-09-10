"""Read-only Blender version detection; never installs or opens a scene."""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess


def inspect(binary=None, runner=subprocess.run):
    selected = binary or os.environ.get('BLENDER_BIN') or shutil.which('blender')
    if not selected:
        return {'status': 'BLENDER_NOT_FOUND', 'scene_operations': False}
    path = Path(selected).expanduser()
    if not path.is_file():
        return {'status': 'INVALID_BINARY_PATH', 'scene_operations': False}
    try:
        result = runner([str(path.resolve()), '--version'], capture_output=True,
                        text=True, encoding='utf-8', errors='replace', timeout=15,
                        check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {'status': 'PROBE_FAILED', 'error_type': type(exc).__name__,
                'scene_operations': False}
    version = re.search(r'^Blender\s+(\d+\.\d+\.\d+)\b', result.stdout, re.M)
    if result.returncode != 0 or not version:
        return {'status': 'PROBE_FAILED', 'returncode': result.returncode,
                'scene_operations': False}
    return {'status': 'BLENDER_FOUND', 'version': version.group(1),
            'scene_operations': False, 'mcp_verified': False,
            'modeling_verified': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--binary', help='Explicit Blender executable, no shell expression')
    args = parser.parse_args()
    result = inspect(args.binary)
    print(json.dumps(result))
    return 0 if result['status'] == 'BLENDER_FOUND' else 1


if __name__ == '__main__':
    raise SystemExit(main())
