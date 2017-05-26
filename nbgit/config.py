import os
import yaml
import nbgit


#
# LOAD USER CONFIG
#
if os.path.isfile(nbgit.USER_CONFIG_PATH):
    user_config=yaml.safe_load(open(nbgit.USER_CONFIG_PATH))
else:
    user_config={}


#
# LOAD DEFAULT CONFIG
#
default_config=yaml.safe_load(open(nbgit.DEFAULT_CONFIG_PATH))


""" fig (as in con.fig)
    get property from user_config (if it exists) 
    otherwise use default_config
"""
def fig(prop)
    return user_config.get(
        prop,
        default_config.get(prop))