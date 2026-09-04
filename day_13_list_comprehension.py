# Day 13: Exercises (List Comprehension & Lambda Functions)

# Exercise 1: Filter positive numbers
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_numbers = [num for num in numbers if num > 0]

# Exercise 2: Flatten a 3-level nested list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = [num for outer in list_of_lists for middle in outer for num in middle]

# Exercise 3: Generate power tuples table
patterned_tuples = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]

# Exercise 4: Flatten tuples into uppercase strings
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_countries = [item.upper() for outer in countries for middle in outer for item in middle]

# Exercise 5: Transform nested tuples into a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_city_dict = [
    {'country': country.upper(), 'city': city.upper()} 
    for outer in countries 
    for middle in outer 
    for country, city in middle
]

# Exercise 6: Join nested name tuples into full name strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Gund')]]
formatted_names = [
    f"{first_name} {last_name}" 
    for outer in names 
    for middle in outer 
    for first_name, last_name in middle
]

# Exercise 7: Linear function lambda (y = mx + c)
linear_function = lambda m, x, c: m * x + c