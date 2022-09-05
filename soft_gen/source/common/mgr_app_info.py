import os
import shutil

from soft_gen.source.common.constants import RAW_DIRPATH, SOURCE_DIRPATH, TOKEN_DIRPATH
from soft_gen.source.common.dot_dict import DotDict


def app_info_mgr(caller_filepath):
    app_info = DotDict({})
    app_info.app_dirpath = os.path.dirname( caller_filepath )
    app_info.token_dirpath = os.path.join(app_info.app_dirpath, TOKEN_DIRPATH)

    app_info.raw_dir_path = os.path.join(os.path.dirname(caller_filepath), RAW_DIRPATH)
    _source_dir_path = os.path.join( app_info.app_dirpath, SOURCE_DIRPATH )
    if os.path.exists(_source_dir_path):
        shutil.rmtree( _source_dir_path )
    os.mkdir(_source_dir_path)
    return app_info

