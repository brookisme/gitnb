import os
import sys
import json
import re
import errno
import nb_git.config as con
import nb_git.utils as utils
from nb_git.constants import *

class Py2NB(object):
    """CONVERT NBPY to Notebook
        Args:
            path: <str> path to file
    """
    def __init__(self,path,nb_path=None):
        self._init_params()
        self.path=path
        self.nb_path=nb_path or self._nbpath()


    def json(self):
        """ get nbpy.py file as ipynb json 
            - sets ipynb dict 
            - sets ipynb json
            - returns ipynb json 
        """
        if not self._json:
            for line in self._read_py_file(self.path):
                self._process_line(line)
            self.ipynb_dict['cells']=self.cells
            self.ipynb_dict.update(self._meta())
            self._json=json.dumps(
                self.ipynb_dict,
                sort_keys=True,
                indent=con.fig('TAB_SIZE'))
        return self._json


    def convert(self):
        """ Convert .nbpy.py to .ipynb
            returns file path of ipynb file
        """
        if con.fig('CREATE_DIRS'): self._mkdirs()
        with open(self.nb_path, 'w') as outfile:
            outfile.write(self.json())
        return self.nb_path


    #
    # INTERNAL: IPYNB_DICT CONSTRUCTION
    #
    def _process_line(self,line):
        """ Process Line from file
            - if new cell: init cell
            - if end cell: 
                - close cell
                - append cell to cells
            - if cell-line: add cell-line to cell
        """
        line=self._clean(line)
        cell_type=self._is_new_cell(line)
        if cell_type: self._init_cell(cell_type)
        else:
            if self._is_end_of_cell(line):
                self._close_cell()
            else:
                if self.cell:
                    self._insert_line(line)


    def _is_new_cell(self,line):
        """ Check if new cell
            if new cell return cell-type
            else return None
        """
        if line==CODE_START:
            return CODE_TYPE
        elif line==MARKDOWN_START:
            return MARKDOWN_TYPE
        elif line==RAW_START:
            return RAW_TYPE
        else:
            return None


    def _is_end_of_cell(self,line):
        """ Check if end of cell
            return bool
        """
        if self.cell_type==CODE_TYPE:
            return line==CODE_END
        else:
            return line==UNCODE_END


    def _init_cell(self,cell_type):
        """ Initialize New Cell
        """
        self.cell_type=cell_type
        self.cell=self._new_cell(cell_type)
        if cell_type=='code':
            self.cell['execution_count']=None
            self.cell['outputs']=[]


    def _insert_line(self,line):
        """ Insert Source line into cell-source
        """
        self.cell['source'].append("{}\n".format(line))


    def _close_cell(self):
        """ Close cell
            - remove '\n' from last cell-source-line
            - set cell/cell_type to None
        """        
        lastline=self.cell['source'].pop()
        self.cell['source'].append(lastline.rstrip('\n'))
        self.cells.append(self.cell)
        self.cell=None
        self.cell_type=None


    def _new_cell(self,cell_type):
        """ Return New Cell
        """    
        return {
            "cell_type": cell_type,
            "metadata": {},
            "source": []}


    def _meta(self):
        """ Return Notebook Metadata
        """   
        major,minor,micro,_,_=sys.version_info
        return {
        "metadata": {
            "kernelspec": {
                "display_name": "Python {}".format(major),
                "language": "python",
                "name": "python{}".format(major)},
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": major},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython{}".format(major),
                "version": "{}.{}.{}".format(major,minor,micro)}},
            "nbformat": 4,
            "nbformat_minor": 2}


    #
    # INTERNAL: UTILS
    #
    def _init_params(self):
        self._json=None
        self.cells=[]
        self.cell=None
        self.cell_type=None
        self.ipynb_dict={}


    def _nbpath(self):
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
        path=re.sub('\.py$','',self.path)
        if nbpy_ident:
            path=re.sub('\.{}$'.format(nbpy_ident),'',path)
        nb_path='{}{}'.format(path,ext)
        if utils.truthy(nbpy_nb_dir):
            nb_name=os.path.basename(nb_path)
            nb_path=os.path.join(nbpy_nb_dir,nb_name)
        return nb_path


    def _mkdirs(self):
        """ Make parent dirs if they dont exist
        """
        utils.mkdirs(self.nb_path)


    def _read_py_file(self,path):
        """ Read file
            return lines list
        """ 
        with open(path,'r') as pyfile:
            lines=pyfile.readlines()
        return lines


    def _clean(self,line):
        """ Remove spaces and line break 
            from end of line
        """   
        return line.rstrip(' ').rstrip('\n').rstrip(' ')





