
import os
import shutil
import subprocess


path = '/Users/bart_mac/Desktop/untitled folder'
new_path = '/Users/bart_mac/Desktop/copy2_test'

file_paths = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(path)
        for file in files
    ]


for file_path in file_paths:
    name = os.path.basename(file_path)
    new_file_path = os.path.join(new_path,name)

    shutil.copy(file_path,new_file_path)
