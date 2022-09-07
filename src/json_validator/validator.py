import json

from soft_gen.source.code_generator.mgr_validation import validation_mgr

fn_validate_json_file, fn_validate_json = validation_mgr(__file__)

jsonData = json.loads('{"id" : "10", "name": "DonOfDen","contact_number":1234567890}')


print('fn_validate_json')
error_code = fn_validate_json( 'user_schema.json', jsonData)
if error_code:
    print(error_code)
else:
    print('success')
print()


print('fn_validate_json_file')
error_code = fn_validate_json_file( 'user_schema.json', 'udata.json' )
if error_code:
    print(error_code)
else:
    print('success')
print()