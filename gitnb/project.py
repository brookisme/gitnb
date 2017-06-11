import os
import re
import gitnb.utils as utils
import gitnb.config as con
from gitnb.topy import NB2Py
from gitnb.paths import *


#
# CONFIG
#
NOTEBOOKS_SEP='|'
NOTEBOOKS_FMT='{} {} {}'



#
# GitNBProject:
#
class GitNBProject(object):
    #
    # STATIC METHODS
    #
    @staticmethod
    def initialize():
        """ Installs GITNB
            - installs git pre-commit hook
            - creates .gitnb dir
        """
        if os.path.isfile(GIT_PC):
            nb_match=utils.nb_matching_lines('gitnb',GIT_PC)
        else:
            nb_match=0
        if nb_match>0:
            print("\ngitnb[WARNING]:")
            print("\tit appears you have already initialized gitnb for")
            print("\tthis project. verify: cat .git/hooks/pre-commit\n")
        else:
            if os.path.exists(GIT_DIR):
                cmd1='cp -R {} {}'.format(DOT_GITNB_CONFIG_DIR,GITNB_CONFIG_DIR)
                os.system(cmd1)
                utils.copy_append(PRECOMMIT_SCRIPT,GIT_PC)
                cmd2='chmod +x {}'.format(GIT_PC)
                os.system(cmd2)
                print("\ngitnb: INSTALLED ")
                print("\t - nbpy.py files will be created/updated/tracked")
                print("\t - install user config with: $ gitnb configure\n")
            else:
                print("gitnb: MUST INITIALIZE GIT")


    @staticmethod
    def configure():
        """ Install config file
            allows user to change config
        """
        utils.copy_append(DEFAULT_CONFIG,USER_CONFIG,'w')
        print("gitnb: USER CONFIG FILE ADDED ({}) ".format(USER_CONFIG))


    

    #
    # INSTANCE METHODS
    #
    def __init__(self):
        self._notebooks= None
        self._all_notebooks= None
        self._tracked_notebooks= None
        self._untracked_notebooks= None



    def all_notebooks(self):
        nbks_list=utils.rglob(
            '*.ipynb',exclude_dirs=con.fig('EXCLUDE_DIRS'))
        nbks_list=[self._clean_path(nbk) for nbk in nbks_list]
        return nbks_list
    
    
    def notebooks(self):
        nbks_dict={}
        nbks_lines=utils.read_lines(NOTEBOOK_LIST)
        for line in nbks_lines:
            parts=line.split(NOTEBOOKS_SEP)
            if len(parts)==2:
                key, value=(self._clean(part) for part in parts)
                nbks_dict[key]=value
        return nbks_dict

    
    def list_notebooks(self):
        return self.notebooks().keys()  
    

    def list_nbpys(self):
        return self.notebooks().values()

    
    def list_untracked(self):
        all_set=set(self.all_notebooks())
        tracked_set=set(self.list_notebooks())
        return list(all_set-tracked_set)


    def update(self):
        for path,nbpy_path in self.notebooks().items():
            if os.path.isfile(path):
                NB2Py(path,nbpy_path).convert()
                if con.fig('GIT_ADD_ON_GITNB_UPDATE'):
                    utils.git_add(nbpy_path)
            else:
                msg='tracked notebook {} is not in local system'.format(path)
                print('gitnb[update]: {}'.format(msg))


    def add(self,path,nbpy_path=None):
        msg=None
        added_file=False
        nbks=self.notebooks()
        if not nbks.get(path):
            if nbpy_path in self.list_nbpys():
                msg='nbpy.py file ({}) already added'.format(nbpy_path)
            else:
                if os.path.isfile(path):
                    nbpy_path=NB2Py(path,nbpy_path).convert()
                    self._append_notebooks(path,nbpy_path)
                    if con.fig('GIT_ADD_ON_GITNB_ADD'):
                        utils.git_add(nbpy_path)
                else:
                    msg='notebook ({}) does not exist'.format(path)
            if msg: self._out(msg,'WARNING')
        return added_file


    def remove(self,path):
        if not path in self.list_notebooks():
            level='WARNING'
            msg='{} is not being tracked'.format(path)
        else:
            nb_match=utils.nb_matching_lines(
                path,NOTEBOOK_LIST)
            if nb_match==0:
                level='ERROR'
                msg="failed to remove {} from {}".format(
                    path,NOTEBOOK_LIST)
            if nb_match>1:
                level='WARNING'
                msg="more than one line matching {} in {}".format(
                    path,NOTEBOOK_LIST)
            else:
                level=None
                utils.remove_lines(path,NOTEBOOK_LIST)
                msg="{} no longer being tracked".format(path)
        self._out(msg,level)
        return path


    def _append_notebooks(self,path,nbpy_path):
        nbk_line=NOTEBOOKS_FMT.format(path,NOTEBOOKS_SEP,nbpy_path)
        self._out('add ({})'.format(nbk_line))
        with open(NOTEBOOK_LIST, "a") as nbks_file:
            nbks_file.write('\n{}'.format(nbk_line))
        

    def _out(self,msg,level=None):
        if level: info="gitnb[{}]".format(level)
        else: info="gitnb"
        print("{}: {}".format(info,msg))


    def _clean_path(self,string):
        return re.sub('^\.\/','',string)


    def _clean(self,string):
        return string.strip(' ').strip('\n').strip(' ')

