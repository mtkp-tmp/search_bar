if __name__ == "__main__":
    import  upload_data as up
    import  calculations as cal
    import  output_info as out
    f = open('C:/Users/Владислав/Desktop/data-2897-2017-12-21.json', 'r')
    Parsed_string = up.ReadJson(f)
    Calculation = cal.CalculBar(Parsed_string)
    Out = out.OutputBar(Parsed_string, Calculation)
