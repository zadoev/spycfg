import sys
import os

sys.path.append(
    os.path.join(os.path.dirname(__file__), '..','src')
)

from spycfg import SpyCfg

cfg = SpyCfg('src/tests/fixtures/simple.json', cfg_type=SpyCfg.JSON)

print("cfg['key1'] =", cfg['key1'])
print("cfg['key2'] =", cfg['key2'])