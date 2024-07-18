import json

with open('Config/locationatlas.json') as json_file:
    locations_json = json.load(json_file)
    #print(locations_json)
    
with open('Config/othervariables.json') as json_file:
    variables_json = json.load(json_file)
    #print(variables_json)

with open('Config/commands.json') as json_file:
    commands_json = json.load(json_file)
    #print(commands_json)

with open('Config/model_categories.json') as json_file:
    models_json = json.load(json_file)
    #print(models_json)