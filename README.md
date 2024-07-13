# snipe-it-agent
Simple customizable Snipe-IT Agent

Requirements
python.dotenv
requests
pyinstaller

Set up:
.env
commands.json
othervaribles.json - powershell_enable is nonfunctional
locationatlas.json - optional

Production build command
pyinstaller --noconsole --add-data "Config\commands.json:Config" --add-data "Config\locationatlas.json:Config" --add-data "Config\othervariables.json:Config" --add-data ".env:." agent.py

Debug build command
pyinstaller --add-data "Config\commands.json:Config" --add-data "Config\locationatlas.json:Config" --add-data "Config\othervariables.json:Config" --add-data ".env:." agent.py

After building move config folder from _internal to root folder