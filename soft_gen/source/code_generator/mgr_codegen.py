import os

from soft_gen.source.common.constants import RAW_DIRPATH
from soft_gen.source.env_mgt.mgr_env import env_mgr
from src.basab_expts.Tokens.mgr_token import token_mgr


def codegen_mgr(caller_filepath):
    _root_dir = os.path.join(os.path.dirname(caller_filepath), RAW_DIRPATH)
    fn_get_tokens = token_mgr()
    tokens = fn_get_tokens()
    fn_getenv = env_mgr()


    def fn_generate_code_for_file(dirpath, filename):
        try:
            env = fn_getenv(dirpath)
            tm = env.get_template( filename )
            msg = tm.render( tokens )
            print(msg)
        except Exception as x:
            print(x)

    def fn_generate_code_for_dir(root_dirpath):
        for root, dirs, files in os.walk( root_dirpath ):
            for filename in files:
                fn_generate_code_for_file(root, filename)
            for subdir in dirs:
                fn_generate_code_for_dir( os.path.join(root, subdir) )

            x = 1

    def fn_generate_code():
        fn_generate_code_for_dir( _root_dir )

    return fn_generate_code