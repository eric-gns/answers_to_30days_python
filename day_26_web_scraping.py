# ==============================================================================
# 30 DAYS OF PYTHON - DAY 26: WEB SCRAPING & DATA EXPORT
# CODE COMPILATION
# ==============================================================================

import pandas as pd
import requests
from bs4 import BeautifulSoup

# ------------------------------------------------------------------------------
# 1. FETCH HTML CONTENT
# ------------------------------------------------------------------------------
url = 'https://quotes.toscrape.com'
response = requests.get(url)
print(f"Server Response: {response.status_code}")  # 200 indicates success

# ------------------------------------------------------------------------------
# 2. PARSE HTML & ISOLATE CONTAINERS
# ------------------------------------------------------------------------------
soup = BeautifulSoup(response.text, 'html.parser')

# Find all quote container blocks (<div class="quote">)
quote_cards = soup.find_all('div', class_='quote')

# Initialize container for structured data
scraped_data = []

# ------------------------------------------------------------------------------
# 3. EXTRACT DATA & ACCUMULATE IN A LIST
# ------------------------------------------------------------------------------
for i, card in enumerate(quote_cards, start=1):
    # Extract text relative to the individual container card
    text = card.find('span', class_='text').text.strip()
    author = card.find(class_='author').text.strip()
    
    # Print formatted output to console
    print(f"{i}. {text} - {author}")
    
    # Append structured dictionary record
    scraped_data.append({
        'Quote': text, 
        'Author': author
    })

# ------------------------------------------------------------------------------
# 4. CONVERT TO PANDAS DATAFRAME & EXPORT TO CSV
# ------------------------------------------------------------------------------
df = pd.DataFrame(scraped_data)

# Export without the default numeric row index column
df.to_csv('quotes.csv', index=False)
print("\nScraped data successfully saved to 'quotes.csv'!")