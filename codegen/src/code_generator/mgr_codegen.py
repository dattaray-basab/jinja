import os

from codegen.src.common.constants import RAW_FOLDER, SOURCE_FOLDER, ERROR_ON_MISSING_CONTEXT
from codegen.src.common.mgr_app_info import app_info_mgr
from codegen.src.code_generator.mgr_env import env_mgr
from codegen.src.code_generator.mgr_context import context_mgr


def codegen_mgr(app_info = None):
    app_info = app_info_mgr()

    fn_get_context = context_mgr(app_info)
    context = fn_get_context(app_info['token_dirpath'])
    if ERROR_ON_MISSING_CONTEXT and context is None:
        raise Exception( 'ERROR: Missing Context' )
    if context is not None:
        fn_getenv = env_mgr(app_info)

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
            if context is not None:
                env = fn_getenv( dirpath )
                tm = env.get_template( filename )
                data = tm.render( context )
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
