'''
Uppercase letters are 65 -> 65+25
Lowercase letters are 97 -> 97+25
'''


def swap_case(s):
    words_swapped = ''
    for letter in s:
        if ord(letter) < 97:  # must be uppercase
            words_swapped += letter.lower()
        elif ord(letter) >= 97:  # must be Lowercase
            words_swapped += letter.upper()
        else:
            words_swapped += letter
    return words_swapped


print(swap_case('Testing words like Alex and Maggie to see if this workS'))
