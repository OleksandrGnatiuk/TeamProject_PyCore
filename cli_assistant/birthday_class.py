from datetime import datetime


class Field():
    pass

class Birthday(Field):

    def __init__(self, value=None):
        self.__private_value = None
        self.value = value

    @property
    def value(self):
        return self.__private_value

    # перевірка коректності дати
    @value.setter
    def value(self, value):
        try:
            if value != None:
                self.__private_value = datetime.strptime(value, '%d/%m/%Y').date()
        except ValueError:
            print (f'Please, input the date in format dd/mm/yyyy ')    


class Record():

    def __init__(self, birthday: Birthday):
        self.birthday = birthday


    def __repr__(self):
        # rec = f'{self.name}, phones: {self.phones}, birthday: {self.birthday.value}'
        rec = f'birthday: {self.birthday.value}'
        return rec

    def days_to_birthday(self, birthday: Birthday):
        
        self.birthday = birthday
        if self.birthday.value:
            try:
                current_date = datetime.now().date()
                user_date = self.birthday.value.replace(year = current_date.year)
                delta_days = user_date - current_date
                    
                if 0 < delta_days.days:
                    return f'Лишилось до Дня народження: {delta_days.days} днів.'
                else:
                    user_date = self.birthday.value.replace(year=user_date.year + 1)
                    delta_days = user_date - current_date
                    if 0 < delta_days.days:
                        return f'Лишилось до Дня народження: {delta_days.days} днів.'
            except ValueError:
                return f'Please, input date in format dd/mm/yyyy '
        else:
            return f'Date of birth is not found. Please, add day of birth, if you want. '



def get_birthdays_per_week(users, range_of_days=7):
    """Аналізує усі контакти. Якщо кількість днів до др <= range_of_days, виводиться на екран."""
    pass 


# Виводить дату народження. Виводить кількість днів до дня народження для контакту.
birth = Birthday()
record = Record(birth)
print(Record.days_to_birthday(Record, birth))
print(Record.__repr__(Record))
