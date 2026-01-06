from src.modules.config import *

from random import shuffle, choice

def generate():
    lower_case_letters = []
    for n in range(97, 123):
        lower_case_letters.append(chr(n))

    upper_case_letters = []
    for n in range(65, 91):
        upper_case_letters.append(chr(n))

    numbers = []
    for n in range(48, 58):
        numbers.append(chr(n))

    symbols = []
    for n in range(33, 40):
        symbols.append(chr(n))

    password_list = []
    if UPPERCASE_LETTER:
        password_list.extend(upper_case_letters)

    if LOWERCASE_LETTER:
        password_list.extend(lower_case_letters)

    if NUMBERS:
        password_list.extend(numbers)

    if SYMBOLS:
        password_list.extend(symbols)

    shuffle(password_list)

    new_password = ""
    for _ in range(PASSWORD_LENGTH):
        new_password += choice(password_list)

    return new_password