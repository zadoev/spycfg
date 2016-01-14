import json

import spycfg.errors


class SpyCfg(dict):
    JSON = 'json'

    def __init__(self, cfg_path, cfg_type=None):
        try:
            f = open(cfg_path)
        except IOError as e:
            raise spycfg.errors.IOError("IOError") from e
        super(SpyCfg, self).__init__(json.loads(f.read()))
