import importlib
import os
from inspect import isfunction, getmembers

from jinja2 import FileSystemLoader, Environment

from codegen.src.__FILTERS.str_ops import flt_x1
from codegen.src.__FUNCTIONS.str_fns import fn_x2
from codegen.src.common.constants import ENV_FILTERS, ENV_FUNCTIONS


def env_mgr(app_info):

    def _fn_attach_local_bindings_to_env (env_place, folder_name):
        dirpath = os.path.join(app_info['lib_src_dirpath'] , folder_name)
        filenames = []
        for root, dirs, files in os.walk( dirpath ):
            if root.endswith(folder_name):
                for file in files:
                    filenames.append( file )

        for filename in filenames:
            module_name = filename.rsplit(".", 1)[0]
            module_dot_path = 'codegen.src.{}.{}'.format(folder_name, module_name)
            module = importlib.import_module( module_dot_path )
            for member in getmembers( module ):
                if isfunction(member[1]):
                    if member[0] not in env_place.keys():
                        env_place[member[0]] = member[1]

    def fn_getenv(dirpath):
        file_loader = FileSystemLoader( dirpath )
        env = Environment( loader=file_loader )

        _fn_attach_local_bindings_to_env( env.filters, ENV_FILTERS )
        _fn_attach_local_bindings_to_env( env.globals, ENV_FUNCTIONS )

        return env

    return fn_getenv

# module_dot_path = 'codegen.src.__FUNCTIONS.str_fns'
# module = importlib.import_module( module_dot_path )
# fn_list = [o for o in getmembers( module ) if isfunction( o[1] )]
# env.filters["flt_x1"] = flt_x1
# env.globals["fn_x2"] = fn_list[0] # fn_x2