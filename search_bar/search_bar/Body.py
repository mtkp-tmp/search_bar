import load_data as ld

UserCoord = {"X": 0.0, "Y": 0.0}

print("Введите свои координаты")
UserCoord["X: "] = float(input("Долгота: "))
UserCoord["Y: "] = float(input("Широта: "))
output = ld.Poisk(UserCoord)

print("Название: ",str(output["Name"]))
print("Адрес: ",str(output["Address"]))
print("Количество мест: ",int(output["SeatsCount"]))
print("Тип: ",str(output["TypeObject"]))
print("Телефон: ",str(output["PublicPhone"]))
