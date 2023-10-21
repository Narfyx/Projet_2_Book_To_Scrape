import requests, csv, argparse
from pprint import pprint
from bs4 import BeautifulSoup
import pandas as pd


if __name__ == '__main__':
    url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"

    def parse_html(page_html):

        
        req = requests.get(page_html)
        encoding = req.encoding if 'charset' in req.headers.get('content-type', '').lower() else None
        soup = BeautifulSoup(req.content, 'html.parser', from_encoding=encoding)
        x = soup.select('div[class="page-header action"] h1')[0].text
        print(x)

        return soup



    parse_html(url)





    print()