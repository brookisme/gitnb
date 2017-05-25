import os
import json
import re
from nbgit.config import *


class NB2Py(object):
    """CONVERT NOTEBOOKS TO PYTHON
        Args:
            path: <str> path to file
    """
    def __init__(self,path,py_path=None):
        self.path=path
        self.py_path=py_path or self._pypath()


    def convert(self):
        """ converts ipynb to .py """
        if CREATE_DIRS: self._mkdirs()
        with open(self.path,'r') as notebook_file:
            self.notebook_dict=json.load(notebook_file)
            with open(self.py_path,'w') as py_file:
                for line in self._lines():
                    py_file.write('{}\n'.format(line))


    #
    # INTERNAL
    #
    def _lines(self):
        """ get lines from notebook as a list """
        notebook_lines=[]
        for cell in self.notebook_dict.get('cells',[]):
            notebook_lines=notebook_lines+self._cell_header(cell)
            notebook_lines=notebook_lines+self._source(cell)
        if INCLUDE_OUTPUT:
            notebook_lines=notebook_lines+self._outputs(cell)
        return notebook_lines


    def _cell_header(self,cell):
        lines=[]
        lines=self._append_empty_lines(lines,LINES_BEFORE_HEADER)
        if HEADER_KEYS:
            lines.append(HEADER_START.format(HEADER_LABEL))    
            for key in HEADER_KEYS:
                val=cell.get(key,'')
                lines.append("{}: {}".format(key,val))    
            lines.append(HEADER_END)
        lines=self._append_empty_lines(lines,LINES_AFTER_HEADER)
        return lines


    def _source(self,cell):
        cell_type, lines=self._cell_type_and_source_lines(cell)
        if lines:
            lines=[self._clean(line) for line in lines]
            if cell_type!=CODE_TYPE:
                lines.insert(0,UNCODE_START.format(cell.get(TYPE_KEY,''))) 
                lines.append(UNCODE_END) 
            else:
                if CODE_START:
                    lines.insert(0,CODE_START.format(cell.get(TYPE_KEY,'')))
                if CODE_END:
                    lines.append(CODE_END)       
        return lines


    def _pypath(self):
        py_path=re.sub('.ipynb$','.py',self.path)
        if NBPY_DIR:
            py_name=os.path.basename(py_path)
            py_path=os.path.join(NBPY_DIR,py_name)
        return py_path

    
    def _mkdirs(self):
        """ Make parent dirs if they dont exist
        """
        if not os.path.exists(os.path.dirname(self.py_path)):
            try:
                os.makedirs(os.path.dirname(self.py_path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
    

    def _outputs(self,cell):
        lines=[]
        outputs=cell.get(OUTPUTS_KEY,False)
        if outputs:
            lines=self._append_empty_lines(lines,LINES_BEFORE_OUTPUTS)
            lines.append(OUTPUTS_START.format(cell.get(OUTPUTS_LABEL_KEY,OUTPUTS_LABEL))) 
            for out in outputs: lines=lines+self._outputs(out)
            lines.append(OUTPUTS_END)  
            lines=self._append_empty_lines(lines,LINES_AFTER_OUTPUTS)
        return lines


    def _append_empty_lines(self,lines,n):
        for i in range(n): 
            lines.append(EMPTY_LINE)
        return lines


    def _clean(self,line):
        return line.replace('\n','').rstrip(' ')


    def _cell_type_and_source_lines(self,cell):
        cell_type=cell.get(TYPE_KEY)
        source_lines=cell.get(SOURCE_KEY,[])
        return cell_type,[self._clean(line) for line in source_lines]


    def _output(self,out):
        # MAYBE DO SOMETHING MORE HERE - STRIP IMAGES ECT
        return self._clean(out.get(OUTPUT_KEY,''))
        



