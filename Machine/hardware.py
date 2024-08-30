import os, datetime, requests, sys
from Machine.initialize import variables_json, commands_json

#here lies my attempt, forever forgotton
#def slice_ip_address(address):
#    carrot = address[2:18]
#    output = carrot[:carrot.find('"')]
#    return output

def url_ok(url):
    try:
        response = requests.get(url)
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

def get_date_snipe_field():
    field = variables_json["variables"]["date_field"]
    return field

def get_serial_number():
    brisket = get_os_type()
    if "Windows" in brisket:
        command_os = 'wmic bios get serialnumber | find /v "SerialNumber"'
    elif "Linux" in brisket:
        command_os = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
    elif "MacOS" in brisket:
        command_os = "ioreg -l | grep IOPlatformSerialNumber"
    return os.popen(command_os).read().replace("\n","").replace("   ","").replace("  ","").replace(" ","")

def get_asset_id(banana):
    Assetid = banana['rows'][0]["id"]
    return Assetid

def get_os_type():
    os_type = sys.platform.lower()
    if "win" in os_type:
        type_os = "Windows"
    elif "linux" in os_type:
        type_os = "Linux"
    elif "darwin" in os_type:
        type_os = "MacOS"
    #print(type_os)
    return type_os

def get_machine_attributes_v2():
    blueberry = get_os_type()
    formatting = commands_json[blueberry]["Format"]
    for key, item in commands_json[blueberry]["Commands"].items():
        #print(key)
        output = os.popen(item).read().replace("\n","").replace("   ","")
        for tablekey, code in formatting.items():
            if tablekey != key:
                continue
            else:
                #print(code)
                output = eval(code)
                break
        commands_json[key] = output
        values = commands_json
    return values