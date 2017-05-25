#
# NOTEBOOK CONFIG
#
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

#
# DIRECTORY CONFIG
#
NBPY_DIR='nbpy' # directory to save the notebooks or None for 'same directory as notebook'
CREATE_DIRS=True
EXCLUDE_DIRS=['.ipynb_checkpoints','.git']
NBPY_IDENT='nbpy' # insert into file name for pre-commit hook