# ==========================================
# DAY 17: EXCEPTION HANDLING & CUSTOM ERRORS
# ==========================================

# ------------------------------------------
# EXERCISE 1: Safe Division with try / except / else / finally
# ------------------------------------------
def safe_divide(a, b):
    """
    Demonstrates handling built-in errors (ZeroDivisionError & TypeError)
    using the full try / except / else / finally flow.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Both inputs must be numeric!")
    else:
        print(f"Success! Result: {result}")
    finally:
        print("Division operation complete.\n")


# ------------------------------------------
# EXERCISE 2: Domain Validation with `raise` and `as e`
# ------------------------------------------
def withdraw(balance, amount):
    """
    Validates account operations by raising custom ValueErrors
    for invalid amounts or insufficient funds.
    """
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero!")
    elif amount > balance:
        raise ValueError("Insufficient Funds!")
    else:
        new_balance = balance - amount
        return new_balance


# ==========================================
# SCRIPT EXECUTION & TESTS
# ==========================================
if __name__ == "__main__":
    print("=== DAY 17: EXCEPTION HANDLING RECAP ===\n")

    print("--- Test 1: Catching Built-in Errors ---")
    safe_divide(10, 2)    # Valid division
    safe_divide(10, 0)    # Triggers ZeroDivisionError
    safe_divide(10, "2")  # Triggers TypeError

    print("--- Test 2: Custom Exception Handling (withdraw) ---")
    
    # Test Case A: Valid withdrawal
    try:
        updated_balance = withdraw(100, 30)
        print(f"Updated balance: ${updated_balance}")
    except ValueError as e:
        print(f"Error caught: {e}")

    # Test Case B: Overdraft attempt (triggers custom raise)
    try:
        updated_balance = withdraw(100, 150)
        print(f"Updated balance: ${updated_balance}")
    except ValueError as e:
        print(f"Error caught: {e}")

    # Test Case C: Non-positive withdrawal attempt
    try:
        updated_balance = withdraw(100, -10)
        print(f"Updated balance: ${updated_balance}")
    except ValueError as e:
        print(f"Error caught: {e}")