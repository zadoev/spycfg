import spycfg.errors
from spycfg import SpyCfg
from tests.helpers import BaseTestCase


class CreateTestCase(BaseTestCase):
    def test_no_file(self):
        with self.assertRaises(spycfg.errors.IOError) as cf:
            file_name = 'any'
            SpyCfg(file_name)

        self.assertIsInstance(cf.exception, spycfg.errors.IOError)

    def test_create_from_json(self):
        cfg = SpyCfg(self.SIMPLE_JSON_CONFIG, cfg_type=SpyCfg.JSON)

        self.assertEqual(cfg['key1'], 'key1')
