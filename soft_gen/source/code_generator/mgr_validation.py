import json
import os

import jsonschema
from jsonschema import validate

def validation_mgr(caller_context = None):
    _caller_dirpath = None

    if caller_context:
        if type(caller_context) == str:
            _caller_dirpath = os.path.dirname( caller_context )
        else:
            _caller_dirpath = os.path.dirname( caller_context )

    def _fn_load_json_file(json_filepath):
        try:
            if _caller_dirpath:
                json_filepath  = os.path.join(_caller_dirpath, json_filepath)

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
            return False, 'ERROR: cannot load schema'


        try:
            validate(instance=json_data, schema=schema)
        except jsonschema.exceptions.ValidationError as err_code:
            print(err_code)
            err_code = "Given JSON data is InValid"
            return err_code

        return None

    def fn_validate_json_data_file(schema_filepath, json_filepath):
        data = _fn_load_json_file(json_filepath)
        if data is None:
            return False, 'ERROR: cannot load json data'

        error_code = fn_validate_json_data( schema_filepath, data )
        return error_code

    return fn_validate_json_data_file, fn_validate_json_data




