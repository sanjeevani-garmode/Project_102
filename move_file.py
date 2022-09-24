import os
import shutil

from_dir= "C:/Users/dell/Desktop"
to_dir= "C:/Users/dell/Desktop/Document_File"

listOfFiles= os.listdir(from_dir)
for x in listOfFiles:
    name, extension= os.path.splitext(x)
    if extension == " ":
        continue
    if extension in [".docx", ".txt", ".pdf", ".doc"]:
        path1= from_dir+ "/"+ x
        path2= to_dir+ "/"+ "Document_File"
        path3= to_dir+ "/"+ "Document_File"+ "/"+ x
    
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1, path3)
            