from .assistant import main


def short_help():
    commands = """
    You can use commands:
      - help - hello - good bye - close - .
      - currency
      - clean-folder  
    ADDRESS BOOK:
      - show addressbook - search contacts - phone
      - add contact - remove contact - add phone - change phone - remove phone 
      - add email - change email - remove email - add address - change address - remove address
      - add birthday - remove birthday - change birthday - days to birthday - birthdays
    NOTES BOOK:
      - show notes - note - search notes - search tags
      - add note - change note - add tags - remove note, 
    TASK BOOK:            
      - show tasks - search tasks - responsible person
      - add task - remove task - change deadline - done
      """

    print(commands)
    return main()
