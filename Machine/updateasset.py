import requests, time

from Machine.initialize import variables_json
from getapicreds import snipeurl, apikey
from Machine.hardware import get_machine_attributes_v2, get_asset_id, get_time_and_date, get_date_snipe_field
from Machine.location import find_location, get_ipaddress
from Machine.model import get_model_id

def update_asset(Asset_data):
    update_asset_id_url = snipeurl + "/hardware/" + str(get_asset_id(Asset_data))

    payload = get_machine_attributes_v2()

    yes_or_no = variables_json["variables"]["date_time_enabled"]
    if yes_or_no == True:
        the_field = get_date_snipe_field()
        payload[the_field] = get_time_and_date()

    no_or_yes = variables_json["variables"]["ipaddress_location_enable"]
    if no_or_yes == True:
        strawberry = get_ipaddress(payload)
        payload[variables_json["variables"]["location_field"]] = find_location(strawberry)

    noyesno = variables_json["variables"]["update_model_attributes"]
    if noyesno == True:
        payload["model_id"] = get_model_id()

    yesnoyesno = variables_json["variables"]["update_status_id"]
    if yesnoyesno == True:
        payload["status_id"] = variables_json["variables"]["default_status_id"]


    #print(payload)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + apikey,
        "content-type": "application/json"
    }

    response = requests.patch(update_asset_id_url, json=payload, headers=headers)

    #print(response.text)