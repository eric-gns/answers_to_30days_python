print('hello world')
print(len('hello world'))
print(type('hello world'))
print(str(10))
print(int('10'))
print(float(10))
print(input('enter your name:'))

print((lambda x: x + 10)(5))

#more built-in functions
print(min(20,30, 40, 50))
print(max(20,30, 40, 50))
print(min([20,30, 40, 50 ]))
print(max([20,30, 40, 50 ]))
print(sum([20, 30, 40, 50,]))

#variables: use underscore when stitching words together. like: "first_name"

# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)