import os
import re
from datetime import datetime

folder_path = "./userdata"

def binary_search(files, target):
    left, right = 0, len(files) - 1
    isRight = False
    while left <= right:
        mid = left + (right - left) // 2

        # 如果目标值等于中间值，返回中间索引
        if files[mid].timestamp == target:
            return mid

        # 如果目标值小于中间值，继续在左半部分搜索
        elif files[mid].timestamp > target:
            isRight = True
            right = mid - 1

        # 如果目标值大于中间值，继续在右半部分搜索
        else:
            isRight = False
            left = mid + 1

    # 如果目标值不在数组中，返回-1表示未找到
    if isRight:
        return right+1
    return left-1

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

    start_time = datetime(2022, 1, 30, 0, 0)
    end_time = datetime(2022, 2, 2, 12, 20)
    start_index = binary_search(file_list, start_time)
    end_index = binary_search(file_list, end_time)

    file_path = "output.txt"
    with open(file_path, "w") as file:
        # 遍历字符串数组并将每个字符串写入文件
        for string in file_list:
            file.write(string.filepath + "\n")

    print("done")
    