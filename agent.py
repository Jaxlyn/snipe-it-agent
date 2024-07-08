import os, requests, sys

from dotenv import load_dotenv, dotenv_values

load_dotenv()

def getMachine_addr():
	os_type = sys.platform.lower()
	if "win" in os_type:
		command = "wmic bios get serialnumber"
	elif "linux" in os_type:
		command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
	elif "darwin" in os_type:
		command = "ioreg -l | grep IOPlatformSerialNumber"
	return os.popen(command).read().replace("\n","").replace("	","").replace(" ","").replace("SerialNumber", "")

#output machine serial code: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX

serial = (getMachine_addr())

print(serial)

print(os.getenv("SNIPE_URL"))

url = os.getenv("SNIPE_URL") + "/hardware/byserial/" + serial + "?deleted=false"

print(url)

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + os.getenv("API_KEY")
}

response = requests.get(url, headers=headers)

print(response.text)