# ==========================================
# DAY 16: PYTHON DATETIME MODULE
# ==========================================
from datetime import datetime, timedelta

# ------------------------------------------
# EXERCISE 1: Extracting Current Date Components
# ------------------------------------------
def extract_date_components():
    """Retrieves current time and extracts individual components."""
    now = datetime.now()
    print("Current day: ", now.day)
    print("Current month: ", now.month)
    print("Current year: ", now.year)
    print("Current hour: ", now.hour)
    print("Current minute: ", now.minute)
    print("Current timestamp: ", now.timestamp())


# ------------------------------------------
# EXERCISE 2: Formatting Dates (strftime)
# ------------------------------------------
def format_dates():
    """Formats datetime objects into custom EU and US string formats."""
    now = datetime.now()
    
    # European Format: Day/Month/Year Hours:Minutes:Seconds (24-hour)
    formatted_eu = now.strftime("%d/%m/%Y %H:%M:%S")
    print("European time format: ", formatted_eu)

    # US Format: Month Name Day, Year - Hours:Minutes AM/PM (12-hour)
    formatted_us = now.strftime("%B %d, %Y - %I:%M %p")
    print("US time format: ", formatted_us)


# ------------------------------------------
# EXERCISE 3: Parsing Strings into Dates (strptime)
# ------------------------------------------
def parse_date_string():
    """Parses a formatted date string into a structured datetime object."""
    date_string = "5 December, 2019"
    pattern = "%d %B, %Y"

    date_obj = datetime.strptime(date_string, pattern)
    print("Type of parsed object:", type(date_obj))
    print("Extracted year:", date_obj.year)


# ------------------------------------------
# EXERCISE 4: Time Differences & Future Dates (timedelta)
# ------------------------------------------
def calculate_time_differences():
    """Calculates countdown durations and future target dates using timedelta."""
    now = datetime.now()
    
    # New Year Countdown
    next_yr = datetime(2027, 1, 1)
    countdown = next_yr - now
    print("Full countdown object:", countdown)
    print("Days until 2027:", countdown.days)

    # Future Date Calculation (80 days from now)
    future_80 = now + timedelta(days=80)
    print("Date 80 days from now:", future_80)


# ==========================================
# SCRIPT EXECUTION & TESTS
# ==========================================
if __name__ == "__main__":
    print("=== DAY 16: DATETIME MODULE RECAP ===\n")

    print("--- Exercise 1: Extracting Components ---")
    extract_date_components()
    print()

    print("--- Exercise 2: Formatting Dates ---")
    format_dates()
    print()

    print("--- Exercise 3: Parsing Date Strings ---")
    parse_date_string()
    print()

    print("--- Exercise 4: Time Differences & Timedelta ---")
    calculate_time_differences()