import pickle
import DataBase

FILE_NAME = 'databook.dat'

def main():
    choose = input("Вы хотите считать из базы данных, записать новые данные,\nили стереть старую и создать новую? \"С/З/НОВАЯ\"  ")
    if choose == "З":
        make_book()
    elif choose == "С":
        read_book()
    elif choose == "НОВАЯ":
        new_book()
    else:
        print("\nВы ввели некорректное значение!")
        print()
        main()

def make_book():
    stop = None
    book = open(FILE_NAME, 'ab')
    while stop != "Д":
        name = input("Имя: ")
        soname = input("Фамилия: ")
        phone = input("Номер телефона: ")
        DB = DataBase.DataBase(name, soname, phone)
        pickle.dump(DB, book)
        stop = input("Нажмите \"Д\" для завершения")
        stop = stop.upper()
        print()

def read_book():
    end_of_file = False
    book = open(FILE_NAME, 'rb')
    while not end_of_file:
        try:
            data = pickle.load(book)
            show_book(data)
        except EOFError:
            end_of_file = True

def show_book(data):
    print()
    print("Имя: ", data.get_name())
    print("Фамилия: ", data.get_soname())
    print("Номер телефона: ", data.get_phone())
    print()

def new_book():
    stop = None
    book = open(FILE_NAME, 'wb')
    while stop != "Д":
        name = input("Имя: ")
        soname = input("Фамилия: ")
        phone = input("Номер телефона: ")
        DB = DataBase.DataBase(name, soname, phone)
        pickle.dump(DB, book)
        stop = input("Нажмите \"Д\" для завершения")
        stop = stop.upper()
        print()
    
main()
