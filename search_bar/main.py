from json import load
from calculations import calculations
with open('C:\\Users\\Max\\Desktop\\data-2897-2017-12-21.json','r') as f:
    data, shortest_way_distance, current_coords = load(f), 1999.0, { "Latitude_WGS84" : float(input("Введите долготу")), "Longitude_WGS84" : float(input("Введите широту")) }
for element in data:
    closest_coords = {"Latitude_WGS84" : float(element["Latitude_WGS84"]), "Longitude_WGS84" : float(element["Longitude_WGS84"]) }
    if shortest_way_distance > calculations(current_coords["Latitude_WGS84"], current_coords["Longitude_WGS84"], closest_coords["Latitude_WGS84"], closest_coords["Longitude_WGS84"]):
        shortest_way_distance, shortest_way = calculations(current_coords["Latitude_WGS84"], current_coords["Longitude_WGS84"], closest_coords["Latitude_WGS84"], closest_coords["Longitude_WGS84"]), { "Название ближайшего бара" : element["Name"], "Адрес бара" : element["Address"], "Количество сидячих мест" : element["SeatsCount"] }
print(shortest_way)
