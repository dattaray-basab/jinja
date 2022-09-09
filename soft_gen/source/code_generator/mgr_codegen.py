import os

from soft_gen.source.common.constants import RAW_FOLDER, SOURCE_FOLDER
from soft_gen.source.common.mgr_app_info import app_info_mgr
from soft_gen.source.env_mgt.mgr_env import env_mgr
from soft_gen.source.code_generator.mgr_token import token_mgr


def codegen_mgr(caller_filepath, app_info = None):
    app_info = app_info_mgr(caller_filepath)

    fn_get_tokens = token_mgr(app_info)
    tokens = fn_get_tokens(app_info['token_dirpath'])
    fn_getenv = env_mgr()

    def _fn_replace_write_text_file(file_path, data):
        try:
            dir_path = os.path.dirname(file_path)
            if not os.path.exists( dir_path ):
                os.makedirs( dir_path )
            if os.path.exists( file_path ):
                os.remove( file_path )

            with open( file_path, 'w' ) as f:
                f.write( data )
        except Exception as x:
            print(x)

    def _fn_generate_code_for_file(dirpath, filename):
        try:
            env = fn_getenv(dirpath)
            tm = env.get_template( filename )

            data = tm.render( tokens )
            # print(data)

            source_dirpath = dirpath.replace(RAW_FOLDER, SOURCE_FOLDER)

            source_filepath = os.path.join(source_dirpath, filename)

            _fn_replace_write_text_file( source_filepath, data )

        except Exception as x:
            print(x)
            raise Exception('ERROR: _fn_generate_code_for_file')

    _raw_dirs_and_files = []
    def _fn_generate_code_for_dir(root_dirpath):
        for root, dirs, files in os.walk( root_dirpath ):
            _raw_dirs_and_files.append( (root, files) )

        for d, files in _raw_dirs_and_files:
            for f in files:
                _fn_generate_code_for_file(d, f)
            x = 1

    def _fn_generate_code():
        _fn_generate_code_for_dir( app_info['raw_dir_path'] )

    _fn_generate_code()
