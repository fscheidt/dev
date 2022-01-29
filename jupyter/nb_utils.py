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
print('\nThis_notebook_path:\n\t', NOTE_DIR)

NOTEBOOKS_ABS_DIR = get_notebook_abs_base_path(resource_dir='')
print('\nNotebooks_abs_path:\n\t', NOTEBOOKS_ABS_DIR)

NOTEBOOKS_REL_DIR = get_notebook_rel_base_path(resource_dir='')
print('\nNotebooks_rel_relative_path:\n\t', NOTEBOOKS_REL_DIR)

PROJECT_ABS_DIR = get_notebook_abs_base_path(target_base="gitlog_builder",resource_dir='')
print('\nProject_abs_path:\n\t', PROJECT_ABS_DIR)

PROJECT_REL_DIR =  get_notebook_rel_base_path(target_base="gitlog_builder", resource_dir='')
print('\nProject_rel_path:\n\t', PROJECT_REL_DIR)

STATIC_DIR_REL_PATH = get_notebook_rel_base_path(resource_dir="static")
print('\nStatic_dir_relative_path:\n\t', STATIC_DIR_REL_PATH)

STATIC_DIR_ABS_PATH = get_notebook_abs_base_path(resource_dir="static")
print('\nStatic_dir_absolute_path:\n\t', STATIC_DIR_ABS_PATH)

RENDER_JS_ABS_PATH = get_notebook_abs_base_path(file_name="renderjson.js")
print('\n[renderjson.js] abs_path:\n\t', RENDER_JS_ABS_PATH)

RENDER_JS_REL_PATH = get_notebook_rel_base_path(resource_dir="static", file_name="renderjson.js")
print('\n[renderjson.js] rel_path:\n\t', RENDER_JS_REL_PATH)