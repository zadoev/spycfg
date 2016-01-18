import sys
import os

sys.path.append(
    os.path.join(os.path.dirname(__file__), '..', 'src')
)

from spycfg import SpyCfg

# or you can ran previous example with env
os.environ['KEY1'] = 'hello from env'

cfg = SpyCfg('src/tests/fixtures/simple.json', cfg_type=SpyCfg.JSON)

print("cfg['key1'] =", cfg['key1'])
print("cfg['key2'] =", cfg['key2'])
