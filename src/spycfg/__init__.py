import os
import json
import functools

import spycfg.errors
import spycfg.generators


class SpyCfg(dict):
    JSON = 'json'

    def __init__(self, cfg_path, cfg_type=None):
        dict_from_data = self.read_file(cfg_path)

        self.apply_environments(dict_from_data)

        super(SpyCfg, self).__init__(dict_from_data)

    @staticmethod
    def read_file(cfg_path) -> str:
        """
        Reads file (for now as json)

        :param cfg_path:
        :return:
        """
        try:
            f = open(cfg_path)
        except IOError as e:
            raise spycfg.errors.IOError("IOError") from e
        file_data = f.read()
        dict_from_data = json.loads(file_data)
        return dict_from_data

    @staticmethod
    def apply_environments(cfg):
        for path in spycfg.generators.keys_path_to_simple_values(cfg):
            key = '__'.join(path).upper()
            env_value = os.getenv(key)

            if env_value is not None:
                tail = path.pop()

                section = functools.reduce(dict.__getitem__, path, cfg)

                section[tail] = env_value
