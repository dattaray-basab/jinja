import os

from soft_gen.source.common.constants import RAW_DIRPATH
from soft_gen.source.env_mgt.mgr_env import env_mgr
from src.basab_expts.Tokens.mgr_token import token_mgr


def codegen_mgr(caller_filepath):
    _root_dir = os.path.join(os.path.dirname(caller_filepath), RAW_DIRPATH)
    fn_get_tokens = token_mgr()
    tokens = fn_get_tokens()
    fn_getenv = env_mgr()
    env = fn_getenv()

    def fn_generate_code_for_file(filename):
        tm = env.get_template( filename )
        msg = tm.render( tokens )
        print(msg)

    def fn_generate_code(root_dirpath):
        for root, dirs, files in os.walk( root_dirpath ):
            for filename in files:
                fn_generate_code_for_file(filename)
            for subdir in dirs:
                fn_generate_code( os.path.join(root, subdir) )

            x = 1

    fn_generate_code( _root_dir )

    return fn_generate_code