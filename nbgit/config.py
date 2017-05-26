import os
CONFIG_PATH='./nbgit_config.py'


if os.path.isfile(CONFIG_PATH):
    from nbgit_config import *
else:
    from _default_config import *
