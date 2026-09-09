# ==========================================
# DAY 19: FILE HANDLING (open, with, modes)
# ==========================================

# Exercise 1: Writing to a File ('w' mode)
# Creates 'notes.txt' and writes the initial content
with open("notes.txt", 'w') as f:
    f.write('Learning Python File Handling!')


# Exercise 2: Appending ('a' mode) and Reading Line-by-Line ('r' mode)
# Appends a new line without overwriting
with open('notes.txt', 'a') as f:
    f.write("\nDay 19 is going great!")

# Reads line-by-line using 'end=''' to prevent double newlines
print("--- Reading notes.txt line by line ---")
with open('notes.txt', 'r') as f:
    for line in f:
        print(line, end='')
print("\n")


# Exercise 3: Robust File Reader with Exception Handling
def read_user_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f'The file: {filename} is not found!')


# Testing read_user_file function
print("--- Testing read_user_file() ---")
print(read_user_file("notes.txt"))
read_user_file("missing_file.txt")