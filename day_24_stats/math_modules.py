# ==============================================================================
# 30 DAYS OF PYTHON - DAY 24: STATISTICS FROM SCRATCH & THE STATISTICS MODULE
# CODE COMPILATION
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. CUSTOM STATISTICAL FUNCTIONS (PURE PYTHON IMPLEMENTATION)
# ------------------------------------------------------------------------------

def calculate_mean(lst):
    """Calculates the arithmetic mean (average) of a numeric list."""
    if len(lst) == 0:
        return None
    return sum(lst) / len(lst)


def calculate_median(lst):
    """Calculates the middle value of a sorted numeric list."""
    if len(lst) == 0:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        return (sorted_lst[(n // 2) - 1] + sorted_lst[n // 2]) / 2


def calculate_mode(lst):
    """
    Finds the most frequent item(s) in a list.
    Returns a single value, a list of tied modes, or None if no mode exists.
    """
    if len(lst) == 0:
        return None
        
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
        
    max_freq = max(frequency.values())
    
    # If all items appear with frequency 1, there is no mode
    if max_freq == 1:
        return None
        
    modes = [item for item, freq in frequency.items() if freq == max_freq]
    return modes[0] if len(modes) == 1 else modes


def calculate_range(lst):
    """Calculates the difference between the maximum and minimum values."""
    if len(lst) == 0:
        return None
    return max(lst) - min(lst)


def calculate_variance(lst):
    """Calculates the population variance (average of squared deviations from mean)."""
    if len(lst) == 0:
        return None
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)


def calculate_std_dev(lst):
    """Calculates population standard deviation (square root of variance)."""
    if len(lst) == 0:
        return None
    variance = calculate_variance(lst)
    return variance ** 0.5


# ------------------------------------------------------------------------------
# 2. VERIFICATION & COMPARISON WITH THE STATISTICS MODULE
# ------------------------------------------------------------------------------

import statistics

if __name__ == "__main__":
    # Test dataset: Monthly study hours
    study_hours = [28, 35, 42, 35, 50, 22, 35, 40, 48, 31, 35, 29]

    print("=" * 60)
    print("DAY 24 STATISTICS RESULTS COMPARISON")
    print("=" * 60)

    print("\n--- Custom Pure Python Functions ---")
    print("Mean:              ", calculate_mean(study_hours))
    print("Median:            ", calculate_median(study_hours))
    print("Mode:              ", calculate_mode(study_hours))
    print("Range:             ", calculate_range(study_hours))
    print("Population Variance:", calculate_variance(study_hours))
    print("Population Std Dev :", calculate_std_dev(study_hours))

    print("\n--- Built-in statistics Module ---")
    print("Mean:              ", statistics.mean(study_hours))
    print("Median:            ", statistics.median(study_hours))
    print("Mode:              ", statistics.mode(study_hours))
    print("Population Variance:", statistics.pvariance(study_hours))
    print("Population Std Dev :", statistics.pstdev(study_hours))
    print("=" * 60)