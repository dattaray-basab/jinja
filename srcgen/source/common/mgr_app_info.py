import os
import shutil

from srcgen.source.common.constants import RAW_FOLDER, SOURCE_FOLDER, TOKEN_FOLDER, SCHEMA_FOLDER
from srcgen.source.common.dot_dict import DotDict


def app_info_mgr():
    # cwd = os.path.abspath( )
    app_info = {}
    app_info['app_dirpath'] = os.path.abspath( os.curdir)
    app_info['token_dirpath'] = os.path.join(app_info['app_dirpath'], TOKEN_FOLDER)
    app_info['schema_dirpath'] = os.path.join( app_info['app_dirpath'], SCHEMA_FOLDER )

    app_info['raw_dir_path'] = os.path.join(app_info['app_dirpath'] , RAW_FOLDER)
    _source_dir_path = os.path.join( app_info['app_dirpath'], SOURCE_FOLDER )
    if os.path.exists(_source_dir_path):
        shutil.rmtree( _source_dir_path )
    os.mkdir(_source_dir_path)
    return app_info

