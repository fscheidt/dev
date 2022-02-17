from datetime import datetime
from time import strftime
from time import gmtime
import time
import uuid
from IPython.display import display_javascript, display_html, display, HTML
import json
import ipykernel
import requests
from requests.compat import urljoin
from notebook.notebookapp import list_running_servers
import os
import re
"""
%load https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/nb_util_context.py
"""
PROJECT = 'diffbert'
JS_FILE = "https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/renderjson.js"

class RuntimeLogger:
    def __init__(self, v=False):
        self.begin = None
        self.end = None
        self.start_time = time.time()
        self.start = f"[init_log]: {datetime.now().strftime('%Y/%m/%d - %H:%M:%S')}"
        self.v = v
        if self.v: print(self.start)
    def begin_time(self):
        self.begin = time.time()
        print('begin_time:', datetime.now().strftime('%Y/%m/%d - %H:%M:%S'))
    def end_time(self):
        self.end = time.time()
        print('end_time:', datetime.now().strftime('%Y/%m/%d - %H:%M:%S'))
        ellapse_time = self.end - self.begin
        print('Total timing: ', end='')
        print(f'\t[{strftime("%H:%M:%S", gmtime(ellapse_time))}]')
        return ellapse_time
    @staticmethod
    def runtime(duration):
        print(f'Total run_time: {strftime("%H:%M:%S", gmtime(duration))}')

class RenderJSON(object):
    def __init__(self, json_data):
        json_data = RenderJSON.doc_to_json(json_data)
        if isinstance(json_data, dict):
            self.json_str = json.dumps(json_data)
        else:
            self.json_str = json_data
        self.uuid = str(uuid.uuid4())
    def _ipython_display_(self):
        display_html('<div class="render_json" id="{}" style="font-size:1.2em; height: 600px; width:100%;"></div>'.format(self.uuid), raw=True)
        display_javascript("""
        require(['"""+JS_FILE+"""'], function() {
        document.getElementById('%s').appendChild(renderjson(%s))
        });
        """ % (self.uuid, self.json_str), raw=True)
    @staticmethod
    def pprint(json_data, sort_keys=True, indent=4):
        """ print using pygments """
        json_data = RenderJSON.doc_to_json(json_data)
        from pygments import highlight, lexers, formatters
        formatted_json = json.dumps(json_data, sort_keys=sort_keys, indent=indent)
        colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
        print(colorful_json)
    @staticmethod
    def dprint(data, indent=4, sort_keys=True):
        """ print only using json.dumps """
        data = RenderJSON.doc_to_json(data)
        print(json.dumps(data, indent=indent, sort_keys=sort_keys))
    @staticmethod
    def doc_to_json(mongo_doc) -> dict:   
        import importlib
        bson_installed = importlib.util.find_spec("bson")
        found = bson_installed is not None
        if found:
            from bson import json_util
        else:
            return mongo_doc
        return json.loads(json_util.dumps(mongo_doc))

class NBFunctions:
    log = RuntimeLogger()
    render = RenderJSON
    
    def __init__(self, v=True):
        self.v = v
        self.set_paths()
        self.load_time = time.time()
        print(f"[load_time]: {datetime.now().strftime('%Y/%m/%d - %H:%M:%S')}")
    
    def set_paths(self):
        self.fp = self.get_notebook_full_path_name()
        self.file_name = self.fp.split('/')[-1]
        folders = self.fp.split('/')
        self.base_dir = "/".join(folders[0:-1])
        self.project_path = "/".join(folders[0:folders.index(PROJECT)+1])
        if self.v:
            print('fp:', self.fp)
            print('file_name:', self.file_name)
            print('base_dir:', self.base_dir)
            print('project_path:', self.project_path)
            print('project:', PROJECT)
        
    def get_notebook_full_path_name(self):        
        kernel_id = re.search('kernel-(.*).json',
                              ipykernel.connect.get_connection_file()).group(1)
        servers = list_running_servers()
        for ss in servers:
            response = requests.get(urljoin(ss['url'], 'api/sessions'),
                                    params={'token': ss.get('token', '')})
            for nn in json.loads(response.text):
                if nn['kernel']['id'] == kernel_id:
                    relative_path = nn['notebook']['path']
                    return os.path.join(ss['notebook_dir'], relative_path) 
                
    @staticmethod
    def restart():
        from IPython.core.display import HTML
        print(f"[restarted]: {datetime.now().strftime('%Y/%m/%d - %H:%M:%S')}")
        return HTML("<script>Jupyter.notebook.kernel.restart()</script>")
    @staticmethod
    def kill():
        import IPython
        IPython.Application.instance().kernel.do_shutdown(True)
    @staticmethod
    def pprint(json_data, sort_keys=True, indent=4):
        """ wrapper to render.pprint() """
        NBFunctions.render.pprint(json_data)
    @staticmethod
    def set_env():
        active_env = !conda info | grep "active envi"
        active_env = active_env[0].split(':')[1]
        display(HTML(f"<p style='font-size:1.2em'>Conda_environment: <b style='color:#523ac9'>{active_env}</b></p>"))
    def get_real_path(self):
        global BASE
        global _FOLDER
        try:
            if BASE:
                _FOLDER = BASE.split('/')[-1]
                self.folder = _FOLDER
                self.real_path = BASE
        except:
            BASE = os.path.dirname(os.path.realpath("__file__"))
            _FOLDER = BASE.split('/')[-1]
            self.folder = _FOLDER
            self.real_path = BASE    

    @staticmethod    
    def dec(value):
        return '{:,}'.format(value)
    @staticmethod
    def f2(value):
        return "{:.2f}".format(value)
    @staticmethod
    def f3(value):
        return "{:.3f}".format(value)
    @staticmethod
    def f4(value):
        return "{:.4f}".format(value)
    @staticmethod
    def f5(value):
        return "{:.5f}".format(value)
    @staticmethod
    def f6(value):
        return "{:.6f}".format(value)

nb = NBFunctions()
nb.set_env()
!pwd
%cd $nb.project_path
!pwd