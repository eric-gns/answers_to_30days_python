# ==========================================
# DAY 15: PYTHON EXCEPTION HANDLING
# ==========================================


# ------------------------------------------
# EXERCISE 1: Handling ValueError & Conversion
# ------------------------------------------
def get_user_age():
    """Prompts for input, converts it to an integer, and handles ValueError."""
    try:
        user_input = input('Enter age: ')
        age = int(user_input)
        return age
    except ValueError:
        print('Error: Enter a valid numeric age!')


# ------------------------------------------
# EXERCISE 2: Handling KeyError in Dictionaries
# ------------------------------------------
def get_user_info(user_dict, key):
    """Safely retrieves a dictionary key, catching KeyError if missing."""
    try:
        return user_dict[key]
    except KeyError:
        print(f"Key '{key}' does not exist!")
        return False


# ------------------------------------------
# EXERCISE 3: Handling Multiple Exception Types
# ------------------------------------------
def safe_divide_elements(items, index, divisor):
    """Performs element lookup and division, catching grouped exceptions."""
    try:
        result = items[index] / divisor
        return result
    except (IndexError, ZeroDivisionError):
        print('Index is out of bounds or division by zero!')


# ------------------------------------------
# EXERCISE 4: Full Lifecycle (try, except, else, finally)
# ------------------------------------------
def parse_and_log(value):
    """Demonstrates complete flow using try, except, else, and finally."""
    try:
        result = int(value)
    except ValueError:
        print('Failed to parse value into an integer!')
    else:
        print(f'The parsed value is {result}.')
    finally:
        print('Enter another value')


# ==========================================
# SCRIPT EXECUTION & TESTS
# ==========================================
if __name__ == "__main__":
    print("=== DAY 15: EXCEPTION HANDLING RECAP ===\n")

    # --- Test Exercise 1 ---
    print("--- Exercise 1: get_user_age ---")
    age_result = get_user_age()
    print('Returned Result:', age_result)
    print()

    # --- Test Exercise 2 ---
    print("--- Exercise 2: get_user_info ---")
    user_record = {'name': 'Mark', 'role': 'Admin'}
    print("Lookup 'name':", get_user_info(user_record, 'name'))
    print("Lookup 'email':", get_user_info(user_record, 'email'))
    print()

    # --- Test Exercise 3 ---
    print("--- Exercise 3: safe_divide_elements ---")
    numbers = [10, 20, 30]
    print("Valid Division (index 1 / 2):", safe_divide_elements(numbers, 1, 2))
    print("Out of Bounds (index 5 / 2):", safe_divide_elements(numbers, 5, 2))
    print("Zero Division (index 1 / 0):", safe_divide_elements(numbers, 1, 0))
    print()

    # --- Test Exercise 4 ---
    print("--- Exercise 4: parse_and_log ---")
    print("[Test 1: Valid Input]")
    parse_and_log("42")
    print("\n[Test 2: Invalid Input]")
    parse_and_log("abc")