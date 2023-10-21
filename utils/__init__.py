
#Fichiers
import utils.test #prototypage
import utils.create_csv
import utils.get_scrap
import utils.get_image_book


#Modules
import requests, csv, argparse, urllib.request
from pprint import pprint
from bs4 import BeautifulSoup
import pandas as pd


#Constantes
ALL_PRODUCT_URL = "http://books.toscrape.com/index.html"
CATALOGUE_URL = "http://books.toscrape.com/catalogue/"
BASE_URL = "http://books.toscrape.com/"
NAME_FILE = None

print("init initialisé")