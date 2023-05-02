import random

class NoOptionSelected(Exception):
    pass

class NotEnoughCharacters(Exception):
    pass

def generate_password(length:int,has_symbols : bool,has_numbers:bool,has_lowercase:bool,has_uppercase:bool,has_repeated_char:bool,has_ambiguous_char:bool):
    symbols = "!@#$%^&*=?+-|_"
    numbers = "1234567890"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()
    ambiguous = "}{][()/'\`~,;:.<>"

    selected_chars = ""
    if has_symbols:
        selected_chars += symbols
    
    if has_numbers:
        selected_chars += numbers

    if has_lowercase:
        selected_chars += lowercase

    if has_uppercase:
        selected_chars += uppercase

    if has_ambiguous_char:
        selected_chars += ambiguous

    if len(selected_chars) == 0:
        raise NoOptionSelected

    password = ""
    for i in range(length):
        try:
            rnd = random.choice(selected_chars) 
            if has_repeated_char:
                password += rnd
                selected_chars =  selected_chars.replace(rnd,"")
            else:
                password += rnd
        except:
            print("Please select more options or lower password length..")
            raise NotEnoughCharacters

    
    return password
            