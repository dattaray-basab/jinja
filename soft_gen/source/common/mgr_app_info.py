import os
import shutil

from soft_gen.source.common.constants import RAW_FOLDER, SOURCE_FOLDER, TOKEN_FOLDER
from soft_gen.source.common.dot_dict import DotDict


def app_info_mgr(caller_filepath):
    app_info = {}
    app_info['app_dirpath'] = os.path.dirname( caller_filepath )
    app_info['token_dirpath'] = os.path.join(app_info['app_dirpath'], TOKEN_FOLDER)

    app_info['raw_dir_path'] = os.path.join(os.path.dirname(caller_filepath), RAW_FOLDER)
    _source_dir_path = os.path.join( app_info['app_dirpath'], SOURCE_FOLDER )
    if os.path.exists(_source_dir_path):
        shutil.rmtree( _source_dir_path )
    os.mkdir(_source_dir_path)
    return app_info

