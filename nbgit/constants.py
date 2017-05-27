###########################################################
#
# CELl BLOCK MARKERS= DENOTES BEGINING/END OF CELL
#   - For nbpy to ipynb _START must distinguish code|markdown|raw
#
###########################################################

# """ START/END of code block
# """
CODE_START='"""[code]"""'
CODE_END='""""""'

""" START/END of markdown|raw block 
    - the {} is replaced with markdown|raw
"""
UNCODE_START='"""[{}]'
UNCODE_END='"""'
MARKDOWN_START=UNCODE_START.format('markdown')
RAW_START=UNCODE_START.format('raw')

""" START/END of ouputs block
"""
OUTPUTS_START='"""[output]'
OUTPUTS_END='"""'


""" FIXED IPYNB KEYS
"""
TYPE_KEY='cell_type'
OUTPUTS_KEY='outputs'
OUTPUT_KEY='text'
SOURCE_KEY='source'
CODE_TYPE='code'
CELLS_KEY='cells'