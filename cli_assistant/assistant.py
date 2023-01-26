
def hello(value):
    pass


def say_goodbye():
    pass


def add_cntct(value):
    pass


handlers = {
    "hello": hello,
    "add contact": add_cntct,
}


def main():
    while True:
        command = input("Enter command: ")
        command = command.strip().lower()
        if command in ("exit", "close", "good bye", "."):
            say_goodbye()
            break
        else:
            for key in handlers:
                if key in command:
                    print(handlers[key](command[len(key):].strip()))
                    break





if __name__ == "__main__":
    main()