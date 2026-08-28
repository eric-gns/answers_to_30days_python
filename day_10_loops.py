# Level 1: Counting & Patterns
# While Loop (0 to 10)
x = 0
while x <= 10:
    print(x)
    x += 1

# For Loop (0 to 10)
for x in range(11):
    print(x)

# Countdown (10 down to 0)
for x in range(10, -1, -1):
    print(x)

# Triangle Pattern
y = 1
while y <= 7:
    print('#' * y)
    y += 1

# Level 2: Grid & Multiplication Table
# 8x8 Grid
y = 0
while y < 8:
    print('#' * 8)
    y += 1

# Multiplication Table
for x in range(0, 11):
    print(f'{x} x {x} = {x * x}')

# Level 3: Filtering & Accumulation
skills = ['Python', 'SQL', 'Git', 'Data_Eng', 'Cloud_Eng', 'Linux', 'Docker']

for skill in skills:
    if 'Linux' in skill:
        break
    elif 'Eng' in skill:
        print(skill)

even_total = 0
odd_total = 0

for x in range(0, 101):
    if x % 2 == 0:
        even_total += x
    elif x % 2 == 1:
        odd_total += x

print("Sum of evens:", even_total)
print("Sum of odds:", odd_total)