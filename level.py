import os

folder_path = "./userdata"

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

        for folder in subfolders:
            extract_r(folder_path +'/' + folder, file_list)

def extract_files_from_folder(folder_path):
    file_list = []
    extract_r(folder_path, file_list)
    return file_list
    
def make_time_stamp(file_list):
    for file in file_list:
        pass
        
    

if __name__ == "__main__":
    file_list = extract_files_from_folder(folder_path)
    print("done")
    