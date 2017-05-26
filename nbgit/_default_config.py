###########################################################
#
# DIRECTORY/FILE CONFIG
#
###########################################################

""" NBPY_DIR/CREATE_DIRS
    - NBPY_DIR: 
        - direcotry to save .nbpy.py files
        - if None:
            files will be saved in the same dir as the associated notebook
    - CREATE_DIRS: if true directories will be created as needed
"""
NBPY_DIR='nbpy'
CREATE_DIRS=True

""" EXCLUDE_DIRS
    - list of directories to exclude when using nbgit.convert_all
"""
EXCLUDE_DIRS=['.ipynb_checkpoints','.git']

""" NBPY_IDENT
    - an identifer in filenames to marke that it was generated from an ipynb

    examples: 
        - NBPY_IDENT='nbpy'
          somenotebook.ipynb ==> somenotebook.nbpy.py
        - NBPY_IDENT=None
          somenotebook.ipynb ==> somenotebook.py
"""
NBPY_IDENT='nbpy'

""" AUTO_ADD_NBPY
    - if True .nbpy.py files will be added to the git repo upon generation
"""
AUTO_ADD_NBPY=True




###########################################################
#
# CELl SPACING
#
###########################################################

""" EMPTY_LINE
    string to place in the lines before/after given below
"""
EMPTY_LINE=''


""" LINES_BEFORE/AFTER
    The number of EMPTY_LINEs to include before/after each
    - HEADER: empyt lines are included even if HEADER_KEYS=[]
    - SOURCE: the input cell
    - OUTPUTS: the output cell
"""
LINES_BEFORE_HEADER=2
LINES_AFTER_HEADER=0
LINES_BEFORE_SOURCE=2
LINES_AFTER_SOURCE=0
LINES_BEFORE_OUTPUTS=2
LINES_AFTER_OUTPUTS=0
LINES_BETWEEN_OUTPUTS=1



###########################################################
#
# CELl BLOCK MARKERS: DENOTES BEGINING/END OF CELL
#   - For nbpy to ipynb _START must distinguish code|markdown|raw
#
###########################################################

""" START/END of code block
"""
CODE_START='# ----------------- [code] -----------------'
CODE_END='# ----------------------------------------'

""" START/END of markdown|raw block 
    - the {} is replaced with markdown|raw
"""
UNCODE_START='"""[{}]'
UNCODE_END='"""'

""" START/END of ouputs block
    - the {} is replaced with the value of from OUTPUTS_LABEL_KEY
    - if OUTPUTS_LABEL_KEY=None {} is replaced with OUTPUTS_LABEL
"""
OUTPUTS_START='"""[{}]'
OUTPUTS_END='"""'
OUTPUTS_LABEL_KEY=None
OUTPUTS_LABEL='output'




###########################################################
#
# nbpy.py file CONFIG
#
###########################################################

""" INCLUDE_OUTPUT
    - if True output cells will be included in nbpy.py file
    - We strongly suggest False :)
"""
INCLUDE_OUTPUT=False

""" HEADERS
    Headers will appear before the cell block with meta-data.
    - HEADER_KEYS:
        - list of keys for meta-data that can be included in header
        - if None (suggest) no header will be included
        - options:
            - execution_count: (the input/ouput number)
            - cell_type: (code|markdown|raw) 
                note - cell_type is already included in block markers
    - HEADER_LABEL/START/END
        - how to block off the header data
"""
HEADER_KEYS=[] 
HEADER_LABEL='cell-data'
HEADER_START='"""{}'
HEADER_END='"""'




###########################################################
###########################################################
###########################################################
#
# DANGER ZONE: DO NOT EDIT. FIXED NOTEBOOK KEYS
#
###########################################################
###########################################################
###########################################################
TYPE_KEY='cell_type'
OUTPUTS_KEY='outputs'
OUTPUT_KEY='text'
SOURCE_KEY='source'
CODE_TYPE='code'
