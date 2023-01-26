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
    def __init__(self, name, phone, email=None, birthday=None):
        self.name = name
        self.birthday = birthday

        self.emails = []
        if email:
            self.emails.append(email)

        self.phones = []
        if phone:
            self.phones.append(phone)

    """Робота з phone"""
    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)
        print("Phone was added")

    def change_phone(self, old_phone, new_phone):
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        for phone in self.phones:
            if phone.value == old_phone.value:
                phone.value = new_phone.value
                print("phone was changed")

    def delete_phone(self, old_phone):
        old_phone = Phone(old_phone)
        for phone in self.phones:
            if phone.value == old_phone.value:
                self.phones.remove(phone)
                print("Phone was deleted ")

    """Робота з e-mail"""
    def add_email(self, email):
        email = Email(email)
        self.emails.append(email)
        print("Email was added")

    def change_email(self, old_email, new_email):
        old_email = Email(old_email)
        new_email = Email(new_email)
        for email in self.emails:
            if email.value == old_email.value:
                email.value = new_email.value
                print("Email was changed")

    def delete_email(self, old_email):
        old_email = Email(old_email)
        for email in self.emails:
            if email.value == old_email.value:
                self.emails.remove(email)
                print("Email was deleted")

    def contacts(self):
        phon = []
        for i in self.phones:
            phon.append(str(i))
            result_phones = ", ".join(phon)
        em = []
        for i in self.emails:
            em.append(str(i))
            result_emails = ", ".join(em)
        return f"name: {str(self.name.value)};\n" \
               f"phone: {result_phones};\n" \
               f"e-mail: {result_emails};\n" \
               f"birthday:{None};\n"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def show_book(self):
        result = ""
        for name, value in self.data.items():
            s = f"{name}\n{value.contacts()}\n"
            result += s
        return result

    def del_record(self, name):
        self.data.pop(name)
        print("Record was deleted")


if __name__ == "__main__":
    user_1 = Name("User_1")
    user_1_phone = Phone("034-1232-12312-12312")
    user_1_email = Email("user1@gmail.com")
    user_1_rec = Record(user_1,user_1_phone ,user_1_email )
    user_1_rec.add_phone("23123-1232-1132")
    user_1_rec.add_phone("23123-12322")
    user_1_rec.add_phone("09721-1132")
    user_1_rec.add_email("ar@gmail.com")
    user_1_rec.add_email("arb@gmail.com")
    user_1_rec.add_email("arc@gmail.com")
    user_1_rec.delete_phone("23123-1232-1132")
    user_1_rec.delete_email("arb@gmail.com")
    user_1_rec.change_phone("23123-1232-1132", "111111111111111")

    user_2 = Name("User_2")
    user_2_phone = Phone("097123123123")
    user_2_email = Email("user2@gmail.com")
    user_2_rec = Record(user_2,user_2_phone ,user_2_email )
    user_2_rec.add_phone("+380231231222")
    user_2_rec.add_phone("+38023132231222")
    user_2_rec.add_phone("+3802312323231222")

    my_book = AddressBook()
    my_book.add_record(user_1_rec)
    my_book.add_record(user_2_rec)
    #my_book.del_record("User_1")
    print(my_book.show_book())
