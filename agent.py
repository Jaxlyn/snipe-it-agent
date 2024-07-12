import requests, json

from Machine.getapicreds import snipeurl, apikey
from Machine.hardware import get_machine_attributes_v2, get_serial_number, get_asset_id, get_time_and_date, get_date_snipe_field_status, get_date_snipe_field
from Machine.location import find_location, get_location_snipe_field_status, get_ipaddress

with open('Config/commands.json') as json_file:
    data = json.load(json_file)

serial = get_serial_number(data)

url = snipeurl + "/hardware/byserial/" + serial + "?deleted=false"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + apikey
}

response = requests.get(url, headers=headers)

Asset_data = json.loads(response.text)

url2 = snipeurl + "/hardware/" + str(get_asset_id(Asset_data))

print(url2)

machine = get_machine_attributes_v2(data)

yes_or_no = get_date_snipe_field_status()
if yes_or_no == True:
    the_field = get_date_snipe_field()
    machine[the_field] = get_time_and_date()

no_or_yes = get_location_snipe_field_status()
if no_or_yes == True:
    strawberry = get_ipaddress(machine)
    machine["location_id"] = find_location(strawberry)

print(machine)

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + apikey,
    "content-type": "application/json"
}

response = requests.put(url2, json=machine, headers=headers)

print(response.text)

#print(data)
#print(Asset_data)

#modified_json = json.dumps(data)