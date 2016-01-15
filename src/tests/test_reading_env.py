import os
import json

from spycfg import SpyCfg

from tests.helpers import BaseTestCase


class CreateTestCase(BaseTestCase):
    def test_env_variable_overrides_config_value(self):
        config_data = json.loads(self.file_content(self.SIMPLE_JSON_CONFIG))

        any_key_from_config = list(config_data.keys())[0]
        new_key_value = config_data[any_key_from_config] * 2
        os.environ[any_key_from_config.upper()] = new_key_value
        self.assertEquals(os.getenv(any_key_from_config.upper()), new_key_value)
        cfg = SpyCfg(self.SIMPLE_JSON_CONFIG)

        self.assertEqual(cfg[any_key_from_config], new_key_value)

        del os.environ[any_key_from_config.upper()]  # clean up
