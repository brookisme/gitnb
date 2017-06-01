## NBGIT 

**GIT TRACKING FOR PYTHON NOTEBOOKS**

1. [Quick Start](#quick)
2. [Install](#install)
3. [Docs](#docs)
4. [User Config](#config)

NBGIT doesn't actually track python notebooks. Instead, NGIT creates and updates python versions of your notebooks which are in turn tracked by git.

_____
<a name='quick'></a>
#### QUICK START:

This quick-start is just an example. It looks long (due to bash-output) but its quick: 1-2 minutes tops.

A. INITIALIZE GIT REPO

```bash
test| $ tree
.
├── A-Notebook.ipynb
├── A_BUGGY_NOTEBOOK.ipynb
├── Py2NB.ipynb
├── another_python_file.py
├── some_python_file.py
└── widget
    ├── I\ have\ spaces\ in\ my\ name.ipynb
    ├── Notebook1.ipynb
    └── widget.py

1 directory, 8 files

test| $ git init
Initialized empty Git repository in /Users/brook/code/jupyter/nbgit/test/.git/

test| $ git add .

test| $ git commit -am "Initial Commit: python files"
[master (root-commit) b29b6c4] Initial Commit: python files
 4 files changed, 10 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 another_python_file.py
 create mode 100644 some_python_file.py
 create mode 100644 widget/widget.py
```


B. INITIALIZE NB_GIT, ADD NOTEBOOKS TO NB_GIT TO BE TRACKED

```bash

# initialize nb_git
test|master $ nb_git init

nb_git: INSTALLED 
   - nbpy.py files will be created/updated/tracked
   - install user config with: $ nb_git configure

# lets list our (untracked) notebooks
test|master $ nb_git list
nb_git[untracked]
  Py2NB.ipynb
  A-Notebook.ipynb
  widget/I have spaces in my name.ipynb
  A_BUGGY_NOTEBOOK.ipynb
  widget/Notebook1.ipynb

# adding an individual file
test|master $ nb_git add A_BUGGY_NOTEBOOK.ipynb 
nbgit: add (A_BUGGY_NOTEBOOK.ipynb | nbpy/A_BUGGY_NOTEBOOK.nbpy.py)

# adding all the files in a directory
test|master $ nb_git add widget
nbgit: add (widget/I have spaces in my name.ipynb | nbpy/I have spaces in my name.nbpy.py)
nbgit: add (widget/Notebook1.ipynb | nbpy/Notebook1.nbpy.py)

# you can see we now have python versions of these notebooks
test|master $ tree
.
├── A-Notebook.ipynb
├── A_BUGGY_NOTEBOOK.ipynb
├── Py2NB.ipynb
├── another_python_file.py
├── nbpy
│   ├── A_BUGGY_NOTEBOOK.nbpy.py
│   ├── I\ have\ spaces\ in\ my\ name.nbpy.py
│   └── Notebook1.nbpy.py
├── some_python_file.py
└── widget
    ├── I\ have\ spaces\ in\ my\ name.ipynb
    ├── Notebook1.ipynb
    └── widget.py

2 directories, 11 files

# our list now conatins tracked and untracked notebooks
test|master $ nb_git list
nb_git[tracked]
  widget/Notebook1.ipynb
  widget/I have spaces in my name.ipynb
  A_BUGGY_NOTEBOOK.ipynb
nb_git[untracked]
  A-Notebook.ipynb
  Py2NB.ipynb

# note these files are now in our git repo
test|master $ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

  new file:   nbpy/A_BUGGY_NOTEBOOK.nbpy.py
  new file:   nbpy/I have spaces in my name.nbpy.py
  new file:   nbpy/Notebook1.nbpy.py

# lets commit them
test|master $ git commit -am "add nbpy.py versions of notebooks"
[master 868b0a2] add nbpy.py versions of notebooks
 3 files changed, 98 insertions(+)
 create mode 100644 nbpy/A_BUGGY_NOTEBOOK.nbpy.py
 create mode 100644 nbpy/I have spaces in my name.nbpy.py
 create mode 100644 nbpy/Notebook1.nbpy.py
```


C. QUICK LOOK AT A "NBPY.PY" VERSION OF A NOTEBOOK


```bash
test|master $ cat nbpy/A_BUGGY_NOTEBOOK.nbpy.py 


"""[markdown]
## This is a notebook with bugs
"""


"""[code]"""
import numpy as np
""""""


"""[code]"""
def feature(food=True):
    if foo:
        return "I am not a bug"
    else:
        return "I told you I am not a bug"
""""""


"""[code]"""
print("Are you a bug?")
print(feature(True))
""""""

```

D. UPDATE NBPY.PY FILE AFTER EDITING YOUR NOTEBOOK

That notebook is buggy. ...<updating python notebook>... I just went to the python-notebook and fixed the bugs. Let's see what happened:

```bash
# note the changes have not appeared in our nbpy.py file
test|master $ git diff

# `nb_git update` updates your tracked files
test|master $ nb_git update

# now we can see the bug fixes
test|master $ git diff
diff --git a/nbpy/A_BUGGY_NOTEBOOK.nbpy.py b/nbpy/A_BUGGY_NOTEBOOK.nbpy.py
index e80204b..955b359 100644
--- a/nbpy/A_BUGGY_NOTEBOOK.nbpy.py
+++ b/nbpy/A_BUGGY_NOTEBOOK.nbpy.py
@@ -1,7 +1,7 @@
 
 
 """[markdown]
-## This is a notebook with bugs
+## This is a notebook without bugs
 """
 
 
@@ -11,7 +11,7 @@ import numpy as np
 
 
 """[code]"""
-def feature(food=True):
+def feature(foo=True):
     if foo:
         return "I am not a bug"
     else:

# lets fix that too!
test|master $ git commit -am "fixed bug: i fixed .ipynb, nb_git fixed .nbpy.py"
[master 812a4f0] fixed bug: i fixed .ipynb, nb_git fixed .nbpy.py
 1 file changed, 2 insertions(+), 2 deletions(-)

```

E. CREATE PYTHON-NOTEBOOK FROM NBPY.PY FILE

Finally, lets say we actually need that buggy notebook after all

```bash
test|master $ git checkout 868b0a2
Note: checking out '868b0a2'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at 868b0a2... add nbpy.py versions of notebooks
test|(HEAD detached at 868b0a2) $ nb_git tonb nbpy/A_BUGGY_NOTEBOOK.nbpy.py 
test|(HEAD detached at 868b0a2) $ tree nbpy_nb
nbpy_nb
└── A_BUGGY_NOTEBOOK.nbpy.ipynb

0 directories, 1 file
```

My bugs are back!

![nbpy_nb/A_BUGGY_NOTEBOOK.nbpy.ipynb](https://github.com/brookisme/nb_git/blob/master/buggy.png)

_____
<a name='install'></a>
#### INSTALL:

```bash
# pip
pip install nb_git

# or github
git clone https://github.com/brookisme/nb_git.git
cd nb_git
sudo pip install -e .
```

_____
<a name='docs'></a>
#### DOCS:

```bash
$ nb_git --help
usage: nb_git [-h] {init,configure,list,update,add,remove,topy,tonb} ...
```

<a name='methods'></a>
###### methods:

1. [init](#init): initialize nb_git for project
2. [configure](#configure): install nb_git.config.yaml for user config
3. [gitignore](#gitignore): add ipynb \& nb_git files to gitignore
4. [list](#list): list tracked notebooks or nbpy.py files
5. [add](#add): begin tracking notebook
6. [remove](#remove): stop tracking notebook
7. [update](#update): update nbpy.py files with recent notebook edits
8. [diff](#diff): perform diff between current notebook version and last [update](#update)-ed version
9. [topy](#topy): convert notebook to nbpy.py file (without [add](#add)-ing)
10. [tonb](#tonb): convert nbpy.py file to python notebook

_____
<a name='init'></a>

###### init:
Initialize Project:

* `git init` required before `nb_git init`
* installs .nb_git directory at the project root
* creates or appends .git/hooks/pre-commit for auto-tracking config

```bash
$ nb_git init
```
([back to methods](#methods))

_____
<a name='configure'></a>
###### configure:
Install Config:

* optional: only necesary if you want to change the [default config](https://github.com/brookisme/nb_git/blob/master/nb_git/default.config.yaml)
* installs nb_git.config.yaml directory at the project root

```bash
$ nb_git configure
```
([back to methods](#methods))

_____
<a name='gitignore'></a>
###### gitignore:
Update .gitignore:

```bash
TODO: append *.ipynb, .ipynb_checkpoints, nbpy/, nbpy_nb/ into gitignore
```
([back to methods](#methods))

_____
<a name='list'></a>
###### list:
List Project Notebooks, or nbpy.py files

positional arg (*type*):

* (default) **all**: list tracked and untracked notebooks
* **tracked**: list tracked notebooks
* **untracked**: list untracked notebooks
* **nbpy**: list nbpy.py files

```bash
$ nb_git list --help
usage: nb_git list [-h] [type]

positional arguments:
  type        notebooks: ( all | tracked | untracked ), or nbpy
```
([back to methods](#methods))

_____
<a name='add'></a>
Add notebook to nb_git:

* converts notebook(s) to nbpy.py file(s)
* adds notebook-nbpy pair to nb_git tracking list
* performs a `git add` on nbpy.py file(s)
* path: path to file or directory 
* destination_path: (optional) 
    * if path is a file path nbpy file will be at destination_path
    * if destination_path is falsey (recommended) default path is used
    * default path can be changed with [user config](#config)
    * if path is a direcotry path, default config is always used

###### add:
```bash
$ nb_git add --help
usage: nb_git add [-h] path [destination_path]

positional arguments:
  path              path to ipynb file
  destination_path  if falsey uses default destination path
```
([back to methods](#methods))

_____
<a name='remove'></a>
###### remove:
Remove notebook from nb_git:

* notebook will no longer be tracked
* nbpy.py file will **not** be deleted
* ipynb file will **not** be deleted

```bash
$ nb_git remove --help
usage: nb_git remove [-h] path

positional arguments:
  path        path to ipynb file
```
([back to methods](#methods))

_____
<a name='update'></a>
###### update:
Update nbpy files:

* will update nbpy files with current content from your tracked notebooks
* make sure your notebook has been saved!

```bash
$ nb_git update
```
([back to methods](#methods))

_____
<a name='diff'></a>
###### diff:
```bash
TODO: DIFF CURRENT AND LAST
```
([back to methods](#methods))

_____
<a name='topy'></a>
###### topy:
To-Python:

* converts notebook(s) to nbpy.py file(s)
* similar to [add](#add) but does not nb_git or git track

```bash
$ nb_git topy --help
usage: nb_git topy [-h] path [destination_path]

positional arguments:
  path              path to ipynb file
  destination_path  if falsey uses default destination path
```
([back to methods](#methods))

_____
<a name='tonb'></a>
###### tonb:
To-Notebook:

* creates new notebook from nbpy.py python file
* great for collaborators!
* great for recovering lost work!

```bash
$ nb_git tonb --help
usage: nb_git tonb [-h] path [destination_path]

positional arguments:
  path              path to ipynb file
  destination_path  if falsey uses default destination path
```
([back to methods](#methods))


_____
<a name='config'></a>
#### USER CONFIG:

The [configure](#configure) method installs `nb_git.config.yaml` in your root directory.  This is a copy of the [default config](https://github.com/brookisme/nb_git/blob/master/nb_git/default.config.yaml). Note at anytime you can go back to the default configuration by simply deleting the user config file (`nb_git.config.yaml`).

There are comment-docs in the config file that should explain what each configuration control.  However I thought I'd touch a couple of the perhaps more interesting configurations here.

##### GIT_ADD_ON_NB_GIT_ADD (defaults to True):

If True the [add](#add) method will perform a `git add` after creating the nbpy file and adding it to the nb_git tracking list.  You can set this to False if you want to explicity call `git add` yourself after looking over the file.

##### UPDATE_ON_COMMIT (defaults to True):

If True, the ng_git [update](#update) method will automatically be called when performing a `git commit` (during pre-commit hook).

##### AUTO_TRACK_ALL_NOTEBOOKS (defaults to False):

If True, `nb_git add .` (see [add](#add) method) will automatically be called when performing a `git commit` (during pre-commit hook). This will add all notebooks in your project to nb_git.

_Note if the only thing that has changed is your notebooks, you'll still need to explicity call `nb_git update` or add the `--allow-empty` flag to your `git commit`._

##### EXCLUDE_DIRS:

A list of directories not to include when searching for notebooks

##### OTHER:

You can also configure, default location for new files, if they include an indentifier (like 'nbpy' in `somefile.nbpy.py`), spacing in nbpy files and more. Check the comment-docs for more info.


