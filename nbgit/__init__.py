import os
import re
import _default_config
import nbgit
import nbgit.utils as utils
from nbgit.converter import NB2Py

GIT_DIR='./.git'
GIT_PC_PATH='./.git/hooks/pre-commit'
NBGIT_DIR=nbgit.__path__[0]
PRECOMMIT_SCRIPT_PATH='{}/precommit'.format(NBGIT_DIR)
DEFAULT_CONFIG_PATH='{}/_default_config.py'.format(NBGIT_DIR)
CONFIG_PATH='./nbgit_config.py'


def install():
    """ Installs pre-commit hook
    """
    if os.path.exists(GIT_DIR):
        utils.copy_append(PRECOMMIT_SCRIPT_PATH,GIT_PC_PATH)
        os.system('chmod +x {}'.format(GIT_PC_PATH))
    else:
        print "nbgit: MUST INITIALIZE GIT"


def configure():
    """ Install config file
        allows user to change config
    """
    utils.copy_append(DEFAULT_CONFIG_PATH,CONFIG_PATH,'w')


def notebook_list():
    """ Notebook paths as list
    """
    return utils.rglob('*.ipynb',exclude_dirs=config.EXCLUDE_DIRS)    


def convert_all(noisy=True):
    """ Convert all Notebooks
    """
    if noisy: print('nbgit[notebooks]:')
    for path in notebook_list():
        if noisy: print('\t{}'.format(path))
        convert(path)


def convert(path):
    """ Convert Single Notebook
    """
    NB2Py(path).convert()





