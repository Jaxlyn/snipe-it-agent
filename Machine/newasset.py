import requests

from Machine.initialize import commands_json, variables_json
from getapicreds import snipeurl, apikey
from Machine.hardware import get_machine_attributes_v2, get_time_and_date, get_date_snipe_field_status, get_date_snipe_field, get_serial_number
from Machine.location import find_location, get_location_snipe_field_status, get_ipaddress

def get_serial_as_asset_status():
    td = variables_json["variables"]["use_serial_as_asset_tag"]
    return td

def create_new_asset():

    new_asset_id_url = snipeurl + "/hardware"

    payload = get_machine_attributes_v2(commands_json)

    yes_or_no = get_date_snipe_field_status()
    if yes_or_no == True:
        the_field = get_date_snipe_field()
        payload[the_field] = get_time_and_date()

    no_or_yes = get_location_snipe_field_status()
    if no_or_yes == True:
        strawberry = get_ipaddress(payload)
        payload[variables_json["variables"]["location_field"]] = find_location(strawberry)
    
    blueberry = get_serial_as_asset_status()
    if blueberry == True:
        payload["asset_tag"] = get_serial_number()

    payload["status_id"] = variables_json["variables"]["default_status_id"]

    print(payload)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + apikey,
        "content-type": "application/json"
    }

    response = requests.post(new_asset_id_url, json=payload, headers=headers)

    print(response.text)