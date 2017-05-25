#!/usr/bin/env python
from __future__ import print_function
import nbgit
import os
import subprocess

#
# HELPERS
#
def git_add(match):
    cmd=' '.join(['git add',match])
    subprocess.check_output(cmd, shell=True)


#
# CONVERT
#
print('nbgit: looking for notebooks...')
nbgit.convert_all()
print('nbgit: adding nbpy')


#
# ADD FILES TO REPO
#
fmatch='*.{}.py'.format(nbgit.config.NBPY_IDENT)
git_add(fmatch)
git_add('**/{}'.format(fmatch))