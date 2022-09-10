from jinja2 import FileSystemLoader, Environment

from srcgen.source.Filters.str_ops import flt_x1
from srcgen.source.Functions.str_fns import fn_x2
from srcgen.source.common.constants import RAW_FOLDER


def env_mgr():
    def fn_getenv(dirpath):
        file_loader = FileSystemLoader( dirpath )
        env = Environment( loader=file_loader )
        env.filters["flt_x1"] = flt_x1
        env.globals["fn_x2"] = fn_x2
        return env

    return fn_getenv