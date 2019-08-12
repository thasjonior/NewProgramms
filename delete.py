import os 
import re
def Getfile(Path):
    Filename=Path.split('/')[len(Path.split('/'))-1]
    Filepath="{}/{}".format(Path,Filename)
    result= re.findall((r'(#file_size)$'),Filepath)
    return result

def delete_txt_file (Path):
     for entry in os.scandir(Path):
        if entry.is_file() and Getfile(entry.path):
            print("file found!")
        elif entry.is_dir():
            print("{}{}".format(entry.name,"subfolder"))
            delete_txt_file(entry.path) 
        else:
            print("error") 


delete_txt_file(r'/home/judethaddeus/Documents/')

