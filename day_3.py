a = 3
b = 2

total = a + b
diff = a - b
product = a * b
division = a % b
floor_division = a // b
exponential = a ** b



print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)



#exercise!!!

age = 20 
heights = 5.7 #inches
comp = 5j

base = input('Enter base:')
base = float(base)
height = input('Enter height:')
height = float(height)
print('The area of the traingle is:', (base * height) * 0.5)

side_a = input('Enter side a:')
side_b = input('Enter side b:')
side_c = input('Enter side c:')
side_a = float(side_a)
side_b = float(side_b)
side_c = float(side_c)
print('The perimeter of the triangle is:', side_a + side_b + side_c)

length = input('Enter length:')
width = input('Enter width:')
length = float(length)
width = float (width)
area = length * width
perimeter = 2 * (length + width)
print('Area of rectangle is:', area)
print('perimeter of rectangle is:', perimeter)

radius = input('Enter radius:')
radius = float(radius)
pi = 3.14
area = pi* radius * radius
circumference = 2 * pi * radius
print('area is:', area)
print('circumference is:', circumference)


b = input('enter b:')
m = input('enter m:')
b = float(b)
m = float(m)
x = -(b/m)
print(x)
y = m * (x + b)

#skipped task 10

#this is task 11

f = input('enter f:')

xyz = f ** 2 + 6 * f + 9



#12

p = len('python')
d = len('dragon')
print('python and dragon have same length:', p == d)

print('b in python and dragon ', 'b' in 'python' and 'dragon')

float(len('python'))
str(float(len('python')))

if len('python') % 2 == 0:
    print('the number is even')

floor_division = 7 // 3
float(floor_division)
print('floor division of 7 // 3 is:', floor_division)

print(type('10') == type(10))

print(int(9.8) == 10)

hours = input('Enter hours:')
rate = input('Enter rate per hour:')
hours = float(hours)
rate = float(rate)

earnings = hours * rate
print('Your earnings is:', earnings)

lived_years = input('Enter lived years:')
lived_years = float(lived_years)
seconds = lived_years * 365 * 24 * 60 * 60
print('You lived for', seconds, 'seconds')

for i in range(1, 6):
    print(i, '1', i, i * i, i ** 3)


