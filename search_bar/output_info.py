import sys
import codecs
sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')
def output(d : dict): print("{\n"+"\tНазвание ближайшего бара"+" : "+d["Название ближайшего бара"]+"\n\tАдрес бара"+" : "+d["Адрес бара"]+"\n\tКоличество сидячих мест"+" : "+str(d["Количество сидячих мест"])+"\n}")
