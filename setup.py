# import necessary packages
from distutils.core import setup
from distutils.filelist import findall

import os
import py2exe
import sys
import psychopy
import matplotlib
matplotlib.use('wxagg')  # overrule configuration

# this allows to run it with a simple double click.
sys.argv.append('py2exe')

# the name of your .exe file
progName = 'new_bp.py'

# Initialize Holder Files
preference_files = []
app_files = []
matplotlibdatadir = matplotlib.get_data_path()
matplotlibdata = findall(matplotlibdatadir)
matplotlibdata_files = []
for f in matplotlibdata:
    dirname = os.path.join('matplotlibdata', f[len(matplotlibdatadir)+1:])
    matplotlibdata_files.append((os.path.split(dirname)[0], [f]))

# paths
preference_path = os.path.dirname(
    os.path.abspath(psychopy.preferences.__file__))
app_path = os.path.join(os.path.dirname(
    os.path.abspath(psychopy.__file__)), 'app')


# define which files you want to copy for data_files
for filename in os.listdir(preference_path):
    file = os.path.join(preference_path, filename)
    preference_files.append(file)

# if you might need to import the app files
for files in os.listdir(app_path):
    file = os.path.join(app_path, filename)
    app_files.append(file)


# combine the files
# all_files = [("psychopy\\preferences", preference_files), my_data_files[0]]
# all_files = [("psychopy\\preferences", preference_files),("psychopy\\app", app_files), my_data_files[0]]
all_files = [("psychopy\\preferences", preference_files),
             ("psychopy\\app", app_files)] + matplotlibdata_files


py2exe_options = py2exe_options = {
    "compressed": 1,
    "optimize": 2,
    "ascii": 0,
    "bundle_files": 1,
}

# define the setup
setup(
    console=[progName],
    data_files=all_files,
    options={
        "py2exe": py2exe_options
    }
)
