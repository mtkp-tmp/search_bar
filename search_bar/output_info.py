from unicodedata import normalize as norm
def output(d : dict): print("{\n"+"\tНазвание ближайшего бара"+" : "+norm('NFKD', d["Название ближайшего бара"]).encode('ASCII')+"\n\tАдрес бара"+" : "+d["Адрес бара"]+"\n\tКоличество сидячих мест"+" : "+str(d["Количество сидячих мест"])+"\n}")
#unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore')
