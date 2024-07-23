import os, json, requests

from getapicreds import snipeurl, apikey
from Machine.initialize import models_json, variables_json

def get_local_model_name():
    model = os.popen('wmic csproduct get name | find /v "Name"').read().replace("\n","").replace("   ","").replace("  ","")
    return model

def get_local_model_type():
    chassis = os.popen('wmic systemenclosure get chassistypes | find /v "ChassisTypes"').read().replace("\n","").replace("   ","").replace("  ","").replace(" ","")
    return chassis

def get_local_asset_manufacturer():
    maker = os.popen('wmic computersystem get manufacturer | find /v "Manufacturer"').read().replace("\n","").replace("   ","").replace("  ","").replace(" ","%20")
    return maker

def get_product_number():
    product = os.popen('wmic computersystem get SystemSKUNumber | find /v "SystemSKUNumber"').read().replace("\n","").replace("   ","").replace("  ","").replace(" ","")
    return product

#used for creating new asset
def get_model_id():
    search_key = get_local_model_name()
    second_search_key = get_product_number()

    url = snipeurl + "/models?limit=50sdas&offset=0&search=" + search_key + "&sort=created_at&order=asc"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + apikey
    }

    response = requests.get(url, headers=headers)

    Model_data = json.loads(response.text)

    for x in range(0, Model_data["total"], 1):
        if search_key == Model_data["rows"][x]["name"] and second_search_key == Model_data["rows"][x]["model_number"]:
            model_id = Model_data["rows"][x]["id"]
            return model_id

    print("Model not found...\nCreating Model...")
    model_data_id = create_model(search_key)

    model_id = model_data_id["payload"]["id"]
    return model_id

def get_manufacturer_id():
    manufacture = get_local_asset_manufacturer()

    url = snipeurl + "/manufacturers?name=" + manufacture

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + apikey
    }

    response = requests.get(url, headers=headers)

    Model_manufacture = json.loads(response.text)

    if Model_manufacture["total"] == 0:
        print("Unknown Manufacturer...")
        return variables_json["unknown_manufacture_id"]
    for x in range(0, Model_manufacture["total"], 1):
        if manufacture == Model_manufacture["rows"][x]["name"]:
            model_id = Model_manufacture["rows"][x]["id"]
            return model_id


#used for creating new model
def get_model_category():
    model_type = get_local_model_type()

    for id in models_json:
        if id == model_type:
            model_category = models_json[id]
            return model_category
        else:
            continue

def create_model(local_model_name):

    url = snipeurl + "/models"

    payload = {
    "name": local_model_name,
    "category_id": int(get_model_category()),
    "manufacturer_id" : get_manufacturer_id(),
    "model_number" : get_product_number(),
    "fieldset_id": variables_json["variables"]["default_custom_fieldset_id"],
    "eol" : variables_json["variables"]["end_of_life"]
    }

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + apikey,
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    model_data = json.loads(response.text)
    #print(model_data)
    return model_data