import ipaddress
from Machine.initialize import locations_json, variables_json


def find_location(ipadr):
    for key, value in locations_json.items():
        location_bool = ipaddress.ip_address(ipadr) in ipaddress.ip_network(key)
        if location_bool == True:
            return value
            break
        notfound = get_unknown_location_snipe_field()
    return notfound
        
def get_location_snipe_field_status():
    td = variables_json["variables"]["ipaddress_location_enable"]
    return td

def get_unknown_location_snipe_field():
    field2 = variables_json["variables"]["unkown_location_value"]
    return field2

def get_location_snipe_field():
    field = variables_json["variables"]["ipaddress_field"]
    return field

def get_ipaddress(attributes):
    address = attributes[get_location_snipe_field()]
    return address
    