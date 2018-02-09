import math as m
                            # Функция расчёта дистанции между точками A и B
def DistanceToPoint(A,B):
    return m.sqrt((A["X"]-B["X"])**2+(A["Y"]-B["Y"])**2)
