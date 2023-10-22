import utils



if __name__ == '__main__':
    try:
        parser = utils.argparse.ArgumentParser()
        group = parser.add_argument_group('Scraping Options (Required)')
        list_book = []

        #arguments
        parser.add_argument('-u', '--url', type=str, help='URL from book.toscrape', required=True)
        parser.add_argument('-n', '--name', type=str, help='Name CSV')

        group.add_argument('-s', '--single', action='store_true', help='choose if you want to scrape one book')       
        group.add_argument('-c', '--category', action='store_true', help='choose if you want to scrape all books in a category')
        group.add_argument('-a', '--all', action='store_true', help='choose if you want to scrape all books from the main page')


        #Read args
        args = parser.parse_args()
        main_url = args.url
        utils.NAME_FILE = args.name

        if not (args.category or args.all or args.single):#si aucune des options a été choisie
            print("""Please select option:
    -> -c/--category = for scrap category
            OR
    -> -a/--all = for scrap all books
            OR
    -> -s/--single = for scrap single book
    examples:
        python main.py -s -u "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
        python main.py -c -u "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
        python main.py -a -u "http://books.toscrape.com/index.html"
            """)
            quit()


        #cette série de condition va vérifié si il y a bien une correspondance entre l'url entrée et l'option group args
        if args.single and (not '/category/' in main_url):
            list_books_informations = utils.get_scrap.conductor(main_url, value=0)
            
        elif args.category and ('/category/' in main_url) and not args.name:
            list_books_informations = utils.get_scrap.conductor(main_url, value=1)

        elif args.all and (not '/category/' in main_url) and (not '/catalogue/' in main_url) and not args.name:
            list_books_informations = utils.get_scrap.conductor(main_url, value=2)

        else:
            print("ERROR: URL doesn't match with the option selected ! OR you have add name for category or all option !")
            quit() 


    except Exception as ex:
        print(f"{ex}")


