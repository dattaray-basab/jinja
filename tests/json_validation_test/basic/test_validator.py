import json
import os

from soft_gen.source.code_generator.mgr_validation import validation_mgr

app_dirpath = os.path.dirname(__file__)
fn_validate_json_data_file, fn_validate_json_data = validation_mgr({'app_dirpath':app_dirpath})

jsonData = json.loads('{"id" : "ID 10w", "name": "Ashwini","contact_number": 12223334444}')


print('fn_validate_json_data')
error_code = fn_validate_json_data( 'schema.json', jsonData)
if error_code:
    print(error_code)
else:
    print('success')
print()


print('fn_validate_json_data_file')
error_code = fn_validate_json_data_file( 'schema.json', 'input_data.json' )
if error_code:
    print(error_code)
else:
    print('success')
print()