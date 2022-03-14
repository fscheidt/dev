# brief context setup
import os
"""
Load into notebook:
%load https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/nb_context_min.py
"""

DIR_PATH = os.getenv('GTB_DEV')
%cd $DIR_PATH
!conda info | grep 'active envir'

from IPython.lib.deepreload import reload
%load_ext autoreload
%autoreload 2

import numpy as np
import pandas as pd

