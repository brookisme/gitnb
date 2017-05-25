# __init__.py
import os
import re
import errno
import fnmatch
import config
from nbgit.converter import NB2Py
import nbgit.precommit as pc

GIT_DIR='./.git'
GIT_PC_PATH='./.git/hooks/pre-commit'

def install():
    """ Installs pre-commit hook
    """
    if os.path.exists(GIT_DIR):
        pcpath=re.sub('.pyc$','.py',pc.__file__)
        _copy_or_append(pcpath,GIT_PC_PATH)
    else:
        print "nbgit: MUST INITIALIZE GIT"


def notebook_list():
    """ Notebook paths as list
    """
    return _rglob('*.ipynb',exclude_dirs=config.EXCLUDE_DIRS)    


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


def _rglob(match='*',root='.',exclude_dirs=[]):
    """ Recursive Glob
        Args:
            match: <str> string to match
            root: <str> dir to start recursive search
            exclude: <list[str]> list of directories to skip
    """
    matches = []
    for froot, _, filenames in os.walk(root):
        if not any(xdir in froot for xdir in exclude_dirs):
            for filename in fnmatch.filter(filenames, match):
                matches.append(os.path.join(froot, filename))
    return matches


def _copy_or_append(input_path,output_path):
    """ COPY OR APPEND input_path to output_path
    """
    if os.path.isfile(output_path): open_type='a'
    else: open_type='w'
    with open(output_path,open_type) as output_file:
        with open(input_path,'r') as input_file:
            output_file.write(input_file.read())


