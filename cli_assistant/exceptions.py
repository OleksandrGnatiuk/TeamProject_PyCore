from address_book_classes import EmailError, WrongLengthPhoneError, LetterInPhoneError
from functools import wraps
from logger_ import get_logger


class SoundNoteError(Exception):
    pass

class TaskFormatError(Exception):
    pass


logger = get_logger(__name__)

def input_error(func):
    """ Декоратор, що повідомляє про виключення """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError as key_err:
            logger.error(f'[ERROR]: {key_err}')
            return "\nThis record is not exist\n"
        except ValueError as key_err:
            logger.error(f'[ERROR]: {key_err}')
            return "\nThis record is not correct!\n"
        except IndexError as key_err:
            logger.error(f'[ERROR]: {key_err}')
            return "\nThis command is wrong\n"
        except LetterInPhoneError as key_err:
            logger.error(f'[ERROR]: {key_err}')
            return "\nThere is letter in phone number!\n"
        except WrongLengthPhoneError as key_err:
            logger.error(f'[ERROR]: {key_err}')
            return "\nLength of phone's number is wrong!\n"
        except EmailError as key_err:
            logger.error(f'[ERROR]: {key_err}')
            return "\nE-mail is wrong!\n"
        except SoundNoteError as key_err:
            logger.error(f'[ERROR]: {key_err}')
            return "\nSound is not available\n!"
        except TaskFormatError as key_err:
            logger.error(f'[ERROR]: {key_err}')
            return f"\nPlease white command in format 'add task <name> <deadline in format: d/m/yyyy> <task>'\n"
        except Exception as key_err:
            logger.error(f'[ERROR]: {key_err}')
            return "\nMistake\n"

    return wrapper
