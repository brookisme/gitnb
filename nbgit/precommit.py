#!/usr/bin/env python
from __future__ import print_function
import nbgit
import os
import subprocess

#########################################################################
#
# NBGIT: 
#   -   This file is automatically created/append to .git/hooks/pre-commit 
#       upon nbgit.install().
#   -   Upon commiting:
#       - all notebooks will be converted to .nbpy.py files
#       - the .nbpy.py files are added to the repo
#   
#########################################################################

#
# HELPERS
#
def git_add(match):
    cmd=' '.join(['git add',match])
    subprocess.check_output(cmd, shell=True)


#
# CONVERT
#
def convert_notebooks():
    print('nbgit: looking for notebooks...')
    nbgit.convert_all()
    print('nbgit: adding nbpy')


#
# ADD FILES TO REPO
#
def add_files_to_repo():
    fmatch='*.{}.py'.format(nbgit.config.NBPY_IDENT)
    git_add(fmatch)
    git_add('**/{}'.format(fmatch))


if __name__ == "__main__": 
    convert_notebooks()
    add_files_to_repo()


