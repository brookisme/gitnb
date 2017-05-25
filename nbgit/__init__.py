# __init__.py
import os
import errno
import fnmatch
import config
from nbgit.converter import NB2Py


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

