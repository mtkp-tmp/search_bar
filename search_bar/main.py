from json import load as l
from calculations import calculations as calc
with open('C:\\Users\\Lenovo\\Desktop\\data-2897-2017-12-21.json','r') as f:
    data, current_coords = l(f), { "Latitude_WGS84" : float(input("Введите долготу")), "Longitude_WGS84" : float(input("Введите широту")) }
    shortest_way_distance = calc(current_coords["Latitude_WGS84"], current_coords["Longitude_WGS84"], float(data[0]["Latitude_WGS84"]), float(data[0]["Longitude_WGS84"]))
for ind_data in range(1,len(data)):
    closest_coords = {"Latitude_WGS84" : float(data[ind_data]["Latitude_WGS84"]), "Longitude_WGS84" : float(data[ind_data]["Longitude_WGS84"]) }
    if shortest_way_distance > calc(current_coords["Latitude_WGS84"], current_coords["Longitude_WGS84"], closest_coords["Latitude_WGS84"], closest_coords["Longitude_WGS84"]):
        shortest_way_distance, shortest_way = calc(current_coords["Latitude_WGS84"], current_coords["Longitude_WGS84"], closest_coords["Latitude_WGS84"], closest_coords["Longitude_WGS84"]), { "Название ближайшего бара" : data[ind_data]["Name"], "Адрес бара" : data[ind_data]["Address"], "Количество сидячих мест" : data[ind_data]["SeatsCount"] }
print(shortest_way)
