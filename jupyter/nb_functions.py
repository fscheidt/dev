# update_version: https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/nb_functions.py
class NBFunctions:
    
    def __init__():
        pass
    
    @staticmethod
    def restart():
        from IPython.core.display import HTML
        return HTML("<script>Jupyter.notebook.kernel.restart()</script>")
    
    @staticmethod
    def kill():
        import IPython
        IPython.Application.instance().kernel.do_shutdown(True)
    
nbf = NBFunctions
