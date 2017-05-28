###########################################################
#
# CELl BLOCK MARKERS= DENOTES BEGINING/END OF CELL
#   - For nbpy to ipynb _START must distinguish code|markdown|raw
#
###########################################################

""" FIXED IPYNB KEYS
"""
TYPE_KEY='cell_type'
OUTPUTS_KEY='outputs'
OUTPUT_KEY='text'
SOURCE_KEY='source'
CELLS_KEY='cells'
CODE_TYPE='code'
MARKDOWN_TYPE='markdown'
RAW_TYPE='raw'


# """ START/END of code block
# """
CODE_START='"""[{}]"""'.format(CODE_TYPE)
CODE_END='""""""'

""" START/END of markdown|raw block 
    - the {} is replaced with markdown|raw
"""
UNCODE_START='"""[{}]'
UNCODE_END='"""'
MARKDOWN_START=UNCODE_START.format(MARKDOWN_TYPE)
RAW_START=UNCODE_START.format(RAW_TYPE)

""" START/END of ouputs block
"""
OUTPUTS_START='"""[output]'
OUTPUTS_END='"""'

