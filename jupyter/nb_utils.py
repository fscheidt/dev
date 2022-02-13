# utils to set notebook context
# update_version: https://raw.githubusercontent.com/fscheidt/dev/master/jupyter/nb_utils.py
import os
from IPython.display import display_javascript, display_html, display, HTML

# 🟡 project dir_name
PROJECT='gitlog_builder'

_FOLDER = ''
CTX = {}
def show_env():    
    active_env = !conda info | grep "active envi"
    active_env = active_env[0].split(':')[1]
    CTX['conda_env'] = active_env
    display(HTML(f"<p style='font-size:1.2em'>Conda_environment: <b style='color:#523ac9'>{active_env}</b></p>"))

def get_notebook_dir(v=False) -> str:
    CTX['project']=PROJECT
    global BASE
    global _FOLDER
    base_path = ''
    try:
        if BASE:
            base_path = BASE
            _FOLDER = BASE.split('/')[-1]
    except:
        BASE = os.path.abspath('')
        _FOLDER = BASE.split('/')[-1]
        base_path = os.path.abspath('')  # current notebook folder
    if v: print('Notebook location:', base_path)
    return base_path

def get_notebook_abs_base_path(
        target_base='notebooks',
        resource_dir="static",
        file_name=None,
        v=False):
    dirname = get_notebook_dir() # current notebook folder
    folders = dirname.split('/')
    base_path = ''
    for f in folders:
        base_path += f+'/'
        if f == target_base:
            break
    if file_name:
        base_path = os.path.join(base_path,resource_dir,file_name)
    else:
        base_path = os.path.join(base_path,resource_dir)
    if v: print('Notebooks base folder:', base_path)
    return base_path

def get_notebook_rel_base_path(target_base='notebooks',
                               resource_dir="static",
                               file_name=None,
                               v=False):
    global _FOLDER
    dirname = get_notebook_dir()  # current notebook folder
    folders = dirname.split('/')
    folder = ''
    rel_path = ''
    i = -1
    cc = 0
    if target_base == _FOLDER:
        return "./"
    while folder != target_base:
        if v: print(folder, ' == ', target_base)
        rel_path += '../'
        i -= 1
        if folders[i]:
            folder = folders[i]
        else:
            return None
        cc += 1
        if cc > 50:
            print('!could not buid relative path')
            break
    if file_name:
        rel_path = os.path.join(rel_path, resource_dir, file_name)
    else:
        rel_path = os.path.join(rel_path, resource_dir)
    if v: print('Notebooks relative folder:', rel_path)
    return rel_path

def _print_paths():   
    global _FOLDER
    print('\nFolder:\n\t', _FOLDER)
    print('\nThis_notebook_path:\n\t', NOTE_DIR)
    print('\nNotebooks_abs_path:\n\t', NOTEBOOKS_ABS_DIR)
    print('\nNotebooks_rel_relative_path:\n\t', NOTEBOOKS_REL_DIR)
    print('\nProject_abs_path:\n\t', PROJECT_ABS_DIR)
    print('\nProject_rel_path:\n\t', PROJECT_REL_DIR)   
    print('\nStatic_dir_relative_path:\n\t', STATIC_DIR_REL_PATH)
    print('\nStatic_dir_absolute_path:\n\t', STATIC_DIR_ABS_PATH)
    print('\n[renderjson.js] abs_path:\n\t', RENDER_JS_ABS_PATH)  
    print('\n[renderjson.js] rel_path:\n\t', RENDER_JS_REL_PATH)
    
def _info():
    print(f'{"PROJECT_ABS_DIR: ": <18} {PROJECT_ABS_DIR}')
    print(f'{"NOTE_PATH: ": <18} {NOTE_DIR}')
    print(f'{"RENDERJSON: ": <18} {RENDER_JS_LC_PATH}')
    show_env()

# 🟡 resource folder - containing js+other files
RESOURCE_DIR='static'

NOTE_DIR = get_notebook_dir()
CTX['note_dirname'] = NOTE_DIR

NOTEBOOKS_ABS_DIR = get_notebook_abs_base_path(resource_dir='')
CTX['note_abs_path'] = NOTEBOOKS_ABS_DIR

NOTEBOOKS_REL_DIR = get_notebook_rel_base_path(resource_dir='')
CTX['note_rel_path'] = NOTEBOOKS_REL_DIR

PROJECT_ABS_DIR = get_notebook_abs_base_path(target_base=PROJECT,resource_dir='')    
PROJECT_REL_DIR = get_notebook_rel_base_path(target_base=PROJECT, resource_dir='')
STATIC_DIR_REL_PATH = get_notebook_rel_base_path(resource_dir=RESOURCE_DIR)
STATIC_DIR_ABS_PATH = get_notebook_abs_base_path(resource_dir=RESOURCE_DIR)
RENDER_JS_ABS_PATH = get_notebook_abs_base_path(file_name="renderjson.js")
RENDER_JS_REL_PATH = get_notebook_rel_base_path(resource_dir=RESOURCE_DIR, file_name="renderjson.js")
# RENDER_JS_LC_PATH = RENDER_JS_ABS_PATH
RENDER_JS_LC_PATH = RENDER_JS_REL_PATH

# _print_paths()
print(f'{"PROJECT: ": <18} {PROJECT}')
print(f'{"PWD: ": <18}', end=' ')
%cd $PROJECT_ABS_DIR

_info()