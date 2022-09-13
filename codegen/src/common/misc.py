# it contains helper functions for:
# 1) finding path delimiters that vary between OS's.
# The Windows OS path delimiter is '\\' whereas path delimiter for MacOS and Linux is '/'
# At runtime the path limiter has to be determined
# 2) Retrieving the function body from a package

import importlib


def fn_get_function_dynamically(package_name, module_name, object_name):
    module_dot_path = "{}.{}".format(package_name, module_name)
    try:
        module = importlib.import_module(module_dot_path)
        fn_body = getattr(module, object_name)
    except Exception:
        return None
    return fn_body


def fn_get_path_separator(dir_path):
    path_separator = '/'
    if '/' not in dir_path:
        path_separator = '\\'
    return path_separator

# >>> from inspect import getmembers, isfunction
# >>> import helloworld
# >>> print [o for o in getmembers(helloworld) if isfunction(o[1])]
