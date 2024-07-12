import os

domain_name = "POMPS\\"

command = {
    "computer_name" : "hostname",
    "serial" : 'wmic bios get serialnumber | find /v "SerialNumber"',
    "memory" : 'wmic computersystem get totalphysicalmemory | find /v "TotalPhysicalMemory"',
    "user" : "whoami",
    "date" : "date /t",
    "time" : "time /t",
    "cpu" : 'wmic cpu get name | find /v "Name"'
}

def get_serial_number():
    return os.popen(command["serial"]).read().replace("\n","").replace("   ","").replace("  ","").replace(" ","")

def get_machine_attributes():
    for key, item in command.items():
        output = os.popen(item).read().replace("\n","").replace("   ","").replace("  ","")
        if key == "memory":
            output = str(round(int(output)/1073741824)) + " GB"
        elif key == "computer_name":
            computername = str(output).lower() + "\\"
        elif key == "user":
            output = output.replace(computername, "").replace(domain_name, "")
        command[key] = output

