import os
import re
from datetime import datetime
import shutil
from globalVar import *

folder_path = g_original_dir

def custom_sort(a):
    parts = re.split(r'[\\/\\-]', a)
    int_parts = [int(part) for part in parts] 
    return tuple(int_parts)

class File:
  def __init__(self):
      self.filepath= ""
      self.timestamp = None

def extract_r(folder_path ,file_list):
    for folder, subfolders, files in os.walk(folder_path):
        if(len(subfolders)==0):
            for file in files:
                myfile = File()
                myfile.filepath = os.path.join(folder, file)
                file_list.append(myfile)
        if(len(subfolders)>0):
            if subfolders[0].isdigit(): #for numbers
                subfolders.sort(key = lambda x : int(x))
            else:
                subfolders.sort(key = custom_sort )
        for folder in subfolders:
            extract_r(folder_path +'/' + folder, file_list)
        break
        
def extract_files_from_folder(folder_path):
    file_list = []
    extract_r(folder_path, file_list)
    return file_list
  

if __name__ == "__main__":
    file_list = extract_files_from_folder(folder_path)
    
    #use regular expression to get the timestamp
    pattern = r'[/\\](\d+)[/\\](\d+)[/\\](\d+)[/\\](\d+)[-\\](\d+)'

    outputDir = g_file_dir

    for file in file_list:
        match = re.search(pattern, file.filepath)
        v1 = match.group(1)
        groups = match.groups()
        if match:
          year, month, day, hour, minutes = map(int, match.groups())
          file.timestamp = datetime(year, month, day, hour, minutes)

    count = 1
    writer = open(f"{outputDir}/time.txt","w")
    for file in file_list:
        source_file = file.filepath

        date_time = file.timestamp.strftime("%Y-%m-%d-%H-%M")
        destination_file = f'{outputDir}/destination{count}.jpg'  # target file path
        writer.write(f"{date_time}_1\n")

        #copy to 
        shutil.copy(source_file, destination_file)
        count +=1 

    writer.close()
    print("done")
    