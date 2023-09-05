import os
import re

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
                #sorted(subfolders, cmp = custom_sort )
                #Density.sort(key = getSecond, reverse = True);
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
    
    file_path = "output.txt"
    with open(file_path, "w") as file:
        # 遍历字符串数组并将每个字符串写入文件
        for string in file_list:
            file.write(string.filepath + "\n")

    print("done")
    