import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('guard', ROOT / 'tools/workflow_guard.py')
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)
v_spec = importlib.util.spec_from_file_location('validator', ROOT / 'tools/validate.py')
validator = importlib.util.module_from_spec(v_spec)
v_spec.loader.exec_module(validator)


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / 'input.md').write_text('synthetic input', encoding='utf-8')
        (self.root / 'output.md').write_text('synthetic output', encoding='utf-8')
        self.receipt = {'status': 'PASS', 'blockers': [], 'inputs': {'input.md': guard.digest(self.root/'input.md')}, 'outputs': {'output.md': guard.digest(self.root/'output.md')}}

    def tearDown(self):
        self.tmp.cleanup()

    def test_valid_unit(self):
        self.assertEqual(guard.unit('EP01-S02'), ['EP01', 'S02'])

    def test_unit_injection(self):
        for value in ['../EP01', 'EP01/../../x', 'C:\\x', 'EP01;whoami', 'EP1', 'EP01-S01-extra']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                guard.unit(value)

    def test_current_receipt(self):
        self.assertEqual(guard.review_state(self.root, self.receipt), 'CURRENT')

    def test_changed_input_invalidates_review(self):
        (self.root/'input.md').write_text('revised input', encoding='utf-8')
        self.assertEqual(guard.review_state(self.root, self.receipt), 'STALE')

    def test_changed_output_invalidates_review(self):
        (self.root/'output.md').write_text('revised output', encoding='utf-8')
        self.assertEqual(guard.review_state(self.root, self.receipt), 'STALE')

    def test_missing_output_invalidates_review(self):
        (self.root/'output.md').unlink()
        self.assertEqual(guard.review_state(self.root, self.receipt), 'STALE')

    def test_fail_cannot_become_pass(self):
        for status in ['FAIL', 'FAILED', 'PASS_WITH_WARNINGS', None]:
            r = dict(self.receipt, status=status)
            self.assertEqual(guard.review_state(self.root, r), 'BLOCKED')

    def test_blocker_overrides_pass(self):
        self.assertEqual(guard.review_state(self.root, dict(self.receipt, blockers=['missing input'])), 'BLOCKED')

    def test_missing_bindings_fail(self):
        with self.assertRaises(ValueError):
            guard.review_state(self.root, dict(self.receipt, inputs={}))

    def test_path_escape(self):
        for p in ['../outside', '/outside', 'C:\\outside', 'input.md:stream']:
            with self.subTest(path=p), self.assertRaises(ValueError):
                guard.safe_path(self.root, p)

    def test_two_revision_limit(self):
        self.assertEqual(guard.retry_decision(0, False), 'REVISE')
        self.assertEqual(guard.retry_decision(1, False), 'REVISE')
        self.assertEqual(guard.retry_decision(2, False), 'NEEDS_USER_DECISION')
        self.assertEqual(guard.retry_decision(8, False), 'NEEDS_USER_DECISION')

    def test_invalid_retry_state(self):
        for n, passed in [(True, False), (-1, False), (0, 'false')]:
            with self.assertRaises(ValueError):
                guard.retry_decision(n, passed)

    def test_clean_package(self):
        self.assertTrue(validator.validate(ROOT)['ok'])


if __name__ == '__main__':
    unittest.main()
