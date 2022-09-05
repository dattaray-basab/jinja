import os

from soft_gen.source.common.constants import RAW_DIRPATH, SOURCE_DIRPATH
from soft_gen.source.env_mgt.mgr_env import env_mgr
from src.basab_expts.Tokens.mgr_token import token_mgr


def codegen_mgr(caller_filepath):
    _raw_dir_path = os.path.join(os.path.dirname(caller_filepath), RAW_DIRPATH)
    _source_dir_path = os.path.join( os.path.dirname( caller_filepath ), SOURCE_DIRPATH )
    if os.path.exists(_source_dir_path):
        os.removedirs(_source_dir_path)
    os.mkdir(_source_dir_path)

    fn_get_tokens = token_mgr()
    tokens = fn_get_tokens()
    fn_getenv = env_mgr()

    def _fn_generate_code_for_file(dirpath, filename):
        try:
            env = fn_getenv(dirpath)
            tm = env.get_template( filename )
            msg = tm.render( tokens )
            print(msg)

            suffix_source_dirpath, _ = dirpath.rsplit('/', 1)
            source_dirpath = os.path.join( suffix_source_dirpath, SOURCE_DIRPATH)
            print(source_dirpath)
            x = 1
        except Exception as x:
            print(x)

    _raw_dirs_and_files = []
    def _fn_generate_code_for_dir(root_dirpath):
        for root, dirs, files in os.walk( root_dirpath ):
            _raw_dirs_and_files.append( (root, files) )

        for d, files in _raw_dirs_and_files:
            for f in files:
                _fn_generate_code_for_file(d, f)
            x = 1

    def _fn_generate_code():
        _fn_generate_code_for_dir( _raw_dir_path )



    _fn_generate_code()

    return