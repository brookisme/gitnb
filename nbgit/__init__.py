from __future__ import print_function
import os
import re
import argparse
import nbgit.paths as paths
import nbgit.utils as utils
from nbgit.topy import NB2Py
from nbgit.tonb import Py2NB
import nbgit.config as con



def install():
    """ Installs pre-commit hook
    """
    if os.path.exists(paths.GIT_DIR):
        utils.copy_append(paths.PRECOMMIT_SCRIPT,paths.GIT_PC)
        os.system('chmod +x {}'.format(paths.GIT_PC))
    else:
        print("nbgit: MUST INITIALIZE GIT")


def configure():
    """ Install config file
        allows user to change config
    """
    utils.copy_append(paths.DEFAULT_CONFIG,paths.USER_CONFIG,'w')


def notebook_list():
    """ Notebook paths as list
    """
    return utils.rglob('*.ipynb',exclude_dirs=con.fig('EXCLUDE_DIRS'))    


def nbpy_list():
    """ TODO: Notebook paths as list
    """
    print("TODO: Notebook paths as list")
    pass


def topy_all(noisy=True):
    """ Convert all Notebooks
    """
    if noisy: print('\tnbgit[topy notebooks]:')
    for path in notebook_list():
        topy(path)


def topy(path,destination_path=None,noisy=True):
    """ Convert Notebook to Py
    """
    if not path:
        print('\tnbgit: ERROR - MUST PROVIDE FILE PATH TO CONVERT')
    else:
        if noisy: print('\t\t{}'.format(path))
        nbpy_path=NB2Py(path,destination_path).topy()
        if con.fig('AUTO_ADD_NBPY'):
            utils.git_add(nbpy_path)


def tonb_all(noisy=True):
    """ TODO: Convert all NBPY files to Notebooks
    """
    # if noisy: print('\tnbgit[tonb nbpy-files]:')
    # for path in notebook_list():
    #     topy(path)
    print("TODO: Convert all NBPY files to Notebooks")
    pass


def tonb(path,destination_path=None,noisy=True):
    """ Convert Notebook to Py
    """
    if not path:
        print('\tnbgit: ERROR - MUST PROVIDE FILE PATH TO CONVERT')
    else:
        if noisy: print('\t\t{}'.format(path))
        nbpy_path=Py2NB(path,destination_path).topy()
        if con.fig('AUTO_ADD_NBPY'):
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


def _nbpy_list(args):
    for nbpy in nbpy_list():
        print('\tnbgit:',nbpy)


def _topy(args):
    conv_all=utils.truthy(args.all)
    noisy=utils.truthy(args.noisy)
    if conv_all: 
        return topy_all(noisy)
    else:
        return topy(args.source,args.destination,noisy)


def _tonb(args):
    conv_all=utils.truthy(args.all)
    noisy=utils.truthy(args.noisy)
    if conv_all: 
        return tonb_all(noisy)
    else:
        return tonb(args.source,args.destination,noisy)

#
# MAIN
#
def main():
    parser=argparse.ArgumentParser(description='NBGIT: TRACKING FOR PYTHON NOTEBOOKS')
    subparsers=parser.add_subparsers()
    # install
    parser_install=subparsers.add_parser(
        'install',
        help='installs nbgit into local project (writes to .git/hooks/pre-commit')
    parser_install.set_defaults(func=_install)    
    # configure
    parser_configure=subparsers.add_parser(
        'configure',
        help='creates local configuration file ({})'.format(paths.USER_CONFIG))
    parser_configure.set_defaults(func=_configure)    
    # nblist
    parser_nb_list=subparsers.add_parser(
        'nblist',
        help='list all noteboks (that are not in EXCLUDE_DIRS')
    parser_nb_list.set_defaults(func=_notebook_list)  
    # topy
    parser_topy=subparsers.add_parser(
        'topy',
        help='topy .ipynb files to .nbpy.py files')
    parser_topy.add_argument(
        '-a','--all',default=False,
        help='topy all notebooks listed with <nblist>')
    parser_topy.add_argument(
        '-s','--source',
        help='path to source-file to topy')
    parser_topy.add_argument(
        '-d','--destination',default=None,
        help='(optional) path for output file. will use default path if not provided')
    parser_topy.add_argument(
        '-n','--noisy',default=True,help='print out files being topy-ed')
    parser_topy.set_defaults(func=_topy)
    # tonb
    parser_tonb=subparsers.add_parser(
        'tonb',
        help='tonb .ipynb files to .nbpy.py files')
    parser_tonb.add_argument(
        '-a','--all',default=False,
        help='tonb all python files listed with <nbpylist>')
    parser_topy.add_argument(
        '-s','--source',
        help='path to source-file to topy')
    parser_topy.add_argument(
        '-d','--destination',default=None,
        help='(optional) path for output file. will use default path if not provided')
    parser_tonb.add_argument(
        '-n','--noisy',default=True,
        help='print out files being tonb-ed')
    parser_tonb.set_defaults(func=_tonb)   
    # run
    args=parser.parse_args()
    args.func(args)



if __name__ == "__main__": 
    main()



