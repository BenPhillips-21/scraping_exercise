from bs4 import BeautifulSoup

def scrape_quote(quote_div):
    first_span = quote_div.span
    first_quote = first_span.text
    print(first_quote)

    second_span = first_span.find_next_sibling()
    first_author = second_span.small.text
    print(first_author)

    tags_div = quote_div.find('div', class_='tags')
    tags = tags_div.find_all('a')
    for tag in tags:
        print(tag.text)