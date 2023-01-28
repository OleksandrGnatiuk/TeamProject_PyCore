# from address_book_classes import LetterInPhoneError, WrongLengthPhoneError, EmailError


def input_error(func):
    """ Декоратор, що повідомляє про виключення """

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "This record is not exist"
        except ValueError:
            return "This record is not correct!"
        except IndexError:
            return "This command is wrong"
        # except LetterInPhoneError:
        #     return "There is letter in phone number!"
        # except WrongLengthPhoneError:
        #     return "Length of phone's number is wrong!"
        # except EmailError:
        #     return "E-mail is wrong!"
        # except Exception:
        #     return "Mistake"

    return wrapper
