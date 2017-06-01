## GITNB 

**GIT TRACKING FOR PYTHON NOTEBOOKS**

A simple idea: GitNB doesn't actually track python notebooks. Instead, GitNB creates and updates python versions of your notebooks which are in turn tracked by git.

1. [Quick Start](#quick)
2. [But I'm Lazy!!!](#lazy)
3. [Install](#install)
4. [Docs](#docs)
5. [User Config](#config)

_____
<a name='quick'></a>
### QUICK START:

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
[master (root-commit) b29b6c4] ...
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

gitnb[untracked]:
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

# the default directory for the python versions of the notebooks is nbpy/
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

gitnb[tracked]:
  widget/Notebook1.ipynb
  widget/I have spaces in my name.ipynb
  A_BUGGY_NOTEBOOK.ipynb

gitnb[untracked]:
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

# git commit the new nbpy.py versions
test|master $ git commit -am "add nbpy.py versions of notebooks"
[master 868b0a2] ...
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

That notebook is buggy ...[updating python notebook]... I just went to the python-notebook and fixed the bugs. Let's see what happened:

```bash
# note the changes have not appeared in our nbpy.py file
test|master $ git diff

# however, we can see the changes with 'gitnb diff'
test|master $ gitnb diff A_BUGGY_NOTEBOOK.ipynb

gitnb[diff]: A_BUGGY_NOTEBOOK.ipynb[->nbpy.py] - nbpy/A_BUGGY_NOTEBOOK.nbpy.py
--- +++ @@ -1,7 +1,7 @@ 
 
 """[markdown]
-## This is a notebook with bugs
+## This is a notebook without bugs
 """
 
 
@@ -11,7 +11,7 @@ 
 
 """[code]"""
-def feature(food=True):
+def feature(foo=True):
     if foo:
         return "I am not a bug"
     else:


# we now use 'gitnb update' to update the tracked files
# this creates a new nbpy.py version and adds the changes
# to the git repo
test|master $ gitnb update

# now we can see the bug fixes with 'git diff'
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

# commit the changes
test|master $ git commit -am "fixed bug: i fixed .ipynb, gitnb fixed .nbpy.py"
[master 812a4f0] ...
```

E. CREATE PYTHON-NOTEBOOK FROM NBPY.PY FILE

Finally, lets say we actually need that buggy notebook after all

```bash
test|master $ git checkout 868b0a2
Note: checking out '868b0a2'.
[... git detached head messaging ...]
HEAD is now at 868b0a2... add nbpy.py versions of notebooks

# create notebook from nbpy.py file
test|(HEAD detached at 868b0a2) $ gitnb tonb nbpy/A_BUGGY_NOTEBOOK.nbpy.py 

# the default directory for generated notebooks versions is nbpy/
test|(HEAD detached at 868b0a2) $ tree nbpy_nb
nbpy_nb
└── A_BUGGY_NOTEBOOK.nbpy.ipynb

0 directories, 1 file
```

My bugs are back!

![nbpy_nb/A_BUGGY_NOTEBOOK.nbpy.ipynb](https://github.com/brookisme/gitnb/blob/master/buggy.png)

_____
<a name='lazy'></a>
### LAZY CONFIG:

If the [quick-start](#quick) seemed like too much how about this...

```bash
$ gitnb commit -am "I just updated and commited every notebook in my project" 
```

How in the what? Two things are going on here

1. We are [commit](#commit)-ing with `gitnb commit` instead of `git commit`
2. I've [installed](#configure) the user config and set

```bash
# ./gitnb.config.yaml
...
GIT_ADD_ON_GITNB_UPDATE: True
AUTO_TRACK_ALL_NOTEBOOKS: True
...
```

Now each time I `gitnb commit`:

* All new notebooks are [add](#add)ed to be tracked by gitnb
* All notebooks are [update](#update)ed
* All changes are added to the git repo
* `git commit --allow-empty` is [called](#commit)

Note: the `--allow-empty` flag is there because the at the time of the commit (before the nbpy.py files are generated there may or may not be changes to commit)

Here's the super-quick-quick-start-example
```bash
test|master $ git init
Initialized empty Git repository in /Users/brook/code/jupyter/gitnb/test/.git/
test| $ gitnb init

gitnb: INSTALLED 
   - nbpy.py files will be created/updated/tracked
   - install user config with: $ gitnb configure
   
test| $ gitnb configure
gitnb: USER CONFIG FILE ADDED (./gitnb.config.yaml) 
```

... go update user config...

```bash
test| $ gitnb commit -am "Initial Commit with everything"
gitnb: add (A-Notebook.ipynb | nbpy/A-Notebook.nbpy.py)
gitnb: add (A_BUGGY_NOTEBOOK.ipynb | nbpy/A_BUGGY_NOTEBOOK.nbpy.py)
gitnb: add (Py2NB.ipynb | nbpy/Py2NB.nbpy.py)
gitnb: add (widget/I have spaces in my name.ipynb | nbpy/I have spaces in my name.nbpy.py)
gitnb: add (widget/Notebook1.ipynb | nbpy/Notebook1.nbpy.py)
[master (root-commit) cb8c106] ...

test|master $ tree
.
├── A-Notebook.ipynb
├── A_BUGGY_NOTEBOOK.ipynb
├── Py2NB.ipynb
├── another_python_file.py
├── gitnb.config.yaml
├── nbpy
│   ├── A-Notebook.nbpy.py
│   ├── A_BUGGY_NOTEBOOK.nbpy.py
│   ├── I\ have\ spaces\ in\ my\ name.nbpy.py
│   ├── Notebook1.nbpy.py
│   └── Py2NB.nbpy.py
├── some_python_file.py
└── widget
    ├── I\ have\ spaces\ in\ my\ name.ipynb
    ├── Notebook1.ipynb
    └── widget.py

2 directories, 14 files
```
_____
<a name='install'></a>
### INSTALL:

###### pip:
```bash
pip install gitnb
```

###### github:
```
git clone https://github.com/brookisme/gitnb.git
cd gitnb
sudo pip install -e .
```

_____
<a name='docs'></a>
### DOCS:

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
8. [commit](#commit): update, followed by add, followed by `git commit`
9. [diff](#diff): perform diff between current notebook version and last [update](#update)-ed version
10. [topy](#topy): convert notebook to nbpy.py file (without [add](#add)-ing)
11. [tonb](#tonb): convert nbpy.py file to python notebook

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

Appends (or creates) gitignore with the recommended settings. Namely,

* notebooks: *.ipynb, .ipynb_checkpoints
* gitnb: .gitnb/, nbpy_nb/

```bash
$ gitnb gitignore
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
###### add:
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
<a name='commit'></a>
###### commit:
Update and Commit:

* if (UPDATE_ON_GITNB_COMMIT) perform 'gitnb update'
* call `git commit --allow-empty` with optional flags [a|m]:
  - -a flag (add all - same as git commit -a)
  - -m flag (add all - same as git commit -m)

```bash
$ gitnb commit [-a] [-m "COMMIT MESSAGE"]
```
([back to methods](#methods))

_____
<a name='diff'></a>
###### diff:
Diff for recent changes.

Creates a diff between the most recent nbpy.py version of the noteboook
and the nbpy.py version of the notebook in its current state (the working copy).

```bash
$ gitnb diff <PATH-TO-NOTEBOOK(.ipynb)-FILE>
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
### USER CONFIG:

The [configure](#configure) method installs `gitnb.config.yaml` in your root directory.  This is a copy of the [default config](https://github.com/brookisme/gitnb/blob/master/gitnb/default.config.yaml). Note at anytime you can go back to the default configuration by simply deleting the user config file (`gitnb.config.yaml`).

There are comment-docs in the config file that should explain what each configuration control. However I thought I'd touch a couple of the perhaps more interesting configurations here.

##### LAZY INSTALL

see [But I'm Lazy!](#lazy)

##### GIT_ADD_ON_GITNB_ADD (defaults to True):

If True the [add](#add) method will perform a `git add` after creating the nbpy file and adding it to the gitnb tracking list.  You can set this to False if you want to explicity call `git add` yourself after looking over the file.

##### UPDATE_ON_COMMIT (defaults to True):

If True, the gitnb [update](#update) method will automatically be called when performing a `git commit` (during pre-commit hook).

##### AUTO_TRACK_ALL_NOTEBOOKS (defaults to False):

If True, `gitnb add .` (see [add](#add) method) will automatically be called when performing a `git commit` (during pre-commit hook). This will add all notebooks in your project to gitnb.

_Note if the only thing that has changed is your notebooks, you'll still need to explicity call `gitnb update` or add the `--allow-empty` flag to your `git commit`._

##### EXCLUDE_DIRS:

A list of directories not to include when searching for notebooks

##### OTHER:

You can also configure, default location for new files, if they include an indentifier (like 'nbpy' in `somefile.nbpy.py`), spacing in nbpy files and more. Check the comment-docs for more info.


