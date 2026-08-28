# I ALREADY DID THE EXERCISE IN MY GEMINI GEM
# IT WAS SUPRISINGLY ACCURATE


# 1. Creating and joining tuples (Level 1)
brothers = ('John', 'Dave')
sisters = ('Anna', 'Mary')
siblings = brothers + sisters
print("Number of siblings:", len(siblings))

# 2. Modifying tuple via list conversion workaround
family_members = list(siblings)
family_members.append('Father')
family_members.append('Mother')
family_members = tuple(family_members)

# 3. Tuple Unpacking (Level 2)
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
*nordic, es, ru = nordic_countries

# 4. Slicing sequences (First 3 and Last 3 items)
food_stuff_lt = ['banana', 'orange', 'mango', 'lemon', 'Carrot', 'Tomato', 'Cabbage', 'Onion', 'Carrot']

# First 3 items
print(food_stuff_lt[0:3:1])  # or food_stuff_lt[:3]

# Last 3 items
print(food_stuff_lt[-3:])