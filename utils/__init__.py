
#Fichiers
import utils.create_csv
import utils.get_scrap
import utils.get_image_book
import utils.location_file



#Modules
import requests, csv, argparse, urllib.request, os, re
from pprint import pprint
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed


#Constantes
ALL_PRODUCT_URL = "http://books.toscrape.com/index.html"
CATALOGUE_URL = "http://books.toscrape.com/catalogue/"
BASE_URL = "http://books.toscrape.com/"
NAME_FILE = None

print("init initialisé")