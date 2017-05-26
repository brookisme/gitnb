import os
import sys
CONFIG_PATH='./nbgit_config.py'


if os.path.isfile(CONFIG_PATH):
    print "PROJECT DIRECTORY ADDED TO SYS PATH!"
    sys.path.append('./')
    from nbgit_config import *
else:
    from _default_config import *
