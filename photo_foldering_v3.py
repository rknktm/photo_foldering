import os
from datetime import datetime
file_data = dict()
folder_name =list()
wd = input("Working Directory:")
os.chdir(wd)
for file in os.listdir('.'):
  if os.path.isdir(file) or file.startswith('.'):
    continue
  else:
    modified_time =os.stat(file).st_mtime
    if modified_time not in file_data.values():
      file_data[file]=modified_time
    year = datetime.fromtimestamp(modified_time).strftime("%y")
    if year not in folder_name:
      folder_name.append(year)

# creat folders
for i in folder_name:
  if not os.path.isdir(i):
    os.mkdir(i)

# copy files into appropriated folder
for k,v in file_data.items():
  year= datetime.fromtimestamp(v).strftime("%y")
  #if not os.path.isdir(os.path.join(wd,year,k)):
  os.rename(os.path.join(wd,k),os.path.join(wd,year,k))


