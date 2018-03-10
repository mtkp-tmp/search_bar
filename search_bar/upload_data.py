from json import load as l
from os.path import isfile as isf
def read_bars(): # Вводимая директория файла json
    while True:
        try:
            path = input("Введите директорию .json файла").strip() #"search_bar/data.json"  
            with open(path, "r", encoding="windows-1251") as f: return(l(f)) # Открытие файла и удаление символа возврата каретки \r 
            if isf(path)==True: break
        except OSError: print("Файл не найден!")
        
