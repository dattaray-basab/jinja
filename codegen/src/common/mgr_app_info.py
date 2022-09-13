import os
import shutil

from codegen.src.common.constants import RAW_FOLDER, SOURCE_FOLDER, TOKEN_FOLDER, SCHEMA_FOLDER
from codegen.src.common.dot_dict import DotDict


def app_info_mgr():
    # cwd = os.path.abspath( )
    app_info = {}
    app_info['app_dirpath'] = os.path.abspath( os.curdir)
    app_info['token_dirpath'] = os.path.join(app_info['app_dirpath'], TOKEN_FOLDER)
    app_info['schema_dirpath'] = os.path.join( app_info['app_dirpath'], SCHEMA_FOLDER )

    this_dirpath = os.path.realpath( __file__ )
    app_info['lib_src_dirpath'] = os.path.dirname(os.path.dirname( this_dirpath ))

    app_info['raw_dir_path'] = os.path.join(app_info['app_dirpath'] , RAW_FOLDER)
    _source_dir_path = os.path.join( app_info['app_dirpath'], SOURCE_FOLDER )
    if os.path.exists(_source_dir_path):
        shutil.rmtree( _source_dir_path )
    os.mkdir(_source_dir_path)
    return app_info

