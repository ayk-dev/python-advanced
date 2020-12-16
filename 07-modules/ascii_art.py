from pyfiglet import figlet_format


def print_art_message(string):
    art_msg = figlet_format(string)
    print(art_msg)


text = input()
print_art_message(text)