import requests, json, sys, time

from getapicreds import snipeurl, apikey
from Machine.hardware import get_serial_number, url_ok
from Machine.newasset import create_new_asset
from Machine.updateasset import update_asset

print("\n Asset update in progress... \n")
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

#print(Asset_data)

if "rows" in Asset_data:
    update_asset(Asset_data)
else:
    create_new_asset()