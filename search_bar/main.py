import upload_data as updata, calculations as calc, output_info as inf

if __name__ == '__main__':
    bars = updata.getBars()
    while(input('Ввести координаты? (да - любой символ; нет - n): ') != 'n'):
        inf.infoutput(calc.getShortestWay(bars, float(input('Введите широту: ')), float(input('Введите долготу: '))))
        print('------------------------------------')