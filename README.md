## NBGIT 

GIT TRACKING FOR PYTHON NOTEBOOKS.

A simple plan: 

* create ipynb->py converter that ignores all the stuff that makes git tracking hard
* use git pre-commit hooks to
    * copy all .ipynb to .py files
    * git add the new .py files to the repo

###### USAGE:

```bash
# in some project containing some ipython-notebooks
git commit -am "this is going to create/update a python file(s) and add it(them) to your repo"
```

Thats it! A git commit will:

* create or update a python file that you can track with git
* call `git add` on the new python file (you can turn this off by setting AUTO_ADD_NBPY=False)

Here is an example output file:

https://github.com/brookisme/nbgit/blob/master/NBGit%20Example%20Notebook.nbpy.py

File Location/Naming/Layout/Ect... is configurable with the user config file, and there is a CLI for performing these operations outside of the git commit.

--------------------------------
#### Code Status
This is early stage **WIP**, but seems to be working - albeit missing tests, bells and the whistles.

- [x] IPYNB -> PY converter
- [x] PRECOMMIT HOOK SCRIPT
- [x] PRECOMMIT HOOK INSTALLER
- [x] USER CONFIG
- [x] INSTALLER CLI
- [ ] PY -> IPYNB converter
- [ ] tests
- [ ] other/refactoring/cleanup

--------------------------------
### INSTALL NBGIT

```bash
git clone https://github.com/brookisme/nbgit.git
cd nbgit
#
# You may need sudo here. I'll push to PYPI once this is more stable
#
pip install -e .
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
nbgit install
```

* ( optional - only if you want to change the [defaults](https://github.com/brookisme/nbgit/blob/master/nbgit/default.config.yaml) ): install user config file (nbgit.config.yaml).  See doc-comments in [defaults](https://github.com/brookisme/nbgit/blob/master/nbgit/default.config.yaml) file to edit.

```bash
nbgit configure
```

--------------------------------
### OTHER CLI COMMANDS:

In addition to the commands above, the CLI provides `nblist` and `convert` which do what you think they do.  Here are the docs:

```bash
nbgit-repo|master $ nbgit --help
usage: nbgit [-h] {install,configure,nblist,convert} ...

NBGIT: TRACKING FOR PYTHON NOTEBOOKS

positional arguments:
  {install,configure,nblist,convert}
    install             installs nbgit into local project (writes to
                        .git/hooks/pre-commit
    configure           creates local configuration file (./nbgit_config.py)
    nblist              list all noteboks (that are not in EXCLUDE_DIRS)
    convert             convert .ipynb files to .nbpy.py files

optional arguments:
  -h, --help            show this help message and exit
```

```bash
nbgit-repo|master $ nbgit convert --help
usage: nbgit convert [-h] [-a ALL] [-f FILE] [-n NOISY]

optional arguments:
  -h, --help            show this help message and exit
  -a ALL, --all ALL     convert all notebooks listed with <nblist>
  -f FILE, --file FILE  path to file to convert
  -n NOISY, --noisy NOISY
                        print out files being converted
```

