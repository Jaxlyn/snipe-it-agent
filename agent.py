import requests, json, sys, time

from getapicreds import snipeurl, apikey
from Machine.initialize import commands_json
from Machine.hardware import get_serial_number, url_ok, get_machine_attributes_v2
from Machine.newasset import create_new_asset
from Machine.updateasset import update_asset

print("\n Asset update in progress... \n")
print(get_machine_attributes_v2(commands_json))
print(snipeurl)

connection_established = url_ok(snipeurl + "/hardware")

if connection_established == False:
    print("No dice... Ending Update")
    time.sleep(5)
    sys.exit()

serial = get_serial_number()

get_serial_number_asset_arrtibutes_url = snipeurl + "/hardware/byserial/" + serial + "?deleted=false"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + apikey
}

response = requests.get(get_serial_number_asset_arrtibutes_url, headers=headers)

Asset_data = json.loads(response.text)

if Asset_data["messages"] == "Asset does not exist":
    create_new_asset()
else:
    update_asset(Asset_data)