import upload_data as upl, calculations as calc, output_info as out
if __name__ == '__main__':
    data = upl.read_bars()
    while True:
        try: current_coords = { "Latitude_WGS84" : float(input("Введите долготу")), "Longitude_WGS84" : float(input("Введите широту")) }
        except ValueError:
            print("Введённые координаты не могут быть преобразованый в float, попробуйте ввести координаты снова")
            try: current_coords
            except NameError: current_coords = {}
        if len(current_coords.keys()) == 2: break
    closest_bar = calc.shortest_way(current_coords, data)
    out.output(closest_bar)
