import math

def getShortestWay(bars, x0, y0):

    def getLenOfWay(bar):
        x1 = bar['geoData']['coordinates'][0]
        y1 = bar['geoData']['coordinates'][1]
        return math.sqrt((x1-x0) * (x1-x0) + (y1-y0) * (y1-y0))

    shortest = bars[0]

    for i in range(1, len(bars)):
        shortest = bars[i] if getLenOfWay(shortest) > getLenOfWay(bars[i]) else shortest

    return shortest