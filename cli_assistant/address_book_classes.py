from collections import UserDict


class Field:

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):

    def __str__(self):
        return self._value.title()


class Phone(Field):

    def __str__(self):
        return self._value.title()


class Email(Field):

    def __str__(self):
        return self._value.title()


class Record:
    def __init__(self, name, email, phone=None, birthday=None):
        self.email = email
        self.name = name
        self.birthday = birthday
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def contacts(self):
        phon = []
        for i in self.phones:
            phon.append(str(i))
            result_phones = ", ".join(phon)
        return f"name: {str(self.name.value)};\n" \
               f"phone: {result_phones};\n" \
               f"e-mail: {str(self.email.value)};\n" \
               f"birthday:{None};\n"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def show_book(self):
        for name, value in self.data.items():
            print(f"{name}\n{value.contacts()}")


if __name__ == "__main__":
    user_1 = Name("User_1")
    user_1_phone = Phone("034-1232-12312-12312")
    user_1_email = Email("user1@gmail.com")
    user_1_rec = Record(user_1, user_1_email, user_1_phone)
    user_1_rec.add_phone("23123-1232-1132")
    user_1_rec.add_phone("23123-12322")
    user_1_rec.add_phone("09721-1132")

    user_2 = Name("User_2")
    user_2_phone = Phone("097123123123")
    user_2_email = Email("user2@gmail.com")
    user_2_rec = Record(user_2, user_2_email, user_2_phone)
    user_2_rec.add_phone("+380231231222")
    user_2_rec.add_phone("+38023132231222")
    user_2_rec.add_phone("+3802312323231222")

    my_book = AddressBook()
    my_book.add_record(user_1_rec)
    my_book.add_record(user_2_rec)
    print(my_book.show_book())
