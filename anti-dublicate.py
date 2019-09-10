import os
import pprint
# fx get fileinf ... size and name and path
def GetInfo(entry):
    F_size=entry.stat().st_size
    F_name=entry.name
    # F_list= []
    # F_list=[F_name,F_size]
    return "{}-{}".format(F_name,F_size)

# for entry in os.scandir(r'/home/judethaddeus/Documents/fileX'):
#     pprint.pprint(GetInfo(entry))
# def CmpInfo (Path):
#     item=GetFiles(Path).split(',')
#     pprint.pprint(item.cmp())

def PrintUniqueFiles (Path):
    container= set() 
    GetFiles(Path,container)
    pprint.pprint(container)  
    
# fx get all files in folder
def GetFiles (Path, container):
    #fileinfo container
    for entry in os.scandir(Path):
        if entry.is_file():
            container.add(GetInfo(entry))
        elif entry.is_dir():
            GetFiles(entry.path,container)
        else:
            print("Unknwon content: {}".format(entry.name))
        # InfoSet=set(container)
# fx check dublicated files with same name size ,path and format 
# fx delete dublicates leaving single file
PrintUniqueFiles(r'/home/judethaddeus/Documents')
