import locale
locale.setlocale(locale.LC_ALL, "Russian Russia.l251")
def output(d : dict): print("{\n"+"\tНазвание ближайшего бара"+" : "+d["Название ближайшего бара"]+"\n\tАдрес бара"+" : "+d["Адрес бара"]+"\n\tКоличество сидячих мест"+" : "+str(d["Количество сидячих мест"])+"\n}")
