# SET notebook context
def get_notebook_dir(v=False):
    import os
    dirname = os.path.abspath('')  # current notebook folder
    if v: print('Notebook location:', dirname)
    return dirname

def get_notebook_abs_base_path(target_base='notebooks',
                               resource_dir="static",
                               file_name=None,
                               v=False):
    import os
    dirname = os.path.abspath('')  # current notebook folder
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
    import os
    dirname = os.path.abspath('')  # current notebook folder
    folders = dirname.split('/')
    folder = ''
    rel_path = ''
    i = -1
    cc = 0
    while folder != target_base:
        rel_path += '../'
        i -= 1
        folder = folders[i]
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


NOTE_DIR = get_notebook_dir()
print('Notebook location:', NOTE_DIR)

NOTEBOOKS_ABS_DIR = get_notebook_abs_base_path(resource_dir='')
print('Notebooks base folder:', NOTEBOOKS_ABS_DIR)

NOTEBOOKS_BASE_REL = get_notebook_rel_base_path()
print('Notebooks relative folder:', NOTEBOOKS_BASE_REL)

RENDER_JS_ABS_PATH = get_notebook_abs_base_path(file_name="renderjson.js")
print('renderjson.js abs path:', RENDER_JS_ABS_PATH)

RENDER_JS_REL_PATH = get_notebook_rel_base_path(file_name="renderjson.js")
print('renderjson.js rel path:', RENDER_JS_REL_PATH)