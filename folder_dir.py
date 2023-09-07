import os
import re
from datetime import datetime

#folder_path = "./Problem06_Still_No_Longer/TEAM-9/userdata"
folder_path = "./userdata"

class File:
    def __init__(self):
        self.filepath= ""
        self.timestamp = None

def extract_r(folder_path, file_list):
    for folder, subfolders, files in os.walk(folder_path):
        if not subfolders:
            for file in files:
                myfile = File()
                myfile.filepath = os.path.join(folder, file)
                myfile.timestamp = extract_timestamp(myfile.filepath)
                file_list.append(myfile)

def extract_timestamp(filepath):
    # Extract timestamp from the file path using regular expressions
    match = re.search(r'(\d{4})/(\d+)/(\d+)/(\d+)-(\d+)', filepath)
    if match:
        year, month, day, hour, minutes = map(int, match.groups())
        return datetime(year, month, day, hour, minutes)
    return None

def extract_files_from_folder(folder_path):
    file_list = []
    extract_r(folder_path, file_list)
    return sorted(file_list, key=lambda x: x.timestamp)

if __name__ == "__main__":
    file_list = extract_files_from_folder(folder_path)
    
    # Print the sorted list of file paths
    for file in file_list:
        print(file.filepath)

    print("done")
