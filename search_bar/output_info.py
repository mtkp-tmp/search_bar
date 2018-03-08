import codecs
decoder = codecs.getincrementaldecoder('zlib')('strict')
def output(d : dict): print("{\n"+"\tНазвание ближайшего бара"+" : "+decoder.decode(d["Название ближайшего бара"])+"\n\tАдрес бара"+" : "+d["Адрес бара"]+"\n\tКоличество сидячих мест"+" : "+str(d["Количество сидячих мест"])+"\n}")
