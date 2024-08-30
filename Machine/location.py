import ipaddress
from Machine.initialize import locations_json, variables_json
import json, requests
from Machine.initialize import variables_json
from getapicreds import apikey, snipeurl, netboxurl, netboxkey

import requests

def netboxlocation(ipaddress):
    print("\nUpdating Location...\n")
    if variables_json["variables"]["enable_net_box"] == True:
        ipv4address = ipaddress
        url3 = netboxurl + "/api/ipam/prefixes/?contains=" + ipv4address + "&status=active"

        headers2 = {
            "accept": "application/json",
            "Authorization": "Token " + netboxkey
        }

        response2 = requests.get(url3, headers=headers2, verify=False)

        something2 = json.loads(response2.text)

        if something2["count"] > 0:
            print("\nAsset Location: " + something2["results"][0]["site"]["name"])
            applecrisp = something2["results"][0]["site"]["name"]
            url = snipeurl + "/locations?limit=5&offset=0&" + variables_json["variables"]["location_search_field"] + "=" + applecrisp

            headers = {
                "accept": "application/json",
                "Authorization": "Bearer " + apikey
            }

            response = requests.get(url, headers=headers)

            #print(response.text)
            something = json.loads(response.text)

            location = int(something["rows"][0]["id"])
        else:
            location = find_location(ipv4address)
            #location = int(variables_json["variables"]["unkown_location_value"])
        return location
    else:
        #print("no netbox")
        ipv4address = ipaddress
        location = find_location(ipv4address)
        return location

def find_location(ipadr):
    for key, value in locations_json.items():
        location_bool = ipaddress.ip_address(ipadr) in ipaddress.ip_network(key)
        if location_bool == True:
            return value
            break
        notfound = variables_json["variables"]["unkown_location_value"]
    return notfound

def get_ipaddress(attributes):
    address = attributes[variables_json["variables"]["ipaddress_field"]]
    return address
    