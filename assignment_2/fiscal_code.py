import random as rng
import string
from date import Date

lowercase_vocals = ['a', 'e', 'i', 'o', 'u']
lowercase_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
                        'y', 'z']

uppercase_vocals = [str.upper(l_vocal) for l_vocal in lowercase_vocals]
uppercase_consonants = [str.upper(l_consonant) for l_consonant in lowercase_consonants]

month_mapping = {1: 'A',
                 2: 'B',
                 3: 'C',
                 4: 'D',
                 5: 'E',
                 6: 'H',
                 7: 'L',
                 8: 'M',
                 9: 'P',
                 10: 'R',
                 11: 'S',
                 12: 'T'}


# ------------------------------------------

def remove_vocals(s: str) -> str:
    buffer = ""
    for c in s:
        if c not in lowercase_vocals and c not in uppercase_vocals:
            buffer += c

    return buffer


def remove_consonants(s: str) -> str:
    buffer = ""
    for c in s:
        if c in lowercase_vocals and c in uppercase_vocals:
            buffer += c

    return buffer


def generate_fcode(person, bday : Date) -> str:
    """
    Generates the Fiscal Code of a person whose name, gender and birth date is already set
    :param p: Has to be a Person Type, static type restriction wasn't done to avoid cyclic importing
    :return: Fiscal code of the person
    """
    # In our model, the name is a single word
    first_name = person.first_name.replace(" ", "")
    # Last names can have more than one word
    last_name = person.last_name

    # Remove vocals, capitalize and pad with Xs if necessary
    name_vocals = remove_consonants(first_name).capitalize()
    name_consonants = remove_vocals(first_name).upper()

    # Exception for names with more than 4 consonants (the 2nd is skipped)
    if len(name_consonants) >= 4:
        name_consonants = name_consonants[0] + name_consonants[2:]

    # Copy
    f_name_code = str(name_consonants)[0:3]

    if len(f_name_code) < 3:
        missing = 3 - len(f_name_code)
        available = min(missing, len(name_vocals))
        voc_extraction = name_vocals[0:available]
        # If name is less than 3 letters, it's padded with X
        missing = 3 - len(f_name_code)
        f_name_code += ('X' * missing)

    # Remove vocals, capitalize and pad with Xs if necessary
    surname_vocals = remove_consonants(last_name).upper()
    surname_consonants = remove_vocals(last_name).upper()

    f_surname_code = str(surname_consonants)[0:3]

    if len(f_surname_code) < 3:
        missing = 3 - len(f_surname_code)
        available = min(missing, len(surname_vocals))
        voc_extraction = surname_vocals[0:available]
        # If name is less than 3 letters, it's padded with X
        missing = 3 - len(f_surname_code)
        f_surname_code += ('X' * missing)

    year_code = str(bday.year)[-2:]
    month_code = month_mapping[bday.month]
    day_code = '{:02d}'.format(bday.day + (40 if person.gender == 'F' else 0))

    digits_code = [rng.choice(string.digits) for i in range(3)]
    city_code = rng.choice(string.ascii_uppercase)

    for digit in digits_code:
        city_code += digit

    control_code = rng.choice(string.ascii_uppercase)

    return f_surname_code + f_name_code + year_code + month_code + day_code + city_code + control_code
