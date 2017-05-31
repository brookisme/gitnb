import nb_git
import nb_git.config as con

#
# GIT
#
GIT_DIR='./.git'
GIT_PC='./.git/hooks/pre-commit'


#
# NB_GIT
#
NBGIT_DIR=nb_git.__path__[0]
DEFAULT_CONFIG='{}/default.config.yaml'.format(NBGIT_DIR)
USER_CONFIG='./nb_git.config.yaml'
DOT_NBGIT_CONFIG_DIR='{}/dot_nb_git'.format(NBGIT_DIR)
NBGIT_CONFIG_DIR='./.nb_git'
PRECOMMIT_SCRIPT='{}/precommit'.format(DOT_NBGIT_CONFIG_DIR)
NOTEBOOK_LIST='./{}/notebooks'.format(NBGIT_CONFIG_DIR)


#
# 
#
class DEFAULT_PATHS(object):

    @staticmethod
    def nbpy(ipynb_path):
        """ Get Path for nbpy.py file
            - if NBPY_IDENT: use .{ident}.py ext
            - if NBPY_DIR: put in nbpy_dir
            - else put in same direcotry as file
        """
        nbpy_ident=con.fig('NBPY_IDENT')
        nbpy_dir=con.fig('NBPY_DIR')
        if nbpy_ident: ext='.{}.py'.format(nbpy_ident)
        else: ext='.py'
        py_path=re.sub('.ipynb$',ext,ipynb_path)
        if truthy(nbpy_dir):
            py_name=os.path.basename(py_path)
            py_path=os.path.join(nbpy_dir,py_name)
        return py_path


    @staticmethod
    def ipynb(nbpy_path):
        """ Get Path for nbpy.ipynb file
            - if NBPY_NB_IDENT: use .{ident}.ipynb ext
            - if NBPY_NB_DIR: put in nbpy_nb_dir
            - else put in same direcotry as file
        """
        nbpy_ident=con.fig('NBPY_IDENT')
        nbpy_nb_ident=con.fig('NBPY_NB_IDENT')
        nbpy_nb_dir=con.fig('NBPY_NB_DIR')
        if nbpy_nb_ident: ext='.{}.ipynb'.format(nbpy_nb_ident)
        else: ext='.ipynb'
        path=re.sub('\.py$','',nbpy_path)
        if nbpy_ident:
            path=re.sub('\.{}$'.format(nbpy_ident),'',path)
        nb_path='{}{}'.format(path,ext)
        if utils.truthy(nbpy_nb_dir):
            nb_name=os.path.basename(nb_path)
            nb_path=os.path.join(nbpy_nb_dir,nb_name)
        return nb_path


