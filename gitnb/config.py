import os
import yaml
import gitnb.paths as paths

#
# LOAD USER CONFIG
#
if os.path.isfile(paths.USER_CONFIG):
    user_config=yaml.safe_load(open(paths.USER_CONFIG))
else:
    user_config={}


#
# LOAD DEFAULT CONFIG
#
default_config=yaml.safe_load(open(paths.DEFAULT_CONFIG))


""" fig (as in con.fig)
    get property from user_config (if it exists) 
    otherwise use default_config
"""
def fig(prop):
    return user_config.get(
        prop,
        default_config.get(prop))