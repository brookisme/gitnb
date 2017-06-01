## NBGIT 

**GIT TRACKING FOR PYTHON NOTEBOOKS**

NBGIT doesn't actually track python notebooks. Instead, NGIT creates and updates python versions of your notebooks which are in turn tracked by git.

Lets start with an example:

First we initialize a git repo containing python notebooks (we have (git)ignored `\*.ipynb`, `.ipynb_checkpoints`):

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


Now we set up NBGIT

1. initialize nb_git
2. list existing notebooks
3. add the notebooks we want to track

```bash
test|master $ nb_git init

nb_git: INSTALLED 
   - nbpy.py files will be created/updated/tracked
   - install user config with: $ nb_git configure

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


Oh No! One of our notebooks is buggy.  Let's look at the `nbpy.py` version of the notebook

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


I just went to the python-notebook and fixed the bugs

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
test|master $ git commit -am "fixed bug: nb-git-update command copied the bug fixes from the ipynb file to the nbpy.py verison of the notebook"
[master 812a4f0] fixed bug: nb-git-update command copied the bug fixes from the ipynb file to the nbpy.py verison of the notebook
 1 file changed, 2 insertions(+), 2 deletions(-)

```

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


