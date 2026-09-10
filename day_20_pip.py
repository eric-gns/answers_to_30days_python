import requests

response = requests.get("https://api.github.com")
data = response.json()
print("Status Code:", response.status_code)
print("Response:", data['emojis_url'])
# ==========================================
# DAY 20: MODULES & PACKAGE MANAGEMENT (pip)
# ==========================================

# 1. Built-in Modules
import random as rndm
from datetime import datetime

languages = ["Python", "JavaScript", "C++", "Java", "Rust"]
print("Random Choice:", rndm.choice(languages))
print("Current Timestamp:", datetime.now())


# 2. Custom Modules
# (Assuming sample_file_for_pip.py exists in the same directory)
import sample_file_for_pip

text_result = sample_file_for_pip.capitalize_words("hello python learner")
print("Custom Module Output:", text_result)


# 3. External Package Integration (requests)
import requests

response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("Emojis API URL:", data["emojis_url"])