import json
import os

import jsonschema
from jsonschema import validate

def fn_validate_json(json_data):

    def _fn_get_schema():
        """This function loads the given schema available"""

        '/Users/bd/Documents/__DEV_2/Ideas/SoftGen/1/jinja/src/json_validator/user_schema.json'
        schema_path = 'user_schema.json'
        with open( schema_path, 'r' ) as file:
            schema = json.load( file )
        return schema



    execute_api_schema = _fn_get_schema()

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message