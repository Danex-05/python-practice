#! /usr/bin/python3

import os, shutil

ext = input("Input the extention you want to sort: \n")
path = "../my_class-exercise/folders/"

files = os.listdir(path)
for file in files:
    if file.endswith(ext):
        if not os.path.exists(path + ext):
            os.mkdir(path + ext)
        if os.path.exists(path + ext):
            new_file_path = os.path.join(path, ext)
            source = os.path.join(path, file)
            destination = os.path.join(new_file_path, file)
            
            shutil.copy(source, destination)
            print("file copied successfully")
        else:
            print("Directory does not exists")
    else:
        print("No files has the specified extension called " + ext)
        




