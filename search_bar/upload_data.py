from json import load as l
from codecs import open as o
def read_bars(): # Вводимая директория файла json
    try:
        path = input("Введите директорию .json файла") #"search_bar/data.json"  
        with o(path[0:len(path)-1],'r', "utf-16") as f: return(l(f)) # Открытие файла и удаление символа возврата каретки \r 
    except OSError: print("Файл не найден!")
        
    '''
    while True:
        try:
            while isf(path) !=  True:   # Проверка на правильность ввода директории и типа файла
                #path = input("Введите директорию .json файла")
                print(path) #отладка travis
                if isf(path) == False: print("Файл не найден, попробуйте ввести директорию файла заново")
                else: break
                with open(path,'r',encoding='windows-1251') as f: return(l(f)) # Открытие файла            
        except: data = read_bars()
   '''
