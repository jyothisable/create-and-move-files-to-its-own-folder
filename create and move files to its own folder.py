import os
import shutil

directory = os.getcwd()

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):  # change file name from .pdf to any other if needed
        path = filename.split('.')[0]
        os.mkdir(path)
        shutil.move(filename, path + '/' + filename)
        

'''     
This is a Python script to make folder for selected files and then move those files to corresponding folders with same name as file name.

Instructions to use
1. Place this python script in folder containing files
2. Specify the file extension that you want to select(default is .pdf)
3. Now run the script in powershell or cmd(shift + right click and select open in windows terminal)
4. The files with given extension will now be placed inside corresponding folders with same name as file name

WARNING
In editions of Windows before Windows 10 version 1607, the maximum length for a path is MAX_PATH, which is defined as 260 characters.
In later versions of Windows, changing a registry key or using the Group Policy tool is required to remove the limit.
'''