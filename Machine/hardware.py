import os, json, datetime

def get_time_and_date():
    local_date = str(datetime.datetime.now())
    return local_date

def get_date_snipe_field_status():
    with open('Config/othervariables.json') as json_file:
        variable = json.load(json_file)
    td = variable["variables"]["date_time_enabled"]
    return td

def get_date_snipe_field():
    with open('Config/othervariables.json') as json_file:
        variable = json.load(json_file)
    field = variable["variables"]["date_field"]
    return field

def get_serial_number(data):
    return os.popen('wmic bios get serialnumber | find /v "SerialNumber"').read().replace("\n","").replace("   ","").replace("  ","").replace(" ","")

def get_asset_id(banana):
    Assetid = banana['rows'][0]["id"]
    return Assetid

def get_machine_attributes_v2(data):
    with open('Config/othervariables.json') as json_file:
        variable = json.load(json_file)
    formatting = variable["format"]
    for key, item in data.items():
        output = os.popen(item).read().replace("\n","").replace("   ","").replace("  ","")
        for tablekey, code in formatting.items():
            if tablekey != key:
                continue
            else:
                output = eval(code)
                break
        data[key] = output
    return data