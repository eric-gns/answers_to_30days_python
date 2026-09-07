from collections import Counter

# ==========================================
# DATASET
# ==========================================
countries_data = [
    {'name': 'Finland', 'capital': 'Helsinki', 'population': 5540720, 'languages': ['Finnish', 'Swedish']},
    {'name': 'Estonia', 'capital': 'Tallinn', 'population': 1328976, 'languages': ['Estonian']},
    {'name': 'Sweden', 'capital': 'Stockholm', 'population': 10353442, 'languages': ['Swedish']},
    {'name': 'Norway', 'capital': 'Oslo', 'population': 5379475, 'languages': ['Norwegian', 'Sami']},
    {'name': 'Iceland', 'capital': 'Reykjavik', 'population': 366425, 'languages': ['Icelandic']},
]


# ==========================================
# 1. UNIVERSAL DECORATOR (*args, **kwargs)
# ==========================================
def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print('executing function...')
        result = func(*args, **kwargs)
        print('functions executed!')
        return result
    return wrapper

@debug_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# ==========================================
# 2. LEVEL 3 - EXERCISE 1: SORTING FUNCTIONS
# ==========================================
def sorting_countries_data():
    sorted_name = sorted(countries_data, key=lambda c: c['name'])
    sorted_cap = sorted(countries_data, key=lambda c: c['capital'])
    sorted_pop = sorted(countries_data, key=lambda c: c['population'], reverse=True)
    
    print('--- Exercise 1: Sorted Countries ---')
    print('Sorted by name:', [c['name'] for c in sorted_name])
    print('Sorted by capital:', [c['capital'] for c in sorted_cap])
    print('Sorted by population:', [c['name'] for c in sorted_pop])
    print()


# ==========================================
# 3. LEVEL 3 - EXERCISES 2 & 3: MOST SPOKEN LANGUAGES
# ==========================================
def most_spoken_language(data, n):
    all_languages = []
    for country in data:
        for lang in country['languages']:
            all_languages.append(lang)
    language_counts = Counter(all_languages)
    return language_counts.most_common(n)


# ==========================================
# 4. LEVEL 3 - EXERCISE 4: MOST POPULATED COUNTRIES
# ==========================================
def most_populated_countries(data, n):
    sorted_countries = sorted(data, key=lambda c: c['population'], reverse=True)
    sliced_data = sorted_countries[:n]
    return sliced_data


# ==========================================
# SCRIPT EXECUTION
# ==========================================
if __name__ == "__main__":
    print("=== DAY 14: HIGHER-ORDER FUNCTIONS RECAP ===\n")

    # 1. Test Decorator
    print("--- Decorator Test ---")
    print(greet(name="Mark", greeting="Welcome"))
    print()

    # 2. Test Exercise 1
    sorting_countries_data()

    # 3. Test Exercises 2 & 3
    print("--- Exercises 2 & 3: Top 3 Spoken Languages ---")
    print(most_spoken_language(countries_data, 3))
    print()

    # 4. Test Exercise 4
    print("--- Exercise 4: Top 3 Most Populated Countries ---")
    top_3_populated = most_populated_countries(countries_data, 3)
    for country in top_3_populated:
        print(f"{country['name']}: {country['population']:,}")