import requests, json, sys, time

from getapicreds import snipeurl, apikey, netboxurl
from Machine.hardware import get_serial_number, url_ok
from Machine.newasset import create_new_asset
from Machine.updateasset import update_asset
from Machine.initialize import variables_json

print("\nAsset update in progress... \n")
#print(snipeurl)

connection_established = url_ok(snipeurl + "/hardware", variables_json["variables"]["verify_ssl_snipe_url"])
#print(connection_established)

if connection_established == False:
    print("\nNo dice... Ending Update\n")
    time.sleep(5)
    sys.exit()

if variables_json["variables"]["enable_net_box"] == True:
    connection_established = url_ok(netboxurl, variables_json["variables"]["verify_ssl_netbox_url"])
    #print(connection_established)
    if connection_established == False:
        print("\nNo dice... Ending Update\n")
        time.sleep(5)
        sys.exit()

serial = get_serial_number()

get_serial_number_asset_arrtibutes_url = snipeurl + "/hardware/byserial/" + serial + "?deleted=false"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + apikey
}

response = requests.get(get_serial_number_asset_arrtibutes_url, headers=headers, verify=variables_json["variables"]["verify_ssl_snipe_url"])

Asset_data = json.loads(response.text)

#print(Asset_data)

if Asset_data["total"] > 0:
    print("Asset exists...")
    update_asset(Asset_data)
else:
    print("Asset does not exist...\nCreating Asset...")
    create_new_asset()

print("\nUpdate Completed...")
time.sleep(5)