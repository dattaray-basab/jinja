import json
import jsonschema
from jsonschema import validate

def fn_validate_json(json_data):
    def _fn_get_schema():
        """This function loads the given schema available"""
        with open( 'user_schema.json', 'r' ) as file:
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