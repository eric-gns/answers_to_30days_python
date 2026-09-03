# 1. Check Prime
def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# 2. Unique Elements Check
def is_unique(lst):
    return len(lst) == len(set(lst))


# 3. Same Data Type Check
def is_same_type(lst):
    return len(set(type(x) for x in lst)) == 1


# 4. Valid Python Variable Identifier Check
def is_valid_variable(name):
    return name.isidentifier()


# 5. Empty List Check
def check_list_empty(lst):
    return len(lst) == 0  # or: return not lst


# 6. Calculate Mean
def calculate_mean(lst):
    if len(lst) == 0:
        return False
    mean = sum(lst) / len(lst)
    return mean


# 7. Calculate Median
def calculate_median(lst):
    if len(lst) == 0:
        return False
    s_list = sorted(lst)
    n = len(s_list)

    if len(s_list) % 2 == 1:
        return s_list[n // 2]
    else:
        return (s_list[(n // 2) - 1] + s_list[n // 2]) / 2


# 8. Calculate Mode
def calculate_mode(lst):
    return max(lst, key=lst.count)


# 9. Calculate Range
def calculate_range(lst):
    return max(lst) - min(lst)