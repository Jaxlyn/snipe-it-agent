import requests

from Machine.initialize import commands_json, variables_json
from getapicreds import snipeurl, apikey
from Machine.hardware import get_machine_attributes_v2, get_time_and_date, get_date_snipe_field, get_serial_number
from Machine.location import netboxlocation, get_ipaddress 
from Machine.user import get_checkout_snipe_field_status, get_checkout_to_user_snipe_field_status
from Machine.model import get_model_id
from Machine.user import get_user_id, get_user

def get_serial_as_asset_status():
    td = variables_json["variables"]["use_serial_as_asset_tag"]
    return td

def create_new_asset():

    new_asset_id_url = snipeurl + "/hardware"

    payload = get_machine_attributes_v2()

    yes_or_no = variables_json["variables"]["date_time_enabled"]
    if yes_or_no == True:
        the_field = get_date_snipe_field()
        payload[the_field] = get_time_and_date()

    no_or_yes = variables_json["variables"]["ipaddress_location_enable"]
    if no_or_yes == True:
        strawberry = get_ipaddress(payload)
        payload[variables_json["variables"]["location_field"]] = netboxlocation(strawberry)
    
    blueberry = get_serial_as_asset_status()
    if blueberry == True:
        payload["asset_tag"] = get_serial_number()

    payload["serial"] = get_serial_number()

    payload["model_id"] = get_model_id()

    payload["status_id"] = variables_json["variables"]["default_status_id"]

    payload["rtd_location_id"] = variables_json["variables"]["default_location"]

    yesyes = get_checkout_snipe_field_status()
    yesnoyes = get_checkout_to_user_snipe_field_status()
    if yesyes == True:
        if yesnoyes == True:
            payload["assigned_user"] = user_id =get_user_id(get_user())
            if user_id == None:
                chicken = get_ipaddress(payload)
            payload["assigned_location"] = netboxlocation(chicken)
        else:    
            chicken = get_ipaddress(payload)
            payload["assigned_location"] = netboxlocation(chicken)

    #print(payload)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + apikey,
        "content-type": "application/json"
    }

    response = requests.post(new_asset_id_url, json=payload, headers=headers, verify=variables_json["variables"]["verify_ssl_snipe_url"])

    #print(response.text)