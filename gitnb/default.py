import os
import re
import gitnb.config as con
import gitnb.utils as utils



def nbpy_path(ipynb_path):
    """ Get Path for nbpy.py file
        - if NBPY_IDENT: use .{ident}.py ext
        - if NBPY_DIR: put in nbpy_dir
        - else put in same direcotry as file
    """
    if re.search('\.py$',ipynb_path):
        return ipynb_path
    else:
        nbpy_ident=con.fig('NBPY_IDENT')
        nbpy_dir=con.fig('NBPY_DIR')
        if nbpy_ident: ext='.{}.py'.format(nbpy_ident)
        else: ext='.py'
        py_path=re.sub('.ipynb$',ext,ipynb_path)
        if utils.truthy(nbpy_dir):
            py_name=os.path.basename(py_path)
            py_path=os.path.join(nbpy_dir,py_name)
        return py_path


def ipynb_path(nbpy_path):
    """ Get Path for nbpy.ipynb file
        - if NBPY_NB_IDENT: use .{ident}.ipynb ext
        - if NBPY_NB_DIR: put in nbpy_nb_dir
        - else put in same direcotry as file
    """
    if re.search('\.py$',nbpy_path):
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
    else:
        return nbpy_path
