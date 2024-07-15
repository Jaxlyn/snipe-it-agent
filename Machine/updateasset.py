import requests, sys, time

from Machine.initialize import commands_json, variables_json
from getapicreds import snipeurl, apikey
from Machine.hardware import get_machine_attributes_v2, get_asset_id, get_time_and_date, get_date_snipe_field_status, get_date_snipe_field
from Machine.location import find_location, get_location_snipe_field_status, get_ipaddress

def update_asset(Asset_data):
    update_asset_id_url = snipeurl + "/hardware/" + str(get_asset_id(Asset_data))

    payload = get_machine_attributes_v2(commands_json)

    yes_or_no = get_date_snipe_field_status()
    if yes_or_no == True:
        the_field = get_date_snipe_field()
        payload[the_field] = get_time_and_date()

    no_or_yes = get_location_snipe_field_status()
    if no_or_yes == True:
        strawberry = get_ipaddress(payload)
        payload[variables_json["variables"]["location_field"]] = find_location(strawberry)

    print(payload)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + apikey,
        "content-type": "application/json"
    }

    response = requests.patch(update_asset_id_url, json=payload, headers=headers)

    print(response.text)

    print("\nUpdate Completed")
    time.sleep(5)