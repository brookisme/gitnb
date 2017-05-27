import os
import json
import re
import errno
import nbgit.config as con
import nbgit.utils as utils


class NB2Py(object):
    """CONVERT NOTEBOOKS TO PYTHON
        Args:
            path: <str> path to file
    """
    def __init__(self,path,py_path=None):
        self.path=path
        self.py_path=py_path or self._pypath()


    def convert(self):
        """ Convert .ipynb to .nbpy.py
            returns file path of nbpy file
        """
        if con.fig('CREATE_DIRS'): self._mkdirs()
        with open(self.path,'r') as notebook_file:
            self.notebook_dict=json.load(notebook_file)
            with open(self.py_path,'w') as py_file:
                for line in self._lines():
                    py_file.write('{}\n'.format(line))
        return self.py_path


    #
    # INTERNAL
    #
    def _lines(self):
        """ get lines from notebook as a list """
        notebook_lines=[]
        for cell in self.notebook_dict.get('cells',[]):
            notebook_lines=notebook_lines+self._cell_header(cell)
            notebook_lines=notebook_lines+self._source(cell)
        if con.fig('INCLUDE_OUTPUT'):
            notebook_lines=notebook_lines+self._outputs(cell)
        return notebook_lines


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
            if cell_type!=con.fig('CODE_TYPE'):
                lines.insert(0,con.fig('UNCODE_START').format(
                    cell.get(con.fig('TYPE_KEY'),''))) 
                lines.append(con.fig('UNCODE_END')) 
            else:
                if con.fig('CODE_START'):
                    lines.insert(0,con.fig('CODE_START').format(
                        cell.get(con.fig('TYPE_KEY'),'')))
                if con.fig('CODE_END'):
                    lines.append(con.fig('CODE_END'))       
        return lines


    def _pypath(self):
        if con.fig('NBPY_IDENT'): ext='.{}.py'.format(con.fig('NBPY_IDENT'))
        else: ext='.py'
        py_path=re.sub('.ipynb$',ext,self.path)
        if utils.truthy(con.fig('NBPY_DIR')):
            py_name=os.path.basename(py_path)
            py_path=os.path.join(con.fig('NBPY_DIR'),py_name)
        return py_path

    
    def _mkdirs(self):
        """ Make parent dirs if they dont exist
        """
        if not os.path.exists(os.path.dirname(self.py_path)):
            nb_dir=os.path.dirname(self.py_path)
            if utils.truthy(nb_dir):
                try:
                    os.makedirs(os.path.dirname(self.py_path))
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise
    

    def _outputs(self,cell):
        lines=[]
        outputs=cell.get(con.fig('OUTPUTS_KEY'),False)
        if outputs:
            lines=self._append_empty_lines(lines,LINES_BEFORE_OUTPUTS)
            lines.append(con.fig('OUTPUTS_START').format(
                cell.get(con.fig('OUTPUTS_LABEL_KEY'),con.fig('OUTPUTS_LABEL')))) 
            for out in outputs: lines=lines+self._outputs(out)
            lines.append(con.fig('OUTPUTS_END'))  
            lines=self._append_empty_lines(lines,con.fig('LINES_AFTER_OUTPUTS'))
        return lines


    def _append_empty_lines(self,lines,n):
        for i in range(n): 
            lines.append(con.fig('EMPTY_LINE'))
        return lines


    def _clean(self,line):
        return line.replace('\n','').rstrip(' ')


    def _cell_type_and_source_lines(self,cell):
        cell_type=cell.get(con.fig('TYPE_KEY'))
        source_lines=cell.get(con.fig('SOURCE_KEY'),[])
        return cell_type,[self._clean(line) for line in source_lines]


    def _output(self,out):
        # MAYBE DO SOMETHING MORE HERE - STRIP IMAGES ECT
        return self._clean(out.get(con.fig('OUTPUT_KEY'),''))
        



