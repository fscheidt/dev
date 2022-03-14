# set context and import common dependencies
from IPython.display import display_javascript, display_html, display, HTML
import os
from datetime import datetime
from time import strftime
DIR_PATH = os.getenv('GTB_DEV')
%cd $DIR_PATH
!conda info | grep 'active envir'

print(f"[load_time]: {datetime.now().strftime('%Y/%m/%d - %H:%M:%S')}")

from IPython.lib.deepreload import reload
%load_ext autoreload
%autoreload 2

import numpy as np
import pandas as pd