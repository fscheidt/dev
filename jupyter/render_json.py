import uuid
from IPython.display import display_javascript, display_html, display
import json

JS_FILE = "https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/renderjson.js"
# JS_FILE = RENDER_JS_REL_PATH

class RenderJSON(object):
    def __init__(self, json_data):
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
        from pygments import highlight, lexers, formatters
        formatted_json = json.dumps(json_data, sort_keys=True, indent=4)
        colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
        print(colorful_json)

# test:
# RenderJSON(json_doc)
# RenderJSON(fmt.doc_to_json(mongo_doc))