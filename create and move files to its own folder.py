import os
import shutil

directory = os.getcwd()

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):  # change file name from .pdf to any other if needed
        path = filename.split('.')[0]
        os.mkdir(path)
        shutil.move(filename, path + '/' + filename)
