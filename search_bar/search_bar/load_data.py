import Calc as c
import json

filename = "DataBars.json"
MyFile = open(filename, mode="r")

data = json.load(MyFile)

                                    # A - координаты пользователя
def Poisk(A):
    result = {"Name" : " ", "Address" : " ", "SeatsCount" : 0, "TypeObject" : " ", "PublicPhone" : " "}
    Dist = 999
                                    # Цикл вычисления расстояние от введённой точки до места нахождения баров
    for bar in data:
        barCoord = {"X":float(bar["Longitude_WGS84"]), "Y":float(bar["Latitude_WGS84"])}
        NewDist = c.DistanceToPoint(A,barCoord)

        if NewDist < Dist:
            Dist = NewDist
            result["Name"] = bar["Name"]
            result["Address"] = bar["Address"]
            result["SeatsCount"] = bar["SeatsCount"]
            result["TypeObject"] = bar["TypeObject"]
            for i in bar["PublicPhone"]:
                result["PublicPhone"] = i["PublicPhone"]
    return result
