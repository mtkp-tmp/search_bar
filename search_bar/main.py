#__________________________________________________________________________________________________________
#Шаблон модуля main
#__________________________________________________________________________________________________________
import upload_data #Или |from upload_data import имя_функции| для импортирования только одной функции
import calculations
import output_info
#вызовы функций из модулей:
#имя_модуля.имя_функции()

if __name__ == "__main__":
  main()
#__________________________________________________________________________________________________________
#Черновик
#__________________________________________________________________________________________________________
import json
import math

'''coordX = input("Введите координаты X: ")
coordY = input("Введите координаты Y: ")'''

with open('data-2897-2017-12-21.json', 'r', encoding='windows-1251') as fileJSON:
    data = json.load(fileJSON)

print(data[0]['Name'])
print(data[0]['Address'])
print(data[0]['SeatsCount'])
print(data[0]['geoData']['coordinates'][0])
print(data[0]['geoData']['coordinates'][1])

fileJSON.close()

#Позже перенести в upload_data.py
