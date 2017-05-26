import os
import re
import nbgit
import nbgit.utils as utils
from nbgit.converter import NB2Py
from nbgit.config import AUTO_ADD_NBPY

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
        convert(path)


def convert(path,noisy=True):
    """ Convert Notebook
    """
    if noisy: print('\t{}'.format(path))
    nbpy_path=NB2Py(path).convert()
    if AUTO_ADD_NBPY:
        utils.git_add(nbpy_path)

    





