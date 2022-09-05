from jinja2 import FileSystemLoader, Environment

from soft_gen.source.Filters.str_ops import filter_x1
from soft_gen.source.Functions.fn_group_1 import fn_x2
from soft_gen.source.common.constants import RAW_DIRPATH


def env_mgr():
    def fn_getenv(dirpath):
        file_loader = FileSystemLoader( dirpath )
        env = Environment( loader=file_loader )
        env.filters["filter_x1"] = filter_x1
        env.globals["fn_x2"] = fn_x2
        return env

    return fn_getenv