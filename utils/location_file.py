import utils

def file_location(value):
    folder_name = value  # Replace with your desired folder name
    if not utils.os.path.exists(folder_name):
        utils.os.mkdir(folder_name)

    return folder_name
