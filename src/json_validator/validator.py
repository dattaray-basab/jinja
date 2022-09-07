import json

from soft_gen.source.common.json_validator import fn_validate_json

jsonData = json.loads('{"id" : "10", "name": "DonOfDen","contact_number":1234567890}')

# validate it
is_valid, msg = fn_validate_json( jsonData )
print(msg)
