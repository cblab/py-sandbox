import os

def rename_files():
    #(1) get file names from a folder
    data_path = os.getcwd() + '/data'
    file_list = os.listdir(data_path)
    print(file_list)

    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename( data_path + "/" + file_name, file_name.translate(None, "0123456789"))

    # (3) take a look at the pictures, sort them alphabetically

rename_files()