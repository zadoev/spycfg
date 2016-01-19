import unittest


class BaseTestCase(unittest.TestCase):
    SIMPLE_JSON_CONFIG = 'fixtures/simple.json'
    SIMPLE_INI_CONFIG = 'fixtures/simple_ini_config.ini'
    DEV_CONFIG = 'fixtures/DEV.json'

    def file_content(self, file_name):
        f = open(file_name, 'r')

        return f.read()
