'''
Take a string and change the Nth character
This wasn't working before because I ran it with Python 2 which seems to
not work with input instead of raw_input
'''


def change_string_char():
    # example of input 5
    string = input("enter a string to change: ")
    position = int(input("enter the position to change: "))
    character = input("enter the replacement character: ")
    string_list = list(string)
    string_list[position] = character
    return "".join(string_list)


# print(change_string_char('Alexander', 5, 'd'))
print(change_string_char())
