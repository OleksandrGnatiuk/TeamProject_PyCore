from .address_book_classes import EmailError, WrongLengthPhoneError, LetterInPhoneError


class SoundNoteError(Exception):
    pass

class TaskFormatError(Exception):
    pass


def input_error(func):
    """ Декоратор, що повідомляє про виключення """

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "\nThis record is not exist\n"
        except ValueError:
            return "\nThis record is not correct!\n"
        except IndexError:
            return "\nThis command is wrong\n"
        except LetterInPhoneError:
            return "\nThere is letter in phone number!\n"
        except WrongLengthPhoneError:
            return "\nLength of phone's number is wrong!\n"
        except EmailError:
            return "\nE-mail is wrong\n!"
        except SoundNoteError:
            return "\nSound is not available\n!"
        except TaskFormatError:
            return f"\nPlease white command in format 'add task <name> <deadline in format: d/m/yyyy> <task>'\n"
        except Exception:
            return "\nMistake\n"

    return wrapper
