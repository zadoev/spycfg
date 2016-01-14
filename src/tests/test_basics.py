import unittest

from spycfg import SpyCfg
import spycfg.errors


class CreateTestCase(unittest.TestCase):
    def test_no_file(self):
        with self.assertRaises(spycfg.errors.IOError) as cf:
            file_name = 'any'
            cfg = SpyCfg(file_name)

        self.assertIsInstance(cf.exception, spycfg.errors.IOError)

    def test_create_from_json(self):
        cfg = SpyCfg('fixtures/simple.json', cfg_type=SpyCfg.JSON)

        self.assertEqual(cfg['key1'], 'key1')


