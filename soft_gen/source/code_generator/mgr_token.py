import json
import os

from soft_gen.source.code_generator.mgr_validation import validation_mgr
from soft_gen.source.common.constants import SCHEMA_FOLDER, DEFAULT_SCHEMA_REL_FILEPATH
from soft_gen.source.common.dot_dict import DotDict


def token_mgr(app_info):
    def _fn_get_json_file_data(filepath):
        if not os.path.exists( filepath ):
            return None

        with open( filepath, 'r' ) as f:
            data = json.load( f )
        return data

    fn_validate_json_data_file, fn_validate_json_data = validation_mgr(app_info)
    def fn_get_tokens(token_dirpath):
        try:
            file_paths = []
            tokens = DotDict( {} )
            for root, directories, file in os.walk( token_dirpath ):
                for file in file:
                    if (file.endswith( ".json" )):
                        file_paths.append( os.path.join(root, file) )
            tokens = DotDict({})
            for filepath in file_paths:

                data = _fn_get_json_file_data( filepath )
                if data is None:
                    raise Exception( 'ERROR: unable to find file {}'.format(filepath))


                schema_filepath = os.path.join(app_info['schema_dirpath'], DEFAULT_SCHEMA_REL_FILEPATH)
                schema_data = _fn_get_json_file_data( schema_filepath )
                if schema_data is not None:
                    error_code = fn_validate_json_data( schema_filepath, data )
                    if error_code is not None:
                        raise Exception(error_code)

                content = data['content']
                file_name, file_ext = os.path.basename(filepath).rsplit('.')
                tokens[file_name] = content

            return tokens

        except Exception as x:
            print(x)
            return None



    return  fn_get_tokens