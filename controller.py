import view, model

def start():
    while True:
        view.showMenu()
        choice = view.inputInt('Выберите пункт меню: ')

        match (choice):
            case 1:
                try:
                    openFile()
                    print('Книга загружена!')
                except:
                    print('Ошибка работы с файлом')
            case 2:
                try:
                    saveFile()
                    print('\n Книга сохранена!')
                except:
                    print('Ошибка работы с файлом')
                saveFile()
            case 3:
                showAll()
            case 4:
                findContact()
            case 5:
                addContact()
            case 6:
                changeContact()
            case 7:
                deleteContact()
            case _:
                return False

def openFile():
    with open(model.getPath(), 'r', encoding='UTF-8') as data:
        phonebook = data.readlines()
        new_phonebook = []
        for contact in phonebook:
            new_contact = contact.replace('\n', '').split(';')
            new_phonebook.append(new_contact)
        model.setPhoneBook(new_phonebook)

def saveFile():
   with open(model.getPath(), 'w', encoding='UTF-8') as data:
       new_phone_book = []
       for contact in model.getPhoneBook():
           new_phone_book.append(';'.join(contact))
       new_phone_book.sort()
       data.write('\n'.join(new_phone_book))



def showAll():
    phone_book = model.getPhoneBook()
    view.showContacts(phone_book, 'Телефонная книга пуста')

def findContact():
    phone_book = model.getPhoneBook()
    search = view.inputStr('Введите искомый элемент: ')
    search_book = []
    for contact in phone_book:
        for item in contact:
            if search in item:
                search_book.append(contact)
    view.showContacts(search_book, 'Контакт не найден')

def addContact():
    phone_book = model.getPhoneBook()
    contact = []
    contact.append(view.inputStr('Введите имя контакта: '))
    contact.append(view.inputStr('Введите телефон контакта: '))
    contact.append(view.inputStr('Введите комментарий: '))
    phone_book.append(contact)
    print('\nКонтакт добавлен')

def changeContact():
    phone_book = model.getPhoneBook()
    view.showContacts(phone_book, 'Телефонная книга пуста!')
    choice = view.inputStr('Введите номер элемента контакта, который нужно изменить: ')
    print(*phone_book.pop(choice))
    addContact()


def deleteContact():
    phone_book = model.getPhoneBook()
    view.showContacts(phone_book, 'Телефонная книга пуста!')
    choice = view.inputStr('Введите номер элемента контакта, который нужно удалить: ')
    phone_book.pop(choice)


