import upload_data as upl, calculations as calc, output_info as out
if __name__ == '__main__':
    data = upl.read_bars()
    current_coords = {40,55}
    closest_bar = calc.shortest_way(current_coords, data)
    out.output(closest_bar)
