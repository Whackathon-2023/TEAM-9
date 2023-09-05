import os
import subprocess

# 指定文件夹路径
folder_path = './data'

# 获取文件夹中的所有文件名
files = []

class File:
  def __init__(self):
      self.filename= ""
      self.timestamp = None


for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path,filename)
    if os.path.isfile(filepath):
        file = File()
        file.timestamp = os.path.getctime(filepath)
        file.filename = filename
        files.append(file)


sorted(files, key = lambda file:file.timestamp)
for i in range(len(files)):
    print(f"name:{files[i].filename},time:{files[i].timestamp}");

#rename
count = 1
for file in files:
    filepath = os.path.join(folder_path,filename)
    newpath = f"{folder_path}/img{count}.jpg"
    os.rename(filepath, newpath)
    count+=1

print("done")


