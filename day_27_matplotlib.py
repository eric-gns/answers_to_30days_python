import pandas as pd
import matplotlib.pyplot as plt

# Load CSV generated from Day 26
df = pd.read_csv('quotes.csv')

# Count top 5 authors
top_authors = df['Author'].value_counts().head(5)

# Plot top authors
top_authors.plot(kind='barh', color='coral')
plt.title('Top 5 Authors by Quote Count')
plt.xlabel('Number of Quotes')
plt.grid(axis= 'x', linestyle='--')
plt.ylabel('Authors')
plt.show()# ==============================================================================
# 30 DAYS OdF PYTHON - DAY 27: DATAFRAME VISUALIZATION & PIPELINE INTEGRATION
# CODE COMPILATION
# ==============================================================================

import matplotlib.pyplot as plt
import pandas as pd

# ------------------------------------------------------------------------------
# 1. STACKED BAR CHART FROM DATAFRAME
# ------------------------------------------------------------------------------
workforce_data = {
    'Department': ['Engineering', 'Sales', 'Marketing', 'HR', 'Support'],
    'Full_Time': [35, 25, 12, 8, 20],
    'Contractors': [10, 5, 6, 2, 5],
}
df_workforce = pd.DataFrame(workforce_data)

plt.figure(figsize=(8, 4))
df_workforce.plot(
    x='Department',
    kind='bar',
    stacked=True,
    color=['#1f77b4', '#ff7f0e'],
    rot=0,
    title='Department Workforce Breakdown',
)
plt.ylabel('Number of Staff')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# ------------------------------------------------------------------------------
# 2. VISUALIZING SCRAPED PIPELINE DATA (DAY 26 INTEGRATION)
# ------------------------------------------------------------------------------
# Read quotes scraped from quotes.toscrape.com
df_quotes = pd.read_csv('quotes.csv')

# Aggregate top 5 authors by count
top_authors = df_quotes['Author'].value_counts().head(5)

# Plot horizontal bar chart
plt.figure(figsize=(8, 4))
top_authors.plot(kind='barh', color='coral')
plt.title('Top 5 Most Quoted Authors')
plt.xlabel('Number of Quotes')
plt.ylabel('Authors')
plt.grid(axis='x', linestyle='--', alpha=0.7)
# Invert y-axis so the #1 author is displayed at the very top
plt.gca().invert_yaxis()
plt.show()