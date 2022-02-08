# %load https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/nb_functions.py
# update_version: https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/nb_functions.py
from datetime import datetime
from time import strftime
import time
class NBFunctions:
    
    def __init__(self):
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
    
nbf = NBFunctions()