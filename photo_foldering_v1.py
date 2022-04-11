import os
from datetime import datetime

file_data = dict()  #k:file_name v: epoch_st_mtime
folder_name =list() # file-datum
work_dir = input("Enter the working Directory: ")
os.chdir(work_dir)
for file in os.listdir(work_dir):
    if os.path.isdir(os.path.join(work_dir,file)):
        continue
    if file.startswith("."):
        continue
    else:
        epoch = os.stat(os.path.join(work_dir,file)).st_mtime 
#st_birthtime methodunu da bir dene
        if epoch not in file_data.values():
            file_data[file]=epoch
        datum = datetime.fromtimestamp(epoch).strftime("%Y")
        if os.path.isdir(os.path.join(work_dir,datum)): 
            continue
        else:
            os.mkdir(datum) 
        
for k,v in file_data.items():
    datum = datetime.fromtimestamp(v).strftime("%Y")
    os.rename(os.path.join(work_dir,k),os.path.join(work_dir,datum,k))
