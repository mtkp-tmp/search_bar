import json
from calculations import calculations
from upload_data import upload_data


def output_info():
    path = 0.01
    x1 = 55.753712  # input('Введите широту: Для примера можно взять - 55.753712: ')
    y1 = 37.619877  # input('Введите долготу: Для примера можно взять - 37.619877: ')
    for global_id in upload_data():
        x2 = global_id["geoData"]["coordinates"][1]
        y2 = global_id["geoData"]["coordinates"][0]

        if calculations(x1, y1, x2, y2) < path:
            path = calculations(x1, y1, x2, y2)
            name_bar = ("Название бара: "
                        + str(global_id["Name"]) + '\nАдрес бара: '
                        + str(global_id["Address"]) + '\nСидячих мест: '
                        + str(global_id["SeatsCount"]) + '\n\nПриянтого отдыха!')
    print(name_bar)