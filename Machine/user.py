from getapicreds import snipeurl, apikey
from Machine.initialize import variables_json
import requests, os, json

def get_checkout_snipe_field_status():
    tb = variables_json["variables"]["checkout_on_creation"]
    return tb

def get_checkout_to_user_snipe_field_status():
    tp = variables_json["variables"]["checkout_to_user_on_creation"]
    return tp

def get_user():
    return os.popen('whoami').read().replace("\n","").replace("   ","").replace("  ","").replace(" ","")

def get_user_id(user):

    url = snipeurl + "/users?search=" + user + "&limit=50&offset=0&sort=created_at&order=desc&deleted=false&all=false"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + apikey
    }

    response = requests.get(url, headers=headers)
    User_data = json.loads(response.text)

    print(User_data["total"])
    for x in range(0,int(User_data["total"]),1):
        if user == User_data["rows"][x]["username"].lower():
            user_id = User_data["rows"][x]["id"]
            print(user_id)
            return user_id