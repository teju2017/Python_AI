'''
Created on 27 Jun 2025

@author: User
'''


import os
import shutil



def clean_directory(Dir_to_purge):
    print("Directory path ="+Dir_to_purge)
    directory_path=Dir_to_purge
    entries = os.listdir(directory_path)
    for entry in entries:
      print(entry)
      if(os.path.isdir(directory_path+entry)):
         shutil.rmtree(directory_path+entry)
      else:
         os.remove(directory_path+entry)
    if(len(os.listdir(directory_path))==0):
        return True
    else:
        return False
         
