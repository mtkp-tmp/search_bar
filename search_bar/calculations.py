from math import sqrt
def calc(x0, y0, x1, y1 : float) -> float: return sqrt((x1 * x1 - 2 * x0 * x1 + x0 * x0) + (y1 * y1 - 2 * y0 * y1 + y0 * y0))
def shortest_way(current_coords : dict, data : dict) -> dict:
    shortest_way_distance = calc(current_coords["Latitude_WGS84"], current_coords["Longitude_WGS84"], float(data[0]["Latitude_WGS84"]), float(data[0]["Longitude_WGS84"]))
    for ind_data in range(1,len(data)):
        closest_coords = {"Latitude_WGS84" : float(data[ind_data]["Latitude_WGS84"]), "Longitude_WGS84" : float(data[ind_data]["Longitude_WGS84"]) }
        if shortest_way_distance > calc(current_coords["Latitude_WGS84"], current_coords["Longitude_WGS84"], closest_coords["Latitude_WGS84"], closest_coords["Longitude_WGS84"]): shortest_way_distance, shortest_way = calc(current_coords["Latitude_WGS84"], current_coords["Longitude_WGS84"], closest_coords["Latitude_WGS84"], closest_coords["Longitude_WGS84"]), { "Название ближайшего бара" : data[ind_data]["Name"], "Адрес бара" : data[ind_data]["Address"], "Количество сидячих мест" : data[ind_data]["SeatsCount"] }
    return shortest_way
