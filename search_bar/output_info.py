def OutputBar(parsed_string,index):
    print("Название заведения: ", parsed_string[index].get('Name'))
    print("Адрес заведения: ", parsed_string[index].get('Address'))
    print("Телефонный номер: 8", parsed_string[index].get('PublicPhone')[0].get('PublicPhone'))
    print("Количество сидящих мест: ", parsed_string[index].get('SeatsCount'))

