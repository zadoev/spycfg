import os
import json
import functools

import configparser
from io import StringIO

import spycfg.errors
import spycfg.generators


INI_CFG = 'ini'
JSON_CFG = 'json'

CONFIG_TYPES = {
    INI_CFG: INI_CFG,
    JSON_CFG: JSON_CFG,
}


class DictCfg(dict):
    """
    Just to have ability makes configs from dicts
    """


class SpyCfg(DictCfg):
    def __init__(self, cfg_path, cfg_type=JSON_CFG, env=None):

        self.cfg_type = cfg_type

        file_data = self.read_file(cfg_path)

        if self.cfg_type == JSON_CFG:
            dict_from_data = json.loads(file_data)
        elif self.cfg_type == INI_CFG:
            config = configparser.ConfigParser()
            try:
                config.read_file(StringIO(file_data), None)
                dict_from_data = config._sections
            except configparser.MissingSectionHeaderError:
                config.read_file(StringIO('[default]\n' + file_data))
                dict_from_data = dict(config._sections)
                del dict_from_data['default']
                dict_from_data.update(config._sections['default'])

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
        return file_data
        # dict_from_data = json.loads(file_data)
        # return dict_from_data

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
