import json

JSON_PATH = "./config.json"

hotkeys: str = ""

def readJSON():
     global hotkeys

     with open(JSON_PATH, 'r') as config:
          data = json.load(config)

     hotkeys = data['hotkeys']