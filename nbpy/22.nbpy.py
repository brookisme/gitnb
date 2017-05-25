

# ----------------- [code] -----------------
import json
from pprint import pprint
# ----------------------------------------


"""[markdown]
## LOAD EXAMPLE NOTEBOOK
The example notebook is the same as this one except in
the next input we put 'firstpass.ipynb' without the '.example'
Note 'firstpass.ipynb' is excluded from the repo since its a notebook
"""


# ----------------- [code] -----------------
with open('firstpass.ipynb.example') as data_file:
    nb = json.load(data_file)
# ----------------------------------------


# ----------------- [code] -----------------
# # Print outut nb to think about what to include and get keys
# pprint(nb)
# ----------------------------------------


"""[markdown]
## GET CELLS
"""


# ----------------- [code] -----------------
cells=nb.get('cells',[])
# ----------------------------------------


# ----------------- [code] -----------------
# # Print out cells
# pprint('\n\n\n',cells[0])
# ----------------------------------------


"""[markdown]
## CONFIG
"""


# ----------------- [code] -----------------
TYPE_KEY='cell_type'
INCLUDE_OUTPUT=False
OUTPUTS_KEY='outputs'
OUTPUT_KEY='text'
HEADER_KEYS=[] # DEFAULT SHOULD BE EMPTY [], but you could say have ['execution_count'] or something
SOURCE_KEY='source'
CODE_TYPE='code'
EMPTY_LINE=''
LINES_BEFORE_HEADER=2
LINES_AFTER_HEADER=0
LINES_BEFORE_SOURCE=2
LINES_AFTER_SOURCE=0
LINES_BEFORE_OUTPUTS=2
LINES_AFTER_OUTPUTS=0
LINES_BETWEEN_OUTPUTS=1
HEADER_LABEL='cell-data'
HEADER_START='"""{}'
HEADER_END='"""'
CODE_START='# ----------------- [code] -----------------'
CODE_END='# ----------------------------------------'
UNCODE_START='"""[{}]'
UNCODE_END='"""'
OUTPUTS_START='"""[{}]'
OUTPUTS_END='"""'
OUTPUTS_LABEL_KEY=None
OUTPUTS_LABEL='output'
# ----------------------------------------


"""[markdown]
## METHODS
"""


# ----------------- [code] -----------------

def _append_empty_lines(lines,n):
    for i in range(n):
        lines.append(EMPTY_LINE)
    return lines


def cell_header(cell):
    lines=[]
    lines=_append_empty_lines(lines,LINES_BEFORE_HEADER)
    if HEADER_KEYS:
        lines.append(HEADER_START.format(HEADER_LABEL))
        for key in HEADER_KEYS:
            val=cell.get(key,'')
            lines.append("{}: {}".format(key,val))
        lines.append(HEADER_END)
    lines=_append_empty_lines(lines,LINES_AFTER_HEADER)
    return lines


def _clean(line):
    return line.replace('\n','').rstrip(' ')


def _cell_type_and_source_lines(cell):
    cell_type=cell.get(TYPE_KEY)
    source_lines=cell.get(SOURCE_KEY,[])
    return cell_type,[_clean(line) for line in source_lines]


def source(cell):
    cell_type, lines=_cell_type_and_source_lines(cell)
    if lines:
        lines=[_clean(line) for line in lines]
        if cell_type!=CODE_TYPE:
            lines.insert(0,UNCODE_START.format(cell.get(TYPE_KEY,'')))
            lines.append(UNCODE_END)
        else:
            if CODE_START:
                lines.insert(0,CODE_START.format(cell.get(TYPE_KEY,'')))
            if CODE_END:
                lines.append(CODE_END)
    return lines


def _output(out):
    # MAYBE DO SOMETHING MORE HERE - STRIP IMAGES ECT
    return _clean(out.get(OUTPUT_KEY,''))


def outputs(cell):
    lines=[]
    outputs=cell.get(OUTPUTS_KEY,False)
    if outputs:
        lines=_append_empty_lines(lines,LINES_BEFORE_OUTPUTS)
        lines.append(OUTPUTS_START.format(cell.get(OUTPUTS_LABEL_KEY,OUTPUTS_LABEL)))
        for out in outputs: lines=lines+_outputs(out)
        lines.append(OUTPUTS_END)
        lines=_append_empty_lines(lines,LINES_AFTER_OUTPUTS)
    return lines
# ----------------------------------------


"""[markdown]
## GET LINES
"""


"""[raw]
This is the raw-nb-convert cell that I am putting in to see how it works. I've never used this cell-type.
"""


# ----------------- [code] -----------------
notebook_lines=[]
for cell in cells:
    notebook_lines=notebook_lines+cell_header(cell)
    notebook_lines=notebook_lines+source(cell)
    if INCLUDE_OUTPUT:
        notebook_lines=notebook_lines+outputs(cell)
# ----------------------------------------


# ----------------- [code] -----------------
# # print out notebook_lines
# nb_lines
# ----------------------------------------


"""[markdown]
## Write to file
"""


# ----------------- [code] -----------------
with open('firstpass-example.py','w') as file:
    for line in notebook_lines:
        file.write('{}\n'.format(line))
# ----------------------------------------


"""[markdown]
## TEST CLASS
"""


# ----------------- [code] -----------------
from nbgit.converter import NB2Py
# ----------------------------------------


# ----------------- [code] -----------------
nbc=NB2Py('firstpass.ipynb.example','firstpass.nb2py.py')
# ----------------------------------------


# ----------------- [code] -----------------
nbc.convert()
# ----------------------------------------


