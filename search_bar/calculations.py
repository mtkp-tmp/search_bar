from math import sqrt

def CalculBar(parsed_string):
    x =float(input("input longitude: "))  #55.772519
    y =float(input("input latitude: "))   #37.685202
    lst = []
    for i in (parsed_string):
        formula = sqrt((i.get('geoData').get('coordinates')[1] - x)**2 + (i.get('geoData').get('coordinates')[0] - y)**2)
        lst.append(formula)
        index = lst.index(min(lst))
    return index

