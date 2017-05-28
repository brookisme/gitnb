import os
import sys
import json
import re
import errno
import nbgit.config as con
import nbgit.utils as utils
from nbgit.constants import *

class Py2NB(object):
    """CONVERT NBPY to Notebook
        Args:
            path: <str> path to file
    """
    cells=[]
    cell=None
    cell_type=None
    ipynb_dict={}
    
    def __init__(self,lines):
        self.lines=lines
        for line in lines:
            self._process_line(line)
        self.ipynb_dict['cells']=self.cells
        self.ipynb_dict.update(self._meta())


    def write(self,fname):
        ipynb_json=json.dumps(
            self.ipynb_dict,
            sort_keys=True,
            indent=con.fig('TAB_SIZE'))
        with open(fname, 'w') as outfile:
            outfile.write(ipynb_json)


    #
    # INTERNAL: IPYNB_DICT CONSTRUCTION
    #
    def _process_line(self,line):
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
        if line==CODE_START:
            return "code"
        elif line==MARKDOWN_START:
            return "markdown"
        elif line==RAW_START:
            return "raw"
        else:
            return None


    def _is_end_of_cell(self,line):
        if self.cell_type==CODE_TYPE:
            return line==CODE_END
        else:
            return line==UNCODE_END


    def _init_cell(self,cell_type):
        self.cell_type=cell_type
        self.cell=self._new_cell(cell_type)
        if cell_type=='code':
            self.cell['execution_count']=None
            self.cell['outputs']=[]


    def _insert_line(self,line):
        self.cell['source'].append("{}\n".format(line))


    def _close_cell(self):
        lastline=self.cell['source'].pop()
        self.cell['source'].append(lastline.rstrip('\n'))
        self.cells.append(self.cell)
        self.cell=None
        self.cell_type=None


    def _new_cell(self,cell_type):
        return {
            "cell_type": cell_type,
            "metadata": {},
            "source": []}


    def _meta(self):
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
    # UTILS
    #
    def _clean(self,s):
        return s.rstrip('\n').rstrip(' ')


    def _eq(self,s1,s2):
        return s1==s2





