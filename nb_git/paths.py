import nb_git


GIT_DIR='./.git'
GIT_PC='./.git/hooks/pre-commit'
NBGIT_DIR=nb_git.__path__[0]
PRECOMMIT_SCRIPT='{}/precommit'.format(NBGIT_DIR)
DEFAULT_CONFIG='{}/default.config.yaml'.format(NBGIT_DIR)
USER_CONFIG='./nb_git.config.yaml'