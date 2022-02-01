# utils print json_data and mongo_documents
# update_version: https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/render_json.py
import uuid
from IPython.display import display_javascript, display_html, display
import json

# 🟡 filepath
JS_FILE = RENDER_JS_LC_PATH or "https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/renderjson.js"


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
    def print_pyg(json_data):
        json_data = RenderJSON.doc_to_json(json_data)
        from pygments import highlight, lexers, formatters
        formatted_json = json.dumps(json_data, sort_keys=True, indent=4)
        colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
        print(colorful_json)

    @staticmethod
    def doc_to_json(mongo_doc):
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

# test:
# RenderJSON(json_doc)
# RenderJSON({'star':'one', 'distance': '4.4'})
# RenderJSON.print_pyg({'star':'one', 'distance': '4.4'})