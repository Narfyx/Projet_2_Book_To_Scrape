import utils



def write_csv(books, name_file):
    folder = utils.location_file.file_location('data/')
    print("\n")
    book_dict = {
    'product_page_url:': [],
    'universal_product_code:': [],
    'search_title:': [],
    'price_including_tax:': [],
    'price_excluding_tax:': [],
    'search_number_available:': [],
    'product_description:': [],
    'category:': [],
    'review_rating:': [],
    'image_url:': []
    }
    for book in books:
        book_dict['product_page_url:'].append(books[book][0])
        book_dict['universal_product_code:'].append(books[book][1])
        book_dict['search_title:'].append(books[book][2])
        book_dict['price_including_tax:'].append(books[book][3])
        book_dict['price_excluding_tax:'].append(books[book][4])
        book_dict['search_number_available:'].append(books[book][5])
        book_dict['product_description:'].append(books[book][6])
        book_dict['category:'].append(books[book][7])
        book_dict['review_rating:'].append(books[book][8])
        book_dict['image_url:'].append(books[book][9])
        print(f"working on {book} ")

    df = utils.pd.DataFrame(book_dict)
    utils.pprint(df)
    if name_file == None:
        name_file = book_dict['universal_product_code:'][0]
        df.to_csv(f'{folder}{name_file}.csv', sep='\t', encoding='utf-8', index=False)
    else:
        df.to_csv(f'{folder}{name_file}.csv', sep='\t', encoding='utf-8', index=False)
    print(f"CSV file '{name_file}' created successfully.")
    
    utils.get_image_book.save_img(images_url = book_dict['image_url:'], titles=book_dict['search_title:'], upc=book_dict['universal_product_code:'], name_folder_img=name_file)



