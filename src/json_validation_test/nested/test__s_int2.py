import json
import os

from soft_gen.source.code_generator.mgr_validation import validation_mgr

app_dirpath = os.path.dirname(__file__)
fn_validate_json_data_file, fn_validate_json_data = validation_mgr({'app_dirpath':app_dirpath})

error_code = fn_validate_json_data_file( 's_int2.json', 't_int.json' )
if error_code:
    print(error_code)
else:
    print('success')
print()