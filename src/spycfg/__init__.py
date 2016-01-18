import os
import json
import functools

import spycfg.errors
import spycfg.generators


class DictCfg(dict):
    """
    Just to have ability makes configs from dicts
    """


class SpyCfg(DictCfg):
    JSON = 'json'

    def __init__(self, cfg_path, cfg_type=None, env=None):
        self.cfg_type = cfg_type
        dict_from_data = self.read_file(cfg_path)

        self.apply_environments(dict_from_data)

        super(SpyCfg, self).__init__(dict_from_data)

        if env is not None:
            env_cfg = SpyCfg(self.locate_file_by_path_and_name(cfg_path, env))
            self.update(env_cfg)

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
    def locate_file_by_path_and_name(path, file_name):
        file_name += '.json'
        path = list(os.path.split(path))
        path.pop()
        return os.path.join(*path, file_name)

    @staticmethod
    def apply_environments(cfg):
        for path in spycfg.generators.keys_path_to_simple_values(cfg):
            key = '__'.join(path).upper()
            env_value = os.getenv(key)

            if env_value is not None:
                tail = path.pop()

                section = functools.reduce(dict.__getitem__, path, cfg)

                section[tail] = env_value
