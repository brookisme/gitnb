import gitnb

#
# GIT
#
GIT_DIR='./.git'
GIT_PC='./.git/hooks/pre-commit'


#
# GitNB
#
GITNB_DIR=gitnb.__path__[0]
DEFAULT_CONFIG='{}/default.config.yaml'.format(GITNB_DIR)
USER_CONFIG='./gitnb.config.yaml'
DOT_GITNB_CONFIG_DIR='{}/dot_gitnb'.format(GITNB_DIR)
GITNB_CONFIG_DIR='./.gitnb'
PRECOMMIT_SCRIPT='{}/precommit'.format(DOT_GITNB_CONFIG_DIR)
DEFAULT_GITIGNORE='{}/default_gitignore'.format(DOT_GITNB_CONFIG_DIR)
NOTEBOOK_LIST='{}/notebooks'.format(GITNB_CONFIG_DIR)

