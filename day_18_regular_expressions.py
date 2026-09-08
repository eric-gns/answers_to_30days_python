import re

# ==========================================
# DAY 18: REGULAR EXPRESSIONS (re module)
# ==========================================

# 1. re.findall() - Extracting price patterns
txt = "Apple is $2, Banana is $5, and Cherry is $12"
all_prices = re.findall(r'\$\d+', txt)
print("Prices found:", all_prices)

# 2. re.findall() - Extracting lowercase words
description = "The python 3.11 release introduced better error messages and speed."
lower_words = re.findall(r'\b[a-z]\w+', description)
print("Lowercase words:", lower_words)

# 3. re.sub() - Data cleaning (stripping HTML tags)
dirty_text = "<h1>Welcome to Python!</h1> <p>Regex is powerful.</p>"
clean_text = re.sub(r'<[^>]+>', '', dirty_text)
print("Clean text:", clean_text)

# 4. re.search() - Validating username format with anchors (^ and $)
def is_valid_username(username):
    # Starts with a letter, followed by 2-9 word chars (total length 3-10)
    return bool(re.search(r'^[a-zA-Z]\w{2,9}$', username))

print("Is 'user_1111' valid?", is_valid_username("user_1111"))

# 5. re.search() with Capturing Groups () - Extracting email domains
emails = ["user1@gmail.com", "admin@company.org", "support@site.net"]

print("\nExtracted Domains:")
for email in emails:
    match = re.search(r'@([a-zA-Z0-9.-]+)', email)
    if match:
        print(f"- {match.group(1)}")