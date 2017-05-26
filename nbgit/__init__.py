from __future__ import print_function
import os
import re
import argparse
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
        print("nbgit: MUST INITIALIZE GIT")


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
    if noisy: print('\tnbgit[convert notebooks]:')
    for path in notebook_list():
        convert(path)


def convert(path,noisy=True):
    """ Convert Notebook
    """
    if not path:
        print('\tnbgit: ERROR - MUST PROVIDE FILE PATH TO CONVERT')
    else:
        if noisy: print('\t\t{}'.format(path))
        nbpy_path=NB2Py(path).convert()
        if AUTO_ADD_NBPY:
            utils.git_add(nbpy_path)

    
#######################################################
#
# CLI 
#
#######################################################


#
# args methods:
#
def _install(args):
    return install()

def _configure(args):
    return configure()

def _notebook_list(args):
    for nb in notebook_list():
        print('\tnbgit:',nb)

def _convert(args):
    conv_all=utils.truthy(args.all)
    noisy=utils.truthy(args.noisy)
    if conv_all: 
        return convert_all(noisy)
    else:
        return convert(args.file,noisy)


#
# MAIN
#
def main():
    parser=argparse.ArgumentParser(description='NBGIT: TRACKING FOR PYTHON NOTEBOOKS')
    subparsers=parser.add_subparsers()
    # install
    parser_install=subparsers.add_parser(
        'install', help='installs nbgit into local project (writes to .git/hooks/pre-commit')
    parser_install.set_defaults(func=_install)    
    # configure
    parser_configure=subparsers.add_parser(
        'configure', help='creates local configuration file ({})'.format(CONFIG_PATH))
    parser_configure.set_defaults(func=_configure)    
    # nblist
    parser_nb_list=subparsers.add_parser(
        'nblist', help='list all noteboks (that are not in EXCLUDE_DIRS')
    parser_nb_list.set_defaults(func=_notebook_list)  
    # convert
    parser_convert=subparsers.add_parser(
        'convert',help='convert .ipynb files to .nbpy.py files')
    parser_convert.add_argument(
        '-a','--all',default=False,help='convert all notebooks listed with <nblist>')
    parser_convert.add_argument(
        '-f','--file',help='path to file to convert')
    parser_convert.add_argument(
        '-n','--noisy',default=True,help='print out files being converted')
    parser_convert.set_defaults(func=_convert)    
    # run
    args=parser.parse_args()
    args.func(args)



if __name__ == "__main__": 
    main()



