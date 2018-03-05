import upload_data as upl, calculations as calc, output_info as out
if __name__ == '__main__':
    data = upl.read_bars()
    while True: # Проверка на правильность ввода координат
        try: current_coords = { "Latitude_WGS84" : 40.0, "Longitude_WGS84" : 55.0 }
        except ValueError: print("Введённые координаты не могут быть преобразованый в float, попробуйте ввести координаты снова")
        else: break
    closest_bar = calc.shortest_way(current_coords, data)
    out.output(closest_bar)
