# Level 1 - Exercise 1: Driving Age Check
x = int(input('Enter age: '))
remaining = 18 - x

if x >= 18:
    print('you are old enough to drive')
else:
    print(f'you need {remaining} more years to drive')

# Level 1 - Exercise 2: Age Comparison
my_age = 20
your_age = int(input('Enter your age: '))

if my_age > your_age:
    diff = my_age - your_age
    print(f'i am {diff} year/s older than you!')
elif your_age > my_age:
    diff2 = your_age - my_age
    print(f'you are {diff2} year/s older than me!')
else:
    print('we are the same age!')

# Level 2: Grade Calculator
grade = int(input('enter your grades: '))

if grade >= 80:
    print('you got an A!')
elif grade >= 70:
    print('you got a B!')
elif grade >= 60:
    print('you got a c!')
elif grade >= 50:
    print('you got a D!')
else:
    print('you got an F!')

# Level 3: Seasonal Checker
month = input('enter month: ').title()

Autumn = ('September', 'October', 'November')
Winter = ('December', 'January', 'February')
Spring = ('March', 'April', 'May')
Summer = ('June', 'July', 'August')

if month in Autumn:
    print('It is Autumn Season!')
elif month in Winter:
    print('It is Winter Season!')
elif month in Spring: 
    print('It is Spring Season!')
elif month in Summer: 
    print('It is Summer Season!')
else:
    print('invalid month')