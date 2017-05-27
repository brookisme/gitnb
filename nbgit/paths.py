import nbgit


GIT_DIR='./.git'
GIT_PC='./.git/hooks/pre-commit'
NBGIT_DIR=nbgit.__path__[0]
PRECOMMIT_SCRIPT='{}/precommit'.format(NBGIT_DIR)
DEFAULT_CONFIG='{}/default.config.yaml'.format(NBGIT_DIR)
USER_CONFIG='./nbgit.config.yaml'