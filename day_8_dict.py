
# Level 1: Creating & Modifying Dictionaries
dog = {}
dog['name'] = 'Browny'
dog['color'] = 'Black'
dog['breed'] = 'Askal'
dog['legs'] = 4
dog['age'] = 4

student = { 
    'first_name': 'Mark',
    'last_name': 'Genosa',
    'gender': 'M',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'Cloud_Eng'],
    'country': 'PH',
    'city': 'Cebu',
    'address': 'Kahitsaan'
}

# Modifying nested lists inside dictionaries
student['skills'].append('SQL')
student['skills'].append('Data_Eng')

# Level 2: Dictionary Views, Conversions & Deletion
print(len(student))
print(type(student['skills']))

print(student.keys())
print(student.values())

student_tpl = tuple(student.items())
del student['address']

# Level 3: Deleting Variables Entirely
del dog