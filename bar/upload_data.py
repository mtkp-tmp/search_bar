import json
# import math


def upload_data():  		# Функция, загружающая json файл для дальнейшей работы с ней
    return json.load(open("data_bar.json", mode='r'))
	
						
# def TransGrad(R: float):	# транформирует градусы в радианы
#   return math.p   i * R / 180