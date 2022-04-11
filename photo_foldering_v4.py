from PIL import Image
import os
from datetime import datetime
file_data ={}
folder_name =list()
def get_date_taken(path):
    for file in os.listdir(path):
       if os.path.isdir(file) or file.startswith(path):
           continue
       else:
           if os.path.splitext(file)[1] != ".MOV" or os.path.splitext(file)[1] != ".mp4" :
               taken_time = Image.open(os.path.join(path,file))._getexif()[36867]
               if taken_time not in file_data.values():
                   file_data[file] = taken_time
       
    for v in file_data.values():
       if (v[:4]+"-"+v[5:7]) not in folder_name:
         folder_name.append(v[:4]+"-"+v[5:7])
    
    # creat folders
    for i in folder_name:
      if not os.path.isdir(i):
        os.mkdir(i)

    # copy files into appropriated folder
    for k,v in file_data.items():
      name = (v[:4]+"-"+v[5:7])
      if not os.path.isdir(os.path.join(path,name,k)):
          os.rename(os.path.join(path,k),os.path.join(path,name,k))



   
get_date_taken(r"C:\rknktm\OneDrive\Desktop\16")


  






