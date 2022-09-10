import json
import os

import jsonschema
from jsonschema import validate

def validation_mgr(context = None, apply_context = True):
    app_dirpath = None
    if context:
        app_dirpath = context['app_dirpath']

    def _fn_load_json_file(json_filepath):
        try:
            if apply_context:
                json_filepath  = os.path.join(app_dirpath, json_filepath)

            abs_filepath = os.path.abspath( json_filepath )
            with open( abs_filepath, 'r' ) as file:
                data = json.load( file )
                return data
        except Exception as x:
            print( x )
            return None

    def fn_validate_json_data(schema_filepath, json_data):

        schema = _fn_load_json_file(schema_filepath)
        if schema is None:
            return 'ERROR: cannot load schema'

        try:
            validate(instance=json_data, schema=schema)

        except jsonschema.exceptions.ValidationError as err_code:
            print(err_code)
            err_code = "ERROR: Given JSON data is InValid"
            return err_code

        return None

    def fn_validate_json_data_file(schema_filepath, json_filepath):
        data = _fn_load_json_file(json_filepath)
        if data is None:
            return False, 'ERROR: cannot load json data'

        error_code = fn_validate_json_data( schema_filepath, data )
        return error_code

    return fn_validate_json_data_file, fn_validate_json_data




