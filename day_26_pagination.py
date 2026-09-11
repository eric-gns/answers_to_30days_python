import pandas as pd
import http
import requests
from bs4 import BeautifulSoup

scraped_data = []
base_url = 'https://quotes.toscrape.com'
current_path = '/page/1/'

page_num = 1


while current_path:
	full_url = base_url + current_path
	print(f'Scraping Page... {page_num}: {full_url}...')

	response = requests.get(full_url)
	soup = BeautifulSoup(response.text, 'html.parser')
	quote_cards = soup.find_all('div', class_='quote')

	for i, card in enumerate(quote_cards, start = 1):
		text = card.find('span', class_='text').text.strip()
		author = card.find(class_='author').text.strip()	
		print(f'{i}. {text} - {author}')
		scraped_data.append({'Quote': text, 'Author': author})

	next_li = soup.find('li', class_='next')
	
	if next_li:
		current_path = next_li.find('a')['href']
		page_num += 1
	else :
		current_path = None

df = pd.DataFrame(scraped_data)
df.to_csv('quotes.csv', index = False)
print(f"Done! Scraped {len(df)} total quotes across {page_num} pages.")
		