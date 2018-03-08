from unicodedata import normalize as norm 
def output(d : dict): print("{\n"+"\tНазвание ближайшего бара"+" : "+norm('NFD', d["Название ближайшего бара"])+"\n\tАдрес бара"+" : "+d["Адрес бара"]+"\n\tКоличество сидячих мест"+" : "+str(d["Количество сидячих мест"])+"\n}")
