from assistant import main
from show_info import ShortHelpInfo


def short_help():
    print(ShortHelpInfo.get_info("info"))
    return main()


if __name__ == "__main__":
    short_help()
