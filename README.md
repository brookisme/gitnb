## NBGIT 

GIT TRACKING FOR PYTHON NOTEBOOKS.

A simple plan: 

* create ipynb->py converter that ignores all the stuff that makes git tracking hard
* use git pre-commit hooks to
    * copy all .ipynb to .py files
    * git add the new .py files to the repo


--------------------------------
#### Code Status
This is a very early stage **WIP**, but seems to be working - albeit missing tests, bells and the whistles.

- [x] IPYNB -> PY converter
- [x] PRECOMMIT HOOK SCRIPT
- [x] PRECOMMIT HOOK INSTALLER
- [ ] INSTALLER CLI
- [ ] PY -> IPYNB converter
- [ ] tests
- [ ] other/refactoring/cleanup

--------------------------------
### INSTALL NBGIT

```bash
git clone https://github.com/brookisme/nbgit.git
cd nbgit
pip install -e .
```


--------------------------------
### Usage

#### INSTALL IN PROJECT

* before installing for your project you must first init the git repo
* this will create or append your `.git/hooks/pre-commit` file so that, upon git commit it will:
    * copy all .ipynb to .py files
    * git add the new .py files to the repo
* CLI coming soon. For now use 

```bash
python -c "import nbgit; nbgit.install()"
```

#### USE:

```bash
# get example nb
cp firstpass.ipynb.example firstpass.ipynb
# get example nb
git add firstpass.ipynb
#
# The default behavior is to save files to a directory called nbpy
# * you can change this with NBPY_DIR
# * the directory will be created if it doesnt exist
# * NBPY_DIR=None will save the file to the directory that the notebook is in
#
git commit -am "this is going to create and add a python file"
```

Your output should look like this:

https://github.com/brookisme/nbgit/blob/master/nbpy/firstpass.nbpy.py
