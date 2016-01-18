import sys
import os

sys.path.append(
    os.path.join(os.path.dirname(__file__), '..', 'src')
)

from spycfg import SpyCfg

# first reads simple.json, then reads DEV.json in same location and updates
# simple config with data from DEV config
cfg = SpyCfg('src/tests/fixtures/simple.json', cfg_type=SpyCfg.JSON, env='DEV')

print("cfg['key1'] =", cfg['key1'])  # DEV1key1 - value from DEV.cfg
print("cfg['key2'] =", cfg['key2'])
