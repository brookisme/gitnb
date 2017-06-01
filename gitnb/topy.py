import os
import json
import re
import errno
import gitnb.config as con
import gitnb.utils as utils
from gitnb.constants import *
import gitnb.default as default


class NB2Py(object):
    """CONVERT NOTEBOOKS TO PYTHON
        Args:
            path: <str> path to file
    """
    def __init__(self,path,py_path=None):
        self._init_params()
        self.path=path
        self.py_path=py_path or default.nbpy_path(path)


    def lines(self):
        """ get lines from notebook as a list """
        if not self._lines:
            self._lines=[]
            for cell in self.notebook_dict.get(CELLS_KEY,[]):
                self._lines=self._lines+self._cell_header(cell)
                self._lines=self._lines+self._source(cell)
            if con.fig('INCLUDE_OUTPUT'):
                self._lines=self._lines+self._outputs(cell)
        return self._lines


    def convert(self):
        """ Convert .ipynb to .nbpy.py
            returns file path of nbpy file
        """
        if con.fig('CREATE_DIRS'): utils.mkdirs(self.py_path)
        with open(self.path,'r') as notebook_file:
            self.notebook_dict=json.load(notebook_file)
            file_exists=os.path.isfile(self.py_path)
            with open(self.py_path,'w') as py_file:
                for line in self.lines():
                    py_file.write('{}\n'.format(line))
        return self.py_path


    #
    # INTERNAL
    #
    def _init_params(self):
        self._lines=None


    def _cell_header(self,cell):
        lines=[]
        lines=self._append_empty_lines(lines,con.fig('LINES_BEFORE_HEADER'))
        if con.fig('HEADER_KEYS'):
            lines.append(HEADER_START.format(con.fig('HEADER_LABEL')))    
            for key in con.fig('HEADER_KEYS'):
                val=cell.get(key,'')
                lines.append("{}: {}".format(key,val))    
            lines.append(con.fig('HEADER_END'))
        lines=self._append_empty_lines(lines,con.fig('LINES_AFTER_HEADER'))
        return lines


    def _source(self,cell):
        cell_type, lines=self._cell_type_and_source_lines(cell)
        if lines:
            lines=[self._clean(line) for line in lines]
            if cell_type!=CODE_TYPE:
                lines.insert(0,UNCODE_START.format(cell.get(TYPE_KEY))) 
                lines.append(UNCODE_END) 
            else:                
                lines.insert(0,CODE_START)
                lines.append(CODE_END)     
  
        return lines

    
    def _outputs(self,cell):
        lines=[]
        outputs=cell.get(OUTPUTS_KEY,False)
        if outputs:
            lines=self._append_empty_lines(lines,LINES_BEFORE_OUTPUTS)
            lines.append(OUTPUTS_START) 
            for out in outputs: lines=lines+self._outputs(out)
            lines.append(OUTPUTS_END)  
            lines=self._append_empty_lines(lines,con.fig('LINES_AFTER_OUTPUTS'))
        return lines


    def _append_empty_lines(self,lines,n):
        for i in range(n): 
            lines.append(con.fig('EMPTY_LINE'))
        return lines


    def _clean(self,line):
        return line.rstrip(' ').rstrip('\n').rstrip(' ')


    def _cell_type_and_source_lines(self,cell):
        cell_type=cell.get(TYPE_KEY)
        source_lines=cell.get(SOURCE_KEY,[])
        return cell_type,[self._clean(line) for line in source_lines]


    def _output(self,out):
        # MAYBE DO SOMETHING MORE HERE - STRIP IMAGES ECT
        return self._clean(out.get(OUTPUT_KEY,''))
        



