import json, ipaddress

def find_location(ipadr):
    with open('Config/locationatlas.json') as json_file:
        locations = json.load(json_file)
    for key, value in locations.items():
        location_bool = ipaddress.ip_address(ipadr) in ipaddress.ip_network(key)
        if location_bool == True:
            return value
            break
        notfound = get_unknown_location_snipe_field()
    return notfound
        
def get_location_snipe_field_status():
    with open('Config/othervariables.json') as json_file:
        variable = json.load(json_file)
    td = variable["variables"]["ipaddress_location_enable"]
    return td

def get_unknown_location_snipe_field():
    with open('Config/othervariables.json') as json_file:
        variable = json.load(json_file)
    field2 = variable["variables"]["unkown_location_value"]
    return field2

def get_location_snipe_field():
    with open('Config/othervariables.json') as json_file:
        variable = json.load(json_file)
    field = variable["variables"]["ipaddress_field"]
    return field

def get_ipaddress(attributes):
    address = attributes[get_location_snipe_field()]
    return address
    