import os
import re
from datetime import datetime
import shutil


folder_path = "./userdata"

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

# def extract_r(folder_path ,file_list):
#     items = os.listdir(folder_path)
#     dirs = []
#     files = []
#     for item in items:
#         item_path = os.path.join(folder_path, item)
#         if os.path.isdir(item_path):
#             dirs.append(item_path)
            
#         else:
#             myfile = File()
#             myfile.filepath = item_path
#             file_list.append(myfile)

#         extract_r(item_path, file_list)
        

def extract_files_from_folder(folder_path):
    file_list = []
    extract_r(folder_path, file_list)
    return file_list
    
def make_time_stamp(file_list):
    pass
      
  

if __name__ == "__main__":
    file_list = extract_files_from_folder(folder_path)
    
    #use regular expression to get the timestamp
    #regular = r'(\d{4})(\\|\/)(\d+)(\\|\/)(\d+)(\\|\/)(\d+)-(\d+)'
    pattern = r'[/\\](\d+)[/\\](\d+)[/\\](\d+)[/\\](\d+)[-\\](\d+)'

    for file in file_list:
        match = re.search(pattern, file.filepath)
        v1 = match.group(1)
        groups = match.groups()
        if match:
          year, month, day, hour, minutes = map(int, match.groups())
          file.timestamp = datetime(year, month, day, hour, minutes)

    count = 1
    for file in file_list:
        source_file = file.filepath

        destination_file = f'destination{count}.jpg'  # 目标文件路径

        # 使用 shutil.copy() 拷贝文件
        shutil.copy(source_file, destination_file)

        count +=1 

    print("done")
    