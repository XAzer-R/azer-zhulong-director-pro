import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package_validator', ROOT/'tools/validate.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ShowcaseTests(unittest.TestCase):
    def test_actual_selected_image_matches_manifest(self):
        self.assertEqual(set(validator.showcase_assets(ROOT)), {'docs/showcase/illustrated-character-sheet.png'})

    def test_unlisted_whitebox_images_are_not_approved(self):
        approved = validator.showcase_assets(ROOT)
        self.assertNotIn('docs/showcase/blockout-camera.png', approved)
        self.assertNotIn('docs/showcase/articulated-poses.png', approved)

    def test_changed_image_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); sub=root/'docs/showcase';sub.mkdir(parents=True)
            (sub/'sample.png').write_bytes(b'changed')
            (sub/'manifest.json').write_text(json.dumps({'assets':[{'path':'docs/showcase/sample.png','sha256':hashlib.sha256(b'approved').hexdigest()}]}),encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'HASH_MISMATCH'):
                validator.showcase_assets(root)

    def test_outside_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);sub=root/'docs/showcase';sub.mkdir(parents=True)
            (sub/'manifest.json').write_text(json.dumps({'assets':[{'path':'../../private.png','sha256':'a'*64}]}),encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'INVALID_SHOWCASE_PATH'):
                validator.showcase_assets(root)
