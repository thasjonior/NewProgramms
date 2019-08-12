import os
import pprint
import platform
import re
from time import sleep
#  get all files in directory
#  sort by size 
#  write text file showing file asending order

# CreateFile.tx with folder name   
def CreateFile(Path):
    DirList=Path.split('/')
    l=len(DirList)
    return open("{}/{} {}".format(Path,DirList[l-1],"#file_size"),'w')
# GetSize of each file and print into proper formant of bytes , kb, mb,gb
def GetSize(entry):
    size= entry.stat().st_size
    if size <= 1024 :
        return "{}bytes".format(size)
    elif size <= 1024000:
        return "{:.2f}KB".format(size/ 1024)
    elif size <= 1024000000:
        return "{:.2f}MB".format(size/1024000)
    else:
        return "{:.2f}GB".format(size/1024000000)
# provides key in sorted() basing on size
def comparator (entry):
    return entry.stat().st_size  
# deletes all files.text by CreateFile()
def GetFilepath (Path):
    Filename=Path.split('/')[len(Path.split('/'))-1]
    Filepath="{}/{}".format(Path,Filename) 
    return Filepath

def DeleteFile (Path):
    try:
        os.remove(GetFilepath(Path))
        print("File deleted")
    except:
        print("file not found!")
# fx tha excludes hiden files that starts with .
def ExeptinalFile (Path):
        patten=(r'\.[\w\s-]+$')
        # patten=(r'\.\w+$')
        match=re.findall(patten,GetFilepath(Path))
        if  match:
            return True
# fx that gives space between the name and size
def Space (Path): 
    space=143-len(Path.name)-len(GetSize(Path))
    result=" "*space
    return result
#fx to get file.txt created
def Get_file_text(Path):
    Filename=Path.split('/')[len(Path.split('/'))-1]
    Filepath="{}/{}".format(Path,Filename)
    result= re.findall((r'(#file_size)$'),Filepath)
    return result


# ExeptinalFile(r'/home/judethaddeus/Documents')

# gets file dir open all folders to highest level and creats/delets required file
def GetFile (Path):
    File=CreateFile(Path)
    File.write("FILENAME:{}FILSIZE\n{}\n".format(" "*127,"_"*143))
    # DeleteFile(Path)
    # sleep(10)
    for entry in sorted(os.scandir(Path),key= comparator):
        if entry.is_file():
            # pass
            File.write("{}{}{}\n{}\n".format(entry.name.upper(),Space(entry),GetSize(entry),"-"*143))
            # print("{}.txt File created!".format(entry.name))
            print("File Created !")
            # exit()
        elif entry.is_dir() :
            if ExeptinalFile(entry.path):
                print("skiping {}".format(entry.name))
                continue
            pprint.pprint("SubFolder:{}".format(entry.name.upper()))
            GetFile(entry.path)

        else:
            print(entry.name)
GetFile(r'/home/judethaddeus/Documents/')