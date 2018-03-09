#! Функция, выполняющая математические вычисления
def calculations(coord1, coord2, data):
    minimum = 99999.0
    for bar in data:
        distance = ((coord1-bar['geoData']['coordinates'][1]) ** 2)+((coord2-bar['geoData']['coordinates'][0]) ** 2)
        if distance < minimum:
            minimum = distance
            closes_bar = bar
    return closes_bar
