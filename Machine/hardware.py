import os, datetime, requests
from Machine.initialize import variables_json

def url_ok(url):
    try:
        response = requests.head(url)
    except Exception as e:
        print(f"NOT OK: {str(e)}")
        true_or_false = False
        return true_or_false
    else:
        if response.status_code == 200:
            true_or_false = True
            return true_or_false
        else:
            print(f"NOT OK: HTTP response code {response.status_code}")
            true_or_false = False
            return true_or_false

def get_time_and_date():
    local_date = str(datetime.datetime.now())
    return local_date

def get_date_snipe_field_status():
    td = variables_json["variables"]["date_time_enabled"]
    return td

def get_date_snipe_field():
    field = variables_json["variables"]["date_field"]
    return field

def get_serial_number():
    return os.popen('wmic bios get serialnumber | find /v "SerialNumber"').read().replace("\n","").replace("   ","").replace("  ","").replace(" ","")

def get_asset_id(banana):
    Assetid = banana['rows'][0]["id"]
    return Assetid

def get_machine_attributes_v2(data):
    formatting = variables_json["format"]
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