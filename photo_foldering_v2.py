import os
from datetime import datetime

file_data = dict()  #k:file_name v: epoch_st_mtime
folder_name =list() # file-datum
work_dir = input("Enter the working directory: ")
os.chdir(work_dir)
for file in os.listdir(work_dir):
    if os.path.isfile(os.path.join(work_dir,file)) and not file.startswith("."):
        create_date = os.stat(os.path.join(work_dir,file)).st_mtime 
        if create_date not in file_data.values():
            file_data[file]=create_date
        datum = datetime.fromtimestamp(create_date).strftime("%y-%m")
        if os.path.isdir(os.path.join(work_dir,datum)): 
            continue
        else:
            os.mkdir(datum) 
        
for k,v in file_data.items():
    datum = datetime.fromtimestamp(v).strftime("%y-%m")
    os.rename(os.path.join(work_dir,k),os.path.join(work_dir,datum,k))
