import nb_git

#
# GIT
#
GIT_DIR='./.git'
GIT_PC='./.git/hooks/pre-commit'


#
# NB_GIT
#
NBGIT_DIR=nb_git.__path__[0]
DEFAULT_CONFIG='{}/default.config.yaml'.format(NBGIT_DIR)
USER_CONFIG='./nb_git.config.yaml'
DOT_NBGIT_CONFIG_DIR='{}/dot_nb_git'.format(NBGIT_DIR)
NBGIT_CONFIG_DIR='./.nb_git'
PRECOMMIT_SCRIPT='{}/precommit'.format(DOT_NBGIT_CONFIG_DIR)
NOTEBOOK_LIST='./{}/notebooks'.format(NBGIT_CONFIG_DIR)
