# update_version: https://github.com/fscheidt/dev/blob/master/jupyter/nb_functions.py
class NBFunctions:
    
    def __init__():
        pass
    
    @staticmethod
    def restart():
        from IPython.core.display import HTML
        return HTML("<script>Jupyter.notebook.kernel.restart()</script>")
    
nbf = NBFunctions
