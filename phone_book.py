
# class PhoneBook:
#     phone_book = []
#
#     def getPhoneBook() -> list:
#         global phone_book
#         return phone_book
#
#     def setPhoneBook(new_phone_book: list):
#         global phone_book
#         phone_book = new_phone_book()


class People:
    _name: str
    _age: int = 18

    def __init__(self, name: str):
        self._name = name

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def setName(self, name: str):
        self._name = name

    def setAge(self, age: int):
        self._age = age

    def spy(self):
        self._name = 'Антон'
        self._age = 16



stone = People('Стоун')
andrey = People('Андрей')

print(stone.getAge())
stone.setAge(38)

print(stone.getName())
print(stone.getAge())

stone.spy()

print(andrey)
print(andrey)
