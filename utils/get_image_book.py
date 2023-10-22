import utils

def save_img(images_url, titles, upc, name_folder_img):
    for index, image_url in enumerate(images_url):
        img_folder = utils.location_file.file_location('data/img/')
        path = utils.location_file.file_location(f'data/img/{name_folder_img}/')
        utils.urllib.request.urlretrieve('http://' + image_url, f"{path}{upc[index]}.jpg")
        print(f"download image of: {titles[index]}")