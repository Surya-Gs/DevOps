#Problem1

import os
folders = input("Enter the list of folders").split()

for folder in folders:

    try:
        files =os.listdir(folder)
        print(files)
    except FileNotFoundError:
        print("The files has been not found in the path mentioned")

        break
        print("Listing the files of the folde:" + folder)