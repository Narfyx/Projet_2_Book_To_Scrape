# Projet_2_Book_To_Scrape


## Requirements

-   Python 3.11.5 or higher

Make sure that you have all of the required dependencies installed before running the script. You can install the required dependencies by running the following command:

```python
pip install -r requirements.txt
```
if you are this error (i use manjaro):
```python
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try "pacman -S
    python-xyz", where xyz is the package you are trying to
    install.

```


try with this command:
```python
pip install -r requirements.txt --break-system-packages
```

## Usage

example:
-for scrap single book
```python
python main.py -s -u "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
```

example:
-for scrap category
```python
python main.py -c -u "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
```

example:
-for scrap all category
```python
python main.py -a -u "http://books.toscrape.com/index.html"
```

if you want to name your csv file (work only for single book):

example:
-for scrap single book
```python
python main.py -s -u "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html" --name "Book number 1"
```
The downloaded csv and images will be saved in the "data" folder.

## Create venv

-for windows:
```python
c:\>Python35\python -m venv c:\path\to\Projet_2_Book_To_Scrape
```
-for linux:
```python
python -m venv /path/to/Projet_2_Book_To_Scrape
```
## run venv

-for windows:
```python
c:\>path\to\Projet_2_Book_To_Scrape\Scripts\activate.bat
```
-for linux:
```python
source /path/to/Projet_2_Book_To_Scrape/bin/activate
```




