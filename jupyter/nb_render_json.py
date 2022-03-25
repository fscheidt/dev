# RENDER JSON
from IPython.display import display_javascript, display_html
import uuid
import json
JS_FILE = "https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/renderjson.js",
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
        json_data = RenderJSON.doc_to_json(json_data)
        from pygments import highlight, lexers, formatters
        formatted_json = json.dumps(json_data, sort_keys=sort_keys, indent=indent)
        colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
        print(colorful_json)   
    @staticmethod
    def dprint(data, indent=4, sort_keys=True):
        data = RenderJSON.doc_to_json(data)
        print(json.dumps(data, indent=indent, sort_keys=sort_keys))
    @staticmethod
    def doc_to_json(mongo_doc) -> dict:      
        import importlib
        bson_installed = importlib.util.find_spec("bson")        
        if bson_installed is not None:
            from bson import json_util
        else:
            return mongo_doc
        return json.loads(json_util.dumps(mongo_doc))
class NBFunctions:    
    render = RenderJSON    
    @staticmethod
    def pprint(json_data, sort_keys=True, indent=4):
        NBFunctions.render.pprint(json_data)
    @staticmethod
    def dec(value):
        return '{:,}'.format(value) 
    @staticmethod
    def f4(value):
        return "{:.4f}".format(value)
nb = NBFunctions()