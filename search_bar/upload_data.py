import json

def getBars():
    with open('data-2897-2017-12-21.json', 'r', encoding='windows-1251') as fjs:
        return json.load(fjs)

