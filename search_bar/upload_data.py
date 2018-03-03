from json import load as l
from os.path import isfile as isf
def read_bars(): # Вводимая директория файла json
    path = ""
    while True:
        try:
            while (isf(path) !=  True) and (path[len(path)-5:len(path)] != ".json"):   # Проверка на правильность ввода директории и типа файла
                path = input("Введите путь к файлу json") # C:\\Users\\Lenovo\\Desktop\\data-2897-2017-12-21.json
                if isf(path) == False: print("Файл не найден, попробуйте ввести директорию файла заново")
                with open(path,'r',encoding='windows-1251') as f: return(l(f)) # Открытие файла            
        except:
            if path[len(path)-5:len(path)] != ".json": print("Файл имеет формат не .json")
            data = read_bars()
        else: break
