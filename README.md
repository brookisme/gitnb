## NBGIT 
_this is a [work in progress](#wip)_

GIT TRACKING FOR PYTHON NOTEBOOKS

###### USAGE:

```bash
# in some project containing some ipython-notebooks
git commit -am "some commit message"
```

Thats it!

NBGIT doesn't actually track python notebooks. Instead, everytime you perform a `git commit`:

* NBGIT automatically updates (or creates) a .py version of the notebook 
* NBGIT performs a `git add` for any new .py versions (you can turn this off by setting AUTO_ADD_NBPY=False)

This allows you to track any changes to your notebook (by tracking changes to its .py copy). 

If you ever need to recover a notebook from a previous commit, or you are collaborating with others and they too would like a working copy of the notebook, there is a [CLI](#cli) command that creates a new notebook from the .py versions.



* adds .py version to your git repo

* create ipynb->py converter that ignores all the stuff that makes git tracking hard
* use git pre-commit hooks to
    * copy all .ipynb to .py files
    * git add the new .py files to the repo
* you can create new notebooks from the `nbpy.py` files using the 

Here is an example output file:

https://github.com/brookisme/nb_git/blob/master/NBGit%20Example%20Notebook.nbpy.py

File Location/Naming/Layout/Ect... is configurable with the user [config file](#config), and there is a CLI for performing these operations outside of the git commit.

--------------------------------
### INSTALL NBGIT

```bash
# pip
pip install -U nb_git

# latest-dev version
git clone https://github.com/brookisme/nb_git.git
cd nb_git
sudo pip install -e .
```


--------------------------------
### PROJECT INSTALL

* you should probably add `*.ipynb` to your `.gitignore`
* before installing for your project you must first init the git repo
* the command below will create or append your `.git/hooks/pre-commit` file so that, upon git commit it will:
    * copy all .ipynb to .py files
    * git add the new .py files to the repo
* install git-hooks 

```bash
nb_git install
```

<a name='config'></a>
* ( optional - only if you want to change the [defaults](https://github.com/brookisme/nb_git/blob/master/nb_git/default.config.yaml) ): install user config file (nb_git.config.yaml).  See comment-docs for details.

```bash
nb_git configure
```

--------------------------------
<a name='cli'></a>
### OTHER CLI COMMANDS:

In addition to the commands above, the CLI provides `nblist` (notebook-list), `tonb` (to-notebook), `topy` (to-python) and  which do what you think they do.  

Here is a `tonb` example:

```bash
# using default destination path
nb_git tonb -s soure_file.nbpy.py

# specifiy destination path
nb_git tonb -s soure_file.nbpy.py -d output_file.nbpy.ipynb
```

Here are the docs:

```bash
nb_git-repo|master $ nb_git --help
usage: nb_git [-h] {install,configure,nblist,topy,tonb} ...

NBGIT: TRACKING FOR PYTHON NOTEBOOKS

positional arguments:
  {install,configure,nblist,topy,tonb}
    install             installs nb_git into local project (writes to
                        .git/hooks/pre-commit
    configure           creates local configuration file (./nb_git.config.yaml)
    nblist              list all noteboks (that are not in EXCLUDE_DIRS
    topy                topy .ipynb files to .nbpy.py files
    tonb                tonb .ipynb files to .nbpy.py files

optional arguments:
  -h, --help            show this help message and exit
```

```bash
# ** tonb has the same options **
nb_git-repo|master $ nb_git topy --help
usage: nb_git topy [-h] [-a ALL] [-s SOURCE] [-d DESTINATION] [-n NOISY]

optional arguments:
  -h, --help            show this help message and exit
  -a ALL, --all ALL     topy all notebooks listed with <nblist>
  -s SOURCE, --source SOURCE
                        path to source-file to topy
  -d DESTINATION, --destination DESTINATION
                        (optional) path for output file. will use default path
                        if not provided
  -n NOISY, --noisy NOISY
                        print out files being topy-ed
```

--------------------------------
<a name='wip'></a>
#### Code Status

This is a **WIP**, but seems to be working - albeit missing tests, bells and the whistles.

- [x] IPYNB -> PY converter
- [x] PRECOMMIT HOOK SCRIPT
- [x] PRECOMMIT HOOK INSTALLER
- [x] USER CONFIG
- [x] INSTALLER CLI
- [x] PY -> IPYNB converter
- [ ] tests
- [ ] other/refactoring/cleanup
