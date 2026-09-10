import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('blender_preflight', ROOT/'tools/blender_preflight.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


class BlenderIntegrationTests(unittest.TestCase):
    def test_missing_binary(self):
        with patch.dict(probe.os.environ, {}, clear=True), patch.object(probe.shutil, 'which', return_value=None):
            self.assertEqual(probe.inspect()['status'], 'BLENDER_NOT_FOUND')

    def test_explicit_invalid_path_does_not_execute(self):
        def fail(*args, **kwargs):
            self.fail('Invalid executable must not be run')
        self.assertEqual(probe.inspect('missing-blender-test', fail)['status'], 'INVALID_BINARY_PATH')

    def test_probe_only_requests_version(self):
        with tempfile.TemporaryDirectory() as directory:
            fake = Path(directory)/'blender.exe'; fake.touch()
            def run(args, **kwargs):
                self.assertEqual(args, [str(fake.resolve()), '--version'])
                self.assertNotIn('shell', kwargs)
                return subprocess.CompletedProcess(args, 0, 'Blender 5.1.2\n', '')
            result = probe.inspect(str(fake), run)
            self.assertEqual(result['status'], 'BLENDER_FOUND')
            self.assertFalse(result['modeling_verified'])
            self.assertFalse(result['mcp_verified'])

    def test_failed_process_is_not_ready(self):
        with tempfile.TemporaryDirectory() as directory:
            fake = Path(directory)/'blender'; fake.touch()
            result = probe.inspect(str(fake), lambda *a, **kw: subprocess.CompletedProcess(a, 2, 'Blender 5.1.2', ''))
            self.assertEqual(result['status'], 'PROBE_FAILED')

    def test_timeout_is_not_ready(self):
        with tempfile.TemporaryDirectory() as directory:
            fake = Path(directory)/'blender'; fake.touch()
            def timeout(*a, **kw):
                raise subprocess.TimeoutExpired(a[0], 15)
            self.assertEqual(probe.inspect(str(fake), timeout)['status'], 'PROBE_FAILED')

    def test_both_host_entries_resolve(self):
        self.assertTrue((ROOT/'.claude/skills/blender-director/SKILL.md').is_file())
        wrapper = ROOT/'.agents/skills/blender-director/SKILL.md'
        self.assertEqual(wrapper.parent.parents[2], ROOT)
        self.assertIn('.claude/skills/blender-director/SKILL.md', wrapper.read_text(encoding='utf-8'))

    def test_optional_stage_does_not_replace_mainline(self):
        text = (ROOT/'.claude/CLAUDE.md').read_text(encoding='utf-8')
        self.assertIn('~render EP01-S01', text)
        self.assertIn('按需', text)
        self.assertIn('blender-artist', text)

    def test_no_legacy_engine_or_demo_is_installed(self):
        skill = ROOT/'.claude/skills/blender-director'
        self.assertFalse((skill/'engine/analysis_to_shot.py').exists())
        self.assertFalse((skill/'demo-S02').exists())


if __name__ == '__main__':
    unittest.main()
