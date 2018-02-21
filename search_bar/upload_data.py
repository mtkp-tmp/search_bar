import json

def ReadJson(file):
    json_sting = file.read()
    parsed_string = json.loads(json_sting)
    return  parsed_string
