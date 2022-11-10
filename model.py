

path = '/Users/diananorva/Desktop/phone/phone.txt'
phone_book = []

def getPath():
    global path
    return path

def setPath(new_path: str):
    global path
    path = new_path

def getPhoneBook() -> list:
    global phone_book
    return phone_book

def setPhoneBook(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book