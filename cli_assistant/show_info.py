from abc import abstractmethod, ABC
import pyttsx3
from .address_book_classes import *
from .note_book_classes import *
from .task_list_classes import *


class Info(ABC):

    @abstractmethod
    def get_info(self, data):
        pass


class ContactInfo(Info):
    """ Клас виводить інформацію по імені, або телефону контакту """

    def get_info(self, text_to_search: str):
        text_to_search = text_to_search.strip()
        if text_to_search[0].isalpha():
            name = text_to_search.title()
            if name and name.title() in address_book:
                record = address_book[name.title()]
                return record.contacts()
            else:
                return f"\nContact {name.title()} does not exist.\n"

        elif text_to_search[0].isdigit() or text_to_search[0] in ("+", "(") and text_to_search[1].isdigit():
            phone = Phone.validate_phone(text_to_search)
            for record in address_book.values():
                lst = [phone.value for phone in record.phones]
                if phone in lst:
                    return record.contacts()
                else:
                    return f"\nContact with phone number {text_to_search} does not exist.\n"



class AddressBookInfo(Info):
    """ Клас виводить всі записи книги контактів """

    def get_info(self, data):
        if len(address_book) == 0:
            return "\nPhone book is empty.\n"
        else:
            result = "\n"
            for name, value in address_book.data.items():
                s = f"{name}\n{value.contacts()}\n"
                result += s
            return result


class NoteInfo(Info):
    """ Клас виводить та озвучує нотатку по ії ID"""
    def get_info(self, id):
        try:
            s = pyttsx3.init()
            text_to_speach = nb.notes[int(id)].note
            s.say(text_to_speach)
            s.runAndWait()
        except Exception:
            "sound is not available"
        finally:
            return nb.show_note(id)


class NotebookInfo(Info):
    def get_info(self, data):
        if len(nb.notes) > 0:
            result = "\n"
            for id_, rec in nb.notes.items():
                tgs = [tg.word.lower() for tg in rec.tags]
                tags = ", ".join(tgs)
                date = rec.date
                result += f"\nid: {id_}      date: {date} \n{rec.note}\ntags: {tags} \n=========\n"
            return result
        else:
            return f"\nNotebook is empty.\n"


class TaskbookInfo(Info):
    def get_info(self, data):
        result = '\n'
        if len(tasklist.task_lst) > 0:
            for k, v in tasklist.task_lst.items():
                result += f"=== ID: {k} === {v.see_task()}\n"
            return result
        else:
            return f"\nTask book is empty.\n"