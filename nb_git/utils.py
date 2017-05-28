import os
import subprocess
import fnmatch

def rglob(match='*',root='.',exclude_dirs=[]):
    """ Recursive Glob
        Args:
            match: <str> string to match
            root: <str> dir to start recursive search
            exclude: <list[str]> list of directories to skip
    """
    matches = []
    for froot, _, filenames in os.walk(root):
        if not any(xdir in froot for xdir in exclude_dirs):
            for filename in fnmatch.filter(filenames, match):
                matches.append(os.path.join(froot, filename))
    return matches


def copy_append(input_path,output_path,open_type=None):
    """ COPY OR APPEND input_path to output_path
    """
    if not open_type:
        if os.path.isfile(output_path): open_type='a'
        else: open_type='w'
    with open(output_path,open_type) as output_file:
        with open(input_path,'r') as input_file:
            output_file.write(input_file.read())


def git_add(path):
    """ GIT ADD FILE
    """
    safe_path="'{}'".format(path)
    cmd=' '.join(['git add',safe_path])
    subprocess.check_output(cmd, shell=True)


def truthy(value):
    """ Stringy Truthyness
    """
    value=str(value).lower().strip(' ')
    if value in ['none','false','0','nope','','[]']:
        return False
    else:
        return True


def mkdirs(path):
    """ Make parent dirs if they dont exist
    """
    if not os.path.exists(os.path.dirname(path)):
        nb_dir=os.path.dirname(path)
        if truthy(nb_dir):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise



