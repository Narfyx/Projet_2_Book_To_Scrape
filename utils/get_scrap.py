import utils




def parse_html(page_html):

    req = utils.requests.get(page_html)
    encoding = req.encoding if 'charset' in req.headers.get('content-type', '').lower() else None
    soup = utils.BeautifulSoup(req.content, 'html.parser', from_encoding=encoding)
    

    return soup


def number_page(main_url):#récupère toutes les pages (doit être une page contenant plusieurs livres et pages)
    list_of_url_found = []

    rsplit_url = main_url.rsplit('/', 1)[0] + '/'
    if not utils.BASE_URL in rsplit_url:
        rsplit_url = utils.BASE_URL + rsplit_url
    print(rsplit_url)

    count = 1
    
    if main_url == utils.ALL_PRODUCT_URL:
            rsplit_url = utils.BASE_URL

    while count < 100:
        
        url = f"{rsplit_url}page-{count}.html"
        request = utils.requests.get(url)
        
        if request.status_code == 200:
            list_of_url_found.append(url)
            print("\t pages trouvées =", count, end='\r')
            
            count += 1
        else:
            break
    print("\n")
    if list_of_url_found == []:
        return main_url

    return list_of_url_found


def number_books_on_page(list_page_url):#ajoute à une liste toutes les url de livre sur chaque page qu'il reçoit

    if not isinstance(list_page_url, list):
        list_page_url = [list_page_url]
        
    books_url = []
    for index_page, url in enumerate(list_page_url):

        soup = parse_html(url)
        rsplit_url = utils.CATALOGUE_URL

        
        grep_link = ([rsplit_url + (a['href']).replace("../../../","") for a in soup.select('ol[class="row"]  li article[class="product_pod"] div[class="image_container"] a')])


        for index_link, value in enumerate(grep_link):
            print(f"found link number {index_link + 1}/{len(grep_link)} (work on page {index_page + 1})" , end='\r')
            books_url.append(value)
   
    return books_url, len(books_url)


def grep_book_informations(product_page_url):#récupère toutes les informations sur un livre
    
    soup = parse_html(product_page_url)
    book = []
    book.append(product_page_url) #'product_page_url'
    book.append((soup.select('table[class="table table-striped"]  tr:first-child td')[0]).text) #'universal_product_code'
    book.append((soup.select('div[class="col-sm-6 product_main"]  h1')[0]).text) #'search_title'
    book.append((soup.select('table[class="table table-striped"]  tr:nth-child(4) td')[0]).text.strip('Â')) #'price_including_tax'
    book.append((soup.select('table[class="table table-striped"]  tr:nth-child(3) td')[0]).text.strip('Â')) #'price_excluding_tax'
    book.append((soup.select('table[class="table table-striped"]  tr:nth-child(6) td')[0]).text.strip(' availableInstock()')) #'search_number_available'
    book.append((soup.select('article[class="product_page"] div[id="product_description"] ~ p')[0]).text if soup.select('article[class="product_page"] div[id="product_description"] ~ p') else 'N/A') #'product_description'

    # '~ p' signifie "sélectionner tous les éléments <p> qui sont des frères (qui suivent immédiatement) de l'élément précédemment sélectionné".


    book.append((soup.select('ul[class="breadcrumb"]  li:nth-child(3) a')[0]).text) #'category'
    book.append(soup.select('div.col-sm-6.product_main p[class*=star-rating]')[0]['class'][-1]) #'review_rating'

    #p[class*=star-rating], cela recherchera tous les éléments <p> qui ont un attribut class contenant 
    #n'importe quelle class qui contient la sous-chaîne "star-rating". 
    #Cela pourrait correspondre à des classes comme "star-rating", "star-rating-Five", "star-rating-Excellent", etc.
    
    #pour ['class'][-1] si la valeur de l'attribut class était "star-rating Five", [-1] donnerait "Five".
    
    book.append((soup.select('div[class="item active"] img')[0]['src']).replace("../../", "books.toscrape.com/")) #'image_url'
    
    return book


def get_status_url(url) -> str:
    return ("valide" if utils.requests.get(url).status_code == 200 else "invalide"), url

def try_to_connect_and_grep_books_information(list) -> dict:
    books = {}
    #utile pour des opérations intensives en E/S, telles que les requêtes HTTP.
    #chaque thread est responsable de l'envoi de demandes de requêtes HTTP 
    #vers différentes URLs de la liste en parallèle. 
    # Cela signifie qu'un thread commence à traiter une URL, 
    # puis envoie la demande de requête, tandis qu'un autre thread commence 
    # à traiter une URL différente et envoie sa propre demande de requête. 
    # Cette approche parallèle permet d'accélérer le processus, car les demandes de 
    # requête peuvent être en cours d'envoi ou d'attente de réponse pendant que d'autres 
    # URLs sont traitées.

    # Utiliser un ThreadPoolExecutor pour exécuter plusieurs tâches en parallèle
    with utils.ThreadPoolExecutor(max_workers=1) as executor:  # ajuste le nombre de 'worker' (ce sont les threads cpu)
        futures = {executor.submit(get_status_url, url): url for url in list} #envoie en parallèle les requêtes http qui se trouve dans la list à la fonction get_status_url
        #quand une requête à un retour et traité par la fonction get_status_url elle est considéré comme terminée
        for future in utils.as_completed(futures):#pour chaque 'future' dans les requêtes terminées
            status, url = future.result()
            print(f"\t url {status} = {url}\r", end='')

            if status == "valide":
                key = "book_number_" + str(list.index(url))
                books[key] = grep_book_informations(url)

    return books

def get_all_category_url_from_product_page(soup) -> list:
    category = []
    parent_element = soup.select('div[class="side_categories"]')
    

    for x in range(1, len(soup.select('li')) + 1):
        link = soup.select(f'div[class="row"] aside[class="sidebar col-sm-4 col-md-3"] div[class="side_categories"] ul[class="nav nav-list"] ul li:nth-child({x}) a')
        href = link[0]['href'] if link else None  # Get the 'href' attribute if 'link' exists, or None if it doesn't
        
        if href is None:
            break

        category.append(utils.BASE_URL + href)
    print(category)    

    return category


def run(url):
    list_page_found = number_page(url)
    list_url_books = number_books_on_page(list_page_found)
    print(f"\n -Number book url found = {list_url_books[1]}")
    books_information = try_to_connect_and_grep_books_information(list_url_books[0])
    return books_information


def conductor(main_url, value):#fonction principale de ce fichier
    
    soup = parse_html(main_url)

    if value == 0:#mode single book
        book = try_to_connect_and_grep_books_information([main_url])
        utils.create_csv.write_csv(book, utils.NAME_FILE)

    if value == 1:#mode category
        books = run(main_url)
        utils.create_csv.write_csv(books, name_file="category")

    if value == 2:#mode all books
        print(value)
        if main_url == utils.ALL_PRODUCT_URL:
            get_all_category_url = get_all_category_url_from_product_page(soup)
            for category in get_all_category_url:
                books = run(category)
                title = parse_html(category)
                utils.NAME_FILE = title.select('div[class="page-header action"] h1')[0].text
                utils.create_csv.write_csv(books, utils.NAME_FILE)
        else:
            print('ERROR in value 2')
            quit()





#conductor(main_url)