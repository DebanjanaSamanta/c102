import os
import shutil

from_dir = "C:/Users/HP/Downloads"
to_dir = "C:/Users/HP/Documents"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)

    if extension == '':
        continue;
    
    if extension in ['.pdf']:
        path1 = file_name + "/" + from_dir
        path2 = to_dir + "/" + "Document_files" 
        path3 = to_dir + "/" + "Document_files" + "/" + file_name

        if os.path.exists(path2):
            print("Moving" + file_name + ".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2) 
            print("Moving " + file_name + ".....")
            shutil.move(path1, path3)

        
