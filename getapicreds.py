#from dotenv import load_dotenv
import os, json

#load_dotenv()
#apikey = os.getenv("API_KEY")
#snipeurl = os.getenv("SNIPE_URL")
#print(apikey)
#print(snipeurl)

with open('Config/apicreds.json') as json_file:
    apicreds_json = json.load(json_file)
apikey = apicreds_json["API_KEY"]
snipeurl = apicreds_json["SNIPE_URL"]