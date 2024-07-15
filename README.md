# snipe-it-agent
Simple customizable Snipe-IT Agent

Requirements

requests

pyinstaller


Set up:

apicreds.json

Add api url and api token.


commands.json

Custom fields and windows commands


othervariables.json - powershell_enable is nonfunctional

Optional additions and formatting options for windows command outputs. (Formatting uses python)


locationatlas.json - optional

Location reference for ip subnets and location ids in snipe-it



pyinstaller --noconsole --add-data "Config\commands.json:Config" --add-data "Config\locationatlas.json:Config" --add-data "Config\othervariables.json:Config" --add-data "Config/apicreds.json:Config" assetmgr_agent.py

pyinstaller --add-data "Config\commands.json:Config" --add-data "Config\locationatlas.json:Config" --add-data "Config\othervariables.json:Config" --add-data "Config/apicreds.json:Config" assetmgr_agent.py

After building move config folder from _internal to root folder
