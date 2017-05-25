# __init__.py
import os
import fnmatch

def notebook_list():
    return rglob('*.ipynb')


def rglob(match='*',root='.'):
    """ Recursive Glob
    """
    matches = []
    for froot, _, filenames in os.walk(root):
      for filename in fnmatch.filter(filenames, match):
          matches.append(os.path.join(froot, filename))
    return matches