# =====================================================================
# DAY 12: YOUR COMPLETED EXERCISES & MODULES PRACTICE
# =====================================================================

import random
import string

# ---------------------------------------------------------------------
# LEVEL 1: USER ID & COLOR GENERATION
# ---------------------------------------------------------------------

def user_id_gen_by_user():
    """Generates a user-specified number of IDs with custom length from console input."""
    char_num = int(input('Enter number of characters: '))
    id_num = int(input('Enter number of IDs: '))
    characters = string.ascii_letters + string.digits
    for i in range(0, id_num):
        rndm_char = random.choices(characters, k=char_num)
        user_id = "".join(rndm_char)
        print(user_id)


def rgb_color_gen():
    """Generates a single random RGB color string formatted as 'rgb(R, G, B)'."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"


# ---------------------------------------------------------------------
# LEVEL 2: COLOR ROUTING, LIST SHUFFLE & RANDOM DIGITS
# ---------------------------------------------------------------------

def list_of_hexa_colors(num):
    """Generates a list of random 6-character hexadecimal color codes with '#' prefix."""
    characters = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
    colors = []
    for i in range(0, num):
        rndm_hexa_color = random.choices(characters, k=6)
        hexa_color = "#" + ''.join(rndm_hexa_color)
        colors.append(hexa_color)    
    return colors


def generate_colors(num, type_of_color):
    """Routes color generation depending on type: 'hexa' or 'rgb'."""
    if type_of_color == 'hexa':
        characters = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
        colors = []
        for i in range(0, num):
            rndm_hexa_color = random.choices(characters, k=6)
            hexa_color = "#" + ''.join(rndm_hexa_color)
            colors.append(hexa_color)    
        return colors
    elif type_of_color == 'rgb':
        rgb_colors = []
        for i in range(0, num):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            rndm_rgb = f"rgb({r}, {g}, {b})"
            rgb_colors.append(rndm_rgb)
        return rgb_colors


def shuffle_list(lst):
    """Returns a shuffled copy of a list using random.shuffle() while preserving original."""
    copy_list = lst.copy()
    random.shuffle(copy_list)
    return copy_list


def arrayOfRndmNums():
    """Returns a list of 7 unique random digits in the range 0-9 using random.sample()."""
    array_rndm = random.sample(range(0, 10), 7)
    return array_rndm


# ---------------------------------------------------------------------
# LEVEL 3: CUSTOM ALGORITHMS & UNIQUE ID LISTS
# ---------------------------------------------------------------------

def custom_shuffle(lst):
    """Manually shuffles a list using .pop() and random.randint() without random.shuffle()."""
    copy = lst.copy()
    shuffled = []
    while len(copy) != 0:    
        shuffled.append(copy.pop(random.randint(0, len(copy) - 1)))
    return shuffled


def seven_random_ids():
    """Generates and returns a list of 7 unique 6-character IDs (alphanumeric)."""
    characters = string.ascii_letters + string.digits
    rndm_ids = []
    while len(rndm_ids) < 7:
        rndm_char = random.choices(characters, k=6)
        new_id = "".join(rndm_char)
        if new_id not in rndm_ids:
            rndm_ids.append(new_id)
    return rndm_ids


# =====================================================================
# REFERENCE: COMMON PYTHON STANDARD LIBRARY MODULES
# =====================================================================
# 1. DATA & MATH:
#    - random    : Choice, sampling, shuffle, pseudorandom generation
#    - math      : Advanced mathematical functions (sqrt, ceil, floor, pi, sin)
#    - statistics: Mean, median, mode, variance, stdev
#    - decimal   : Precision floating-point arithmetic
#
# 2. STRINGS & TEXT:
#    - string    : Constants like ascii_letters, digits, punctuation
#    - re        : Regular expression pattern matching and search
#
# 3. SYSTEM & FILES:
#    - os        : Operating system interactions (file navigation, directories)
#    - sys       : System-specific parameters and CLI argument handling
#    - pathlib   : Object-oriented filesystem path operations
#
# 4. DATE & TIME:
#    - datetime  : Date and time parsing, formatting, calculations
#    - time      : System time access, delays (time.sleep)
#
# 5. DATA FORMATS & UTILITIES:
#    - json      : Encoding and decoding JSON data
#    - csv       : Reading/writing CSV spreadsheets
#    - itertools : High-performance tools for iteration and combinations
# =====================================================================