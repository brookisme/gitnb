

"""[markdown]
## This is an example notebook

The main purpose of this notebook is to have something to convert with gitnb.  There is nothing interesting to see here. In order to make this point perfectly clear, I will start with some difficult math...
"""


"""[code]"""
1+1
""""""


"""[markdown]
-----------------------
_some more code blocks..._
"""


"""[code]"""
import numpy as np
""""""


"""[code]"""
eps=1e-10
""""""


"""[code]"""
def precision(v,p):
    v=np.array(v)
    p=np.array(p)
    tpa=[pred*int(eq) for (pred,eq) in zip(p,np.equal(v,p))]
    fpa=[pred*int(not eq) for (pred,eq) in zip(p,np.equal(v,p))]
    tp=sum(tpa)
    fp=sum(fpa)
    return tp/(fp+tp+eps)
""""""


"""[code]"""
def recall(v,p):
    v=np.array(v)
    p=np.array(p)
    tpa=[pred*int(eq) for (pred,eq) in zip(p,np.equal(v,p))]
    fna=[(1-pred)*int(not eq) for (pred,eq) in zip(p,np.equal(v,p))]
    tp=sum(tpa)
    fn=sum(fna)
    return tp/(fn+tp+eps)
""""""


"""[code]"""
def f2(a,b):
    pc=precision(a,b)
    rc=recall(a,b)
    return 5 * pc * rc / ((4*pc) + rc + eps)
""""""


"""[code]"""
a=[1,1,0,1,1]
b=[1,1,1,0,0]
f2(a,b)
""""""


"""[markdown]
## Here is a Raw NB Convert block
"""


"""[raw]
gitnb-repo|master $ gitnb --help
usage: gitnb [-h] {install,configure,nblist,convert} ...

GITNB: TRACKING FOR PYTHON NOTEBOOKS

positional arguments:
  {install,configure,nblist,convert}
    install             installs gitnb into local project (writes to
                        .git/hooks/pre-commit
    configure           creates local configuration file (./gitnb_config.py)
    nblist              list all noteboks (that are not in EXCLUDE_DIRS
    convert             convert .ipynb files to .nbpy.py files

optional arguments:
  -h, --help            show this help message and exit
"""


"""[code]"""
2+2
""""""


