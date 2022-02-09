# source: https://github.com/fscheidt/dev/blob/master/jupyter/nb_functions.py
from datetime import datetime
from time import strftime
from time import gmtime
import time

"""
Load this file into a notebook:
%load https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/nb_functions.py
"""

class RuntimeLogger:

    
    def __init__(self, v=False):
        self.begin = None
        self.end = None
        self.start_time = time.time()
        self.start = f"[start]: {datetime.now().strftime('%Y/%m/%d - %H:%M:%S')}"
        self.v = v
        if v:
            print('[start_time]:', datetime.now().strftime('%Y/%m/%d - %H:%M:%S'))

    def begin_time(self):
        self.begin = time.time()
        print('begin_time:', datetime.now().strftime('%Y/%m/%d - %H:%M:%S'))

    def end_time(self):
        self.end = time.time()
        print('end_time:', datetime.now().strftime('%Y/%m/%d - %H:%M:%S'))
        ellapse_time = self.end - self.begin
        print('Total timing:', end='')
        print(f'\t[{strftime("%H:%M:%S", gmtime(ellapse_time))}]')
        return ellapse_time

    @staticmethod
    def runtime(duration):
        print(f'Total run_time: {strftime("%H:%M:%S", gmtime(duration))}')

class NBFunctions:
    
    log = RuntimeLogger(v=True)
    
    def __init__(self, v=True):
        self.v = v
        self.load_time = time.time()
        print(f"[load_time]: {datetime.now().strftime('%Y/%m/%d - %H:%M:%S')}")
    
    @staticmethod
    def restart():
        from IPython.core.display import HTML
        print(f"[restarted]: {datetime.now().strftime('%Y/%m/%d - %H:%M:%S')}")
        return HTML("<script>Jupyter.notebook.kernel.restart()</script>")
    
    @staticmethod
    def kill():
        import IPython
        IPython.Application.instance().kernel.do_shutdown(True)
    
nb = NBFunctions()
