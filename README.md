## GITNB 

**GIT TRACKING FOR PYTHON NOTEBOOKS**

1. [Quick Start](#quick)
2. [Install](#install)
3. [Docs](#docs)
4. [User Config](#config)

GITNB doesn't actually track python notebooks. Instead, NGIT creates and updates python versions of your notebooks which are in turn tracked by git.

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
Initialized empty Git repository in /Users/brook/code/jupyter/gitnb/test/.git/

test| $ git add .

test| $ git commit -am "Initial Commit: python files"
[master (root-commit) b29b6c4] Initial Commit: python files
 4 files changed, 10 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 another_python_file.py
 create mode 100644 some_python_file.py
 create mode 100644 widget/widget.py
```


B. INITIALIZE GitNB, ADD NOTEBOOKS TO GitNB TO BE TRACKED

```bash

# initialize gitnb
test|master $ gitnb init

gitnb: INSTALLED 
   - nbpy.py files will be created/updated/tracked
   - install user config with: $ gitnb configure

# lets list our (untracked) notebooks
test|master $ gitnb list
gitnb[untracked]
  Py2NB.ipynb
  A-Notebook.ipynb
  widget/I have spaces in my name.ipynb
  A_BUGGY_NOTEBOOK.ipynb
  widget/Notebook1.ipynb

# adding an individual file
test|master $ gitnb add A_BUGGY_NOTEBOOK.ipynb 
gitnb: add (A_BUGGY_NOTEBOOK.ipynb | nbpy/A_BUGGY_NOTEBOOK.nbpy.py)

# adding all the files in a directory
test|master $ gitnb add widget
gitnb: add (widget/I have spaces in my name.ipynb | nbpy/I have spaces in my name.nbpy.py)
gitnb: add (widget/Notebook1.ipynb | nbpy/Notebook1.nbpy.py)

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
test|master $ gitnb list
gitnb[tracked]
  widget/Notebook1.ipynb
  widget/I have spaces in my name.ipynb
  A_BUGGY_NOTEBOOK.ipynb
gitnb[untracked]
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

That notebook is buggy. ...[updating python notebook]... I just went to the python-notebook and fixed the bugs. Let's see what happened:

```bash
# note the changes have not appeared in our nbpy.py file
test|master $ git diff

# `gitnb update` updates your tracked files
test|master $ gitnb update

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
test|master $ git commit -am "fixed bug: i fixed .ipynb, gitnb fixed .nbpy.py"
[master 812a4f0] fixed bug: i fixed .ipynb, gitnb fixed .nbpy.py
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
test|(HEAD detached at 868b0a2) $ gitnb tonb nbpy/A_BUGGY_NOTEBOOK.nbpy.py 
test|(HEAD detached at 868b0a2) $ tree nbpy_nb
nbpy_nb
└── A_BUGGY_NOTEBOOK.nbpy.ipynb

0 directories, 1 file
```

My bugs are back!

![nbpy_nb/A_BUGGY_NOTEBOOK.nbpy.ipynb](https://github.com/brookisme/gitnb/blob/master/buggy.png)

_____
<a name='install'></a>
#### INSTALL:

_pip_
```bash
pip install gitnb
```

_github_
```
git clone https://github.com/brookisme/gitnb.git
cd gitnb
sudo pip install -e .
```

_____
<a name='docs'></a>
#### DOCS:

```bash
$ gitnb --help
usage: gitnb [-h] {init,configure,list,update,add,remove,topy,tonb} ...
```

<a name='methods'></a>
###### methods:

1. [init](#init): initialize gitnb for project
2. [configure](#configure): install gitnb.config.yaml for user config
3. [gitignore](#gitignore): add ipynb \& gitnb files to gitignore
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

* `git init` required before `gitnb init`
* installs .gitnb directory at the project root
* creates or appends .git/hooks/pre-commit for auto-tracking config

```bash
$ gitnb init
```
([back to methods](#methods))

_____
<a name='configure'></a>
###### configure:
Install Config:

* optional: only necesary if you want to change the [default config](https://github.com/brookisme/gitnb/blob/master/gitnb/default.config.yaml)
* installs gitnb.config.yaml directory at the project root

```bash
$ gitnb configure
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
$ gitnb list --help
usage: gitnb list [-h] [type]

positional arguments:
  type        notebooks: ( all | tracked | untracked ), or nbpy
```
([back to methods](#methods))

_____
<a name='add'></a>
Add notebook to gitnb:

* converts notebook(s) to nbpy.py file(s)
* adds notebook-nbpy pair to gitnb tracking list
* performs a `git add` on nbpy.py file(s)
* path: path to file or directory 
* destination_path: (optional) 
    * if path is a file path nbpy file will be at destination_path
    * if destination_path is falsey (recommended) default path is used
    * default path can be changed with [user config](#config)
    * if path is a direcotry path, default config is always used

###### add:
```bash
$ gitnb add --help
usage: gitnb add [-h] path [destination_path]

positional arguments:
  path              path to ipynb file
  destination_path  if falsey uses default destination path
```
([back to methods](#methods))

_____
<a name='remove'></a>
###### remove:
Remove notebook from gitnb:

* notebook will no longer be tracked
* nbpy.py file will **not** be deleted
* ipynb file will **not** be deleted

```bash
$ gitnb remove --help
usage: gitnb remove [-h] path

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
$ gitnb update
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
* similar to [add](#add) but does not gitnb or git track

```bash
$ gitnb topy --help
usage: gitnb topy [-h] path [destination_path]

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
$ gitnb tonb --help
usage: gitnb tonb [-h] path [destination_path]

positional arguments:
  path              path to ipynb file
  destination_path  if falsey uses default destination path
```
([back to methods](#methods))


_____
<a name='config'></a>
#### USER CONFIG:

The [configure](#configure) method installs `gitnb.config.yaml` in your root directory.  This is a copy of the [default config](https://github.com/brookisme/gitnb/blob/master/gitnb/default.config.yaml). Note at anytime you can go back to the default configuration by simply deleting the user config file (`gitnb.config.yaml`).

There are comment-docs in the config file that should explain what each configuration control.  However I thought I'd touch a couple of the perhaps more interesting configurations here.

##### GIT_ADD_ON_GitNB_ADD (defaults to True):

If True the [add](#add) method will perform a `git add` after creating the nbpy file and adding it to the gitnb tracking list.  You can set this to False if you want to explicity call `git add` yourself after looking over the file.

##### UPDATE_ON_COMMIT (defaults to True):

If True, the ng_git [update](#update) method will automatically be called when performing a `git commit` (during pre-commit hook).

##### AUTO_TRACK_ALL_NOTEBOOKS (defaults to False):

If True, `gitnb add .` (see [add](#add) method) will automatically be called when performing a `git commit` (during pre-commit hook). This will add all notebooks in your project to gitnb.

_Note if the only thing that has changed is your notebooks, you'll still need to explicity call `gitnb update` or add the `--allow-empty` flag to your `git commit`._

##### EXCLUDE_DIRS:

A list of directories not to include when searching for notebooks

##### OTHER:

You can also configure, default location for new files, if they include an indentifier (like 'nbpy' in `somefile.nbpy.py`), spacing in nbpy files and more. Check the comment-docs for more info.


