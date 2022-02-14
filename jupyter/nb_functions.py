# source: https://github.com/fscheidt/dev/blob/master/jupyter/nb_functions.py
from datetime import datetime
from time import strftime
from time import gmtime
import time
import uuid
from IPython.display import display_javascript, display_html, display
import json

"""
Load this script into notebook:
%load https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/nb_functions.py
"""

_DEFS = {
    'JS_URL': "https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/renderjson.js",
    'SOURCE': "https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/nb_functions.py",
    'JS_FILE': None,
}
try:
    # _DEFS['JS_FILE'] = RENDER_JS_LC_PATH or _DEFS['JS_URL']
    _DEFS['JS_FILE'] = ctx.settings.RENDER_JS_LC_PATH or _DEFS['JS_URL']
except:
    _DEFS['JS_FILE'] = _DEFS['JS_URL']
JS_FILE = _DEFS['JS_FILE']

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
        """
        convert mongo document to json
        """        
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

    @staticmethod    
    def dec(value):
        return '{:,}'.format(value)
    @staticmethod
    def float2(value):
        return "{:.2f}".format(value)
    @staticmethod
    def float3(value):
        return "{:.3f}".format(value)
    @staticmethod
    def float4(value):
        return "{:.4f}".format(value)
    @staticmethod
    def float5(value):
        return "{:.5f}".format(value)
    @staticmethod
    def float6(value):
        return "{:.6f}".format(value)

nb = NBFunctions()
# # test:
# print(JS_FILE)
# nb.restart()
# nb.dec(100000)
# nb.log.begin_time()
# nb.render({'data': '1'})
# nb.render.pprint({'data': '1'})
# nb.render.dprint({'data': '1'})