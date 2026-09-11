# ==============================================================================
# 30 DAYS OF PYTHON - DAY 25: PANDAS & DATA ANALYSIS
# CODE COMPILATION
# ==============================================================================

import pandas as pd

# ------------------------------------------------------------------------------
# 1. CREATING A DATAFRAME
# ------------------------------------------------------------------------------
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [20, 22, 19, 21],
    'Score': [85, 92, 78, 90]
}

df = pd.DataFrame(data)

# Inspecting top 2 rows
print("--- First 2 Rows ---")
print(df.head(2))

# Calculating column mean
score_mean = df['Score'].mean()
print(f"\nMean Score: {score_mean}")

# ------------------------------------------------------------------------------
# 2. FILTERING & VECTORIZED COLUMN CREATION
# ------------------------------------------------------------------------------
# Boolean Indexing / Filtering
filtered_df = df[df['Score'] >= 80] 
print("\n--- Filtered DataFrame (Score >= 80) ---")
print(filtered_df)

# Adding a new boolean column (Vectorized comparison)
df['passed'] = df['Score'] >= 80
print("\n--- DataFrame with 'passed' Column ---")
print(df)

# ------------------------------------------------------------------------------
# 3. INSPECTION & AGGREGATION
# ------------------------------------------------------------------------------
print("\n--- Summary Statistics (.describe()) ---")
print(df.describe())

print("\n--- DataFrame Information (.info()) ---")
df.info()

# Calculating mean age of students who passed
avg_passed_age = df[df['passed']]['Age'].mean()
print(f"\nAverage age of students who passed: {avg_passed_age}")