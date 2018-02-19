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

# СОСТАВИТЬ КОРТЕЖИ ДЛЯ КАЖДОЙ ПАРЫ АТРИБУТ-ЗНАЧЕНИЕ
nameBlB = re.findall(r'\w+[^"]', dataFrJS) # не работает
print(nameBlB)

# mas = {key:search_ID_FrJS[i] for i, key in enumerate(search_GlID_FrJS)}

fileJSON.close()
