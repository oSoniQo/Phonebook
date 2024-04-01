def load():
    phonebook={}
    try:
        with open("phonebook.txt", "r") as file:
            for line in file:
                name, phone, birthday, email = line.strip().split(',')
                phonebook[name]={}
                phonebook[name]["phone"] = phone
                phonebook[name]["birthday"] = birthday
                phonebook[name]["email"] = email          
    except:
        phonebook={"Mr. Example" : {"phone": ["12345"], "birthday": ["01.01.2001"], "email": ["example@gmail.com"]}}
        with open("phonebook.txt", "w+") as file:
            for line in file:
                name, phone, birthday, email = line.strip().split(',')
                phonebook[name]={}
                phonebook[name]["phone"] = phone
                phonebook[name]["birthday"] = birthday
                phonebook[name]["email"] = email
    return phonebook

def save():
    with open('phonebook.txt', 'w') as file:
        for name, data in directory.items():
            file.write(f"{name},{data["phone"]},{data["birthday"]},{data["email"]}\n")
        print("Изменения успешно сохранены!")

def add():
    choice = input("Что вы хотите добавить? (контакт - contact , значение - value ) : ")
    if choice == "contact":
        name = input("Введите имя контакта: ")
        phone = input("Введите телефон: ")
        birthday = input("Введите дату рождения: ")
        email = input("Введите электронную почту: ")
        directory[name]={}
        try:
            directory[name]["phone"].append(phone)
        except:
            directory[name]["phone"] = []
            directory[name]["phone"].append(phone)
        try:
            directory[name]["birthday"].append(birthday)
        except:
            directory[name]["birthday"] = []
            directory[name]["birthday"].append(birthday)
        try:
            directory[name]["email"].append(email)
        except:
            directory[name]["email"] = []
            directory[name]["email"].append(email)
        print("Данные успешно добавлены в справочник!")
    elif choice == "value":
        name = input("Введите имя контакта: ")
        option = input("Введите параметр, в который хотите добавить данные (phone, birthday, email): ")
        value = input("Введите значение параметра: ")
        try:
            directory[name][option].append(value)
            print("Данные успешно добавлены в справочник!")
        except:
            print("Что-то пошло не так... Проверьте введенные данные и повторите попытку")
    else:
        print("Что-то пошло не так... Проверьте введенные данные и повторите попытку")
def delete():
    name = input("Введите имя для удаления: ")
    choice = input("Что вы хотите удалить? (контакт - contact , значение - value ) : ")
    if choice == "contact":
        if name in directory:
            del directory[name]
            print("Контакт успешно удален!")
        else:
            print("Контакт не найден.")
    elif choice == "value":
        option = input("Введите параметр, из которого хотите удалить данные (phone, birthday, email): ")
        value = input("Введите данные для удаления: ")
        try:
            temp = directory[name][option].index(value)
            del directory[name][option][temp]
            print("Данные успешно удалены!")
        except:
            print("Что-то пошло не так... Проверьте введенные данные и повторите попытку")
    else:
        print("Что-то пошло не так... Проверьте введенные данные и повторите попытку")
def change():
    name = input("Введите имя для изменения: ")
    option = input("Введите параметр, который хотите изменить (name, phone, birthday, email): ")
    value_old = input("Введите значение для изменения: ")
    value_new = input("Введите новое значение: ")
    if name in directory:
        if option=="name":
            directory[value_new] = directory.pop(name)
            print("Данные успешно изменены!")
        else:
            try:
                temp = directory[name][option].index(value_old)
                directory[name][option][temp] = value_new
                print("Данные успешно изменены!")
            except:
                print("Что-то пошло не так... Проверьте введенные параметры и повторите попытку")
    else:
        print("Контакт не найден.")

def show():
    print("Ваш телефонный справочник: ")
    for name, data in directory.items():
        print(f"{name}: {data}")

def search():
    option=input("Введите параметр поиска (name, phone, birthday, email): ")
    value1=input("Введите значение параметра: ")
    if option== "name":
        print("Результаты по вашему запросу: ")
        for key in directory:
            if key==value1:
                print(f"{key}: {directory[key]}")   
    else:
        try:
            print("Результаты по вашему запросу: ")
            for key, value in directory.items():
                for i in value[option]:
                    if i == value1:
                        print(f"{key}: {directory[key]}")    
        except:
            print("Что-то пошло не так... Проверьте введенные параметры и повторите попытку")
            
directory=load()

choice = input("Введите /start, чтобы начать: ")
if choice == "/start":
    while True:
        command = input("\nВаш запрос: ")
        
        if command == '/add':
            add()
            
        elif command == '/delete':
            delete()
            
        elif command == '/change':
            change()
            
        elif command == '/show':
            show()
        
        elif command == '/search':
            search()
        elif command == '/save':
            save()
            
        elif command == '/quit':
            print("Вы точно хотите выйти? Убедитесь, что сохранили нужные вам изменения. (введите 'yes', если хотите выйти)")
            choice=input("Ваш ответ: ").lower()
            if choice=='yes':
                break
        
        elif command=='/help':
            print("""
    /add - добавление контакта
    /delete - удаление контакта
    /change - изменение контакта
    /show - просмотр контактов
    /search - поиск контакта
    /help - помощь
    /save - сохранение изменений
    /quit - выход
                """)
            
        else:
            print("Незнакомая команда. Попробуйте еще раз или загляните в инструкцию (команда /help)")