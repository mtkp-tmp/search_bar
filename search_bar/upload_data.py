from json import load as l
from os.path import isfile as isf
def read_bars(): # Вводимая директория файла json
    path = ""
    while True:
        try:
            while isf(path) !=  True:   # Проверка на правильность ввода директории и типа файла
                path = 'data.json'
                print(path) #отладка travis
                if isf(path) == False: print("Файл не найден, попробуйте ввести директорию файла заново")
                else: break
                with open(path,'r',encoding='windows-1251') as f: return(l(f)) # Открытие файла            
        except: data = read_bars()
