from collections import UserDict
from datetime import datetime, timedelta
import pickle
from pathlib import Path
import re


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
    @staticmethod
    def validate_phone(phone):
        new_phone = str(phone).strip().replace("+", "").replace(" ", "")
        if not new_phone.isdigit():
            raise ValueError("The phone number should contain only numbers!")
        else:
            if len(new_phone) == 10:
                return f"{new_phone}"
            else:
                raise ValueError("Check the length of the phone number!")

    def __init__(self, value):
        self._value = Phone.validate_phone(value)

    @Field.value.setter
    def value(self, value):
        self._value = Phone.validate_phone(value)


class Email(Field):
    @staticmethod
    def validate_email(email):
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,}$"
        if re.match(pattern, email) is not None:
            return f"{email}"
        else:
            raise ValueError("Email is not correct!")

    def __init__(self, value):
        self._value = Email.validate_email(value)

    @Field.value.setter
    def value(self, value):
        self._value = Email.validate_email(value)


class Address(Field):

    def __str__(self):
        return self._value


class Birthday(Field):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            if value is not None:
                self._value = datetime.strptime(value, '%d/%m/%Y').date()
        except ValueError:
            print(f'Please, input the date in format dd/mm/yyyy ')


class Record:
    def __init__(self, name, phone=None, email=None, birthday=None, address=None):
        self.name = name
        self.birthday = birthday
        self.address = address

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

    """Робота з датою народження"""

    def add_birthday(self, birthday):
        """Adding date of birth"""
        birthday = Birthday(birthday)
        self.birthday = birthday
        print("Date of birth was added")

    def delete_birthday(self, old_birthday):
        """Delete date of birth"""
        old_birthday = Birthday(old_birthday)
        if self.birthday.value == old_birthday.value:
            self.birthday = 'Не вказано'
            print("Date of birth was deleted")
        else:
            print("such a date does not exist")

    def days_to_birthday(self):
        """How many days until user's birthday"""
        if self.birthday.value:
            try:
                birthday_value = datetime.strptime(self.birthday.value, '%d/%m/%Y').date()
                current_date = datetime.now().date()
                user_date = birthday_value.replace(year=current_date.year)
                self.delta_days = user_date - current_date

                if 0 < self.delta_days.days:
                    return f'Лишилось до Дня народження: {self.delta_days.days} днів.'
                else:
                    user_date = birthday_value.replace(year=user_date.year + 1)
                    self.delta_days = user_date - current_date
                    if 0 < self.delta_days.days:
                        return f'Лишилось до Дня народження: {self.delta_days.days} днів.'
            except ValueError:
                return f'Please, input date in format dd/mm/yyyy '
        else:
            return f'Date of birth is not found. Please, add day of birth, if you want. '

    """Робота з адресою"""

    def add_address(self, address):
        address = Address(address)
        self.address = address
        print("Address was added")

    def delete_address(self, old_address):
        old_address = Address(old_address)
        if self.address.value == old_address.value:
            self.address = 'Не вказано'
            print("Address was deleted")
        else:
            print("Such an address does not exist")

    def contacts(self):
        phon = []
        result_phones = ''
        result_emails = ''
        if len(self.phones) > 0:
            for i in self.phones:
                phon.append(str(i))
                result_phones = ", ".join(phon)
        em = []
        if len(self.emails) > 0:
            for i in self.emails:
                em.append(str(i))
                result_emails = ", ".join(em)

        return f"name: {str(self.name.value)};\n" \
               f"phone: {result_phones};\n" \
               f"e-mail: {result_emails};\n" \
               f"birthday: {self.birthday};\n" \
               f"address: {self.address};\n"


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

    def get_birthdays_per_week(self, range_of_days=7):
        """a list of users who have a birthday coming up soon"""
        current_date = datetime.now().date()
        for name, value in self.data.items():
            user_name = name
            user_date = value.birthday.value
            user_date = datetime.strptime(user_date, '%d/%m/%Y').date()
            user_date = user_date.replace(year=current_date.year)
            day_of_week = user_date.weekday()
            delta_days = user_date - current_date

            if 0 < delta_days.days <= range_of_days:
                if day_of_week == 5 or day_of_week == 6:
                    near_birthdays['name0'].append(user_name)
                else:
                    near_birthdays[f"name{day_of_week}"].append(user_name)
            elif 0 < delta_days.days > range_of_days:
                continue
            else:
                user_date = user_date.replace(year=user_date.year + 1)
                delta_days = user_date - current_date
                if 0 < delta_days.days <= range_of_days:
                    if day_of_week == 5 or day_of_week == 6:
                        near_birthdays['name0'].append(user_name)
                    else:
                        near_birthdays[f"name{day_of_week}"].append(user_name)
                elif 0 < delta_days.days > range_of_days:
                    continue
        for i in range(5):
            if not near_birthdays[f"name{i}"]:
                continue
            else:
                print(near_birthdays[f"day{i}"] + ':', ", ".join(near_birthdays[f"name{i}"]))


near_birthdays = {
    'day0': 'Monday', 'name0': [],
    'day1': 'Tuesday', 'name1': [],
    'day2': 'Wednesday', 'name2': [],
    'day3': 'Thurthday', 'name3': [],
    'day4': 'Friday', 'name4': []
}

p = Path("address_book.bin")
address_book = AddressBook()

if p.exists():
    with open("address_book.bin", "rb") as file:
        address_book.data = pickle.load(file)

if __name__ == "__main__":
    user_1 = Name("User_1")
    user_1_phone = Phone("1234567890")
    user_1_email = Email("user1@gmail.com")
    user_1_rec = Record(user_1, user_1_phone, user_1_email)
    user_1_rec.add_phone("0970123546")
    user_1_rec.add_phone("0920193546")
    user_1_rec.add_phone("0970125346")
    user_1_rec.add_email("ar@gmail.com")
    user_1_rec.add_email("arb@gmail.com")
    user_1_rec.add_email("arc@gmail.com")
    user_1_rec.delete_phone("0970123546")
    user_1_rec.delete_email("arb@gmail.com")
    user_1_rec.change_phone("0970123546", "0971111546")

    user_1_rec.add_birthday("31/01/2002")
    user_1_rec.add_address("91502 Elliott Circles.New Janet")

    user_2 = Name("User_2")
    user_2_phone = Phone("0979123546")
    user_2_email = Email("user2@gmail.com")
    user_2_rec = Record(user_2, user_2_phone, user_2_email)
    user_2_rec.add_phone("0900123546")
    user_2_rec.add_phone("+0970111146")
    user_2_rec.add_phone("+0970120000")

    user_2_rec.add_birthday("26/03/2002")
    user_2_rec.delete_birthday("26/03/2002")
    user_2_rec.add_birthday("29/01/2002")
    print(user_2_rec.days_to_birthday())

    my_book = AddressBook()
    my_book.add_record(user_1_rec)
    my_book.add_record(user_2_rec)
    my_book.get_birthdays_per_week()
    user_2_rec.add_address("821 Nader Island Suite 403.Port Conorshire")
    print(my_book.show_book())
    user_2_rec.delete_address("821 Nader Island Suite 403.Port Conorshire")
    # my_book.del_record("User_1")
    print(my_book.show_book())
