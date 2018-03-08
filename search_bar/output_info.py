import sys, locale
sys.setdefaultencoding(locale.getpreferredencoding())
def output(d : dict): print("{\n"+"\tНазвание ближайшего бара"+" : "+d["Название ближайшего бара"]+"\n\tАдрес бара"+" : "+d["Адрес бара"]+"\n\tКоличество сидячих мест"+" : "+str(d["Количество сидячих мест"])+"\n}")
