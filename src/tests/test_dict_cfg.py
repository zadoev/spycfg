from spycfg import DictCfg

from tests.helpers import BaseTestCase


class DictCfgTestCase(BaseTestCase):
    def test_merge(self):
        a_value = 1
        new_b_value = 3

        base_cfg = DictCfg(dict(a=a_value, b=2))
        another_cfg = DictCfg(dict(b=new_b_value))

        base_cfg.update(another_cfg)

        self.assertEquals(new_b_value, base_cfg['b'])
        self.assertEquals(a_value, base_cfg['a'])
