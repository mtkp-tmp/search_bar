if __name__ == "__main__":
  print('go!')

import json
import re

# coordInp = input("Введите координаты: ")

with open('data-2897-2017-12-21.json', 'r', encoding='windows-1251') as fileJSON:
    data = json.load(fileJSON)

dataFrJS = json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
print(dataFrJS)

# название ближайшего бара
# адрес бара
# количество сидячих мест

'''name = re.findall(r'"Name": "\s*([^,]+|\S+)"', dataFrJS)
SeatsCount = re.findall(r'"SeatsCount": \s*([^,]+|\S+)', dataFrJS)
Address = re.findall(r'"Address": "\s*([^,]+|\S+)', dataFrJS)

print(name)
print(Address)
print(SeatsCount)'''


print(data[0]['Name'])


# mas = {key:search_ID_FrJS[i] for i, key in enumerate(search_GlID_FrJS)}

fileJSON.close()
