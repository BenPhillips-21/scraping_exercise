import requests
from bs4 import BeautifulSoup
from scrape_a_quote import scrape_quote

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:134.0) Gecko/20100101 Firefox/134.0'}

url = 'https://quotes.toscrape.com/'

for page_number in range(1, 10):
    print(f'Page number: {page_number}')
    page_url = f'https://quotes.toscrape.com/page/{page_number}'
    response = requests.get(page_url, headers=headers)
    page_html = response.text
    soup = BeautifulSoup(page_html, 'html.parser')

    first_quote = soup.find('div', class_='quote')
    for i in range(10):
        scrape_quote(first_quote)
        first_quote = first_quote.find_next_sibling()

    nav_elem = soup.find('nav')
    nav_ul = nav_elem.find('ul')
    next_anchor = nav_ul.find('li', class_='next').a
    print(next_anchor['href'])

    last_elem = soup.find('footer')
    print(last_elem['class'][0])



