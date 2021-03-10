class DataBase:

    def __init__(self, name, soname, phone):  #Инициализируем атрибуты класса
        self.__name = name
        self.__soname = soname
        self.__phone = phone

    def set_name(self, name):  #Принимаем аргумент для имени
        self.__name = name

    def set_soname(self, soname): #Принимаем аргумент для фамилии
        self.__soname = soname

    def set_phone(self, phone):  #Принимаем аргумент для номера телефона
        self.__phone = phone

    def get_name(self):  #Возвращаем имя
        return self.__name

    def get_soname(self):  #Возвращаем фамилию
        return self.__soname

    def get_phone(self):  #Возвращаем телефон
        return self.__phone
