import os, requests, json

from dotenv import load_dotenv, dotenv_values
from functions.get_serial_number import getMachine_addr

load_dotenv()

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

data = json.loads(response.text)

asset_serial = data['rows'][0]['serial']
asset_name = data['rows'][0]['name']

print(asset_name)

if asset_name != "Ecyuida":
	data['rows'][0]['name'] = "Ecyuida"

print(data)

modified_json = json.dumps(data)