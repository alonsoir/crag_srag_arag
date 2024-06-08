import json

from dorks.ninjadorks import create_json_structure

json_data = create_json_structure('some_dorks.txt')

# Guardar el JSON en un archivo
with open('some_dorks.json', 'w') as file:
    json.dump(json_data, file, indent=4)