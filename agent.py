import os, requests, json

from dotenv import load_dotenv, dotenv_values
from Machine.hardware import get_machine_attributes, command, get_serial_number

load_dotenv()

serial = get_serial_number()

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

get_machine_attributes()

for item in data['rows']:
	for key, value in command:
		if value != item:
			data['rows'][0][key] = value
		else:
			continue

print(data)

modified_json = json.dumps(data)