import json
import os

from codegen.src.code_generator.mgr_validation import validation_mgr
from codegen.src.common.constants import SCHEMA_NAME, SCHEMA_DIRPATH, CONTENT
from codegen.src.common.dot_dict import DotDict


def context_mgr(app_info):
    def _fn_get_json_file_data(filepath):
        if not os.path.exists( filepath ):
            return None

        with open( filepath, 'r' ) as f:
            data = json.load( f )
        return data

    fn_validate_json_data_file, fn_validate_json_data = validation_mgr(app_info)
    def fn_get_context(token_dirpath):
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
                if SCHEMA_NAME in data.keys():
                    schema_filepath = os.path.join( app_info[SCHEMA_DIRPATH], data[SCHEMA_NAME] + '.json' )
                    if os.path.exists(schema_filepath):
                        _fn_run_schema_check( data, schema_filepath )

                content = data[CONTENT]
                file_name, file_ext = os.path.basename(filepath).rsplit('.')
                tokens[file_name] = content

            return tokens

        except Exception as x:
            print(x)
            return None

    def _fn_run_schema_check(data, schema_filepath):
        schema_data = _fn_get_json_file_data( schema_filepath )
        if schema_data is not None:
            error_code = fn_validate_json_data( schema_filepath, data )
            if error_code is not None:
                raise Exception( error_code )

    return  fn_get_context