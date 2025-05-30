import load_date_extractors
import file_date_extractor as file_date_extractor
import os
import shutil
# Assuming handlers are classes that inherit from Read_meta

handlers = load_date_extractors.load_all_handlers()
file_date_extractor = file_date_extractor.flie_meta_extractor(handlers)


valid_extensions = {'.jpg', '.jpeg', '.heic','.mov','.mp4','.avi'}
#path ='/Users/bart_mac/Desktop/zdjecia_test/sandbox'
path ='/Users/bart_mac/Desktop/Cloud_storage'
new_path = '/Users/bart_mac/Desktop/No_date_files'
#have to decide where to put logic for extension checking

files_ordered = set()
ordered_repeat_check = set()    


files_not_ordered = set()
not_ordered_repeat_check = set()


# new repeat check besed on file hash for both ordered and not ordered files
# if the file hash is in the set it is neccesary to chech which is larger
# when it is larger it replaces the smaller one
# when it is smaller it is not added to the set and script continues
# so the whole idea of previous repeat check is not needed just some info in whinch set the file is


# Walk through the directory and process files
# prepares set of files with metadata and without metadata
# without repeatitions
# repeatitions are checked by metadata and file size when metadata is available
# when metadata is not available it is checked by file name and file size


for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1].lower() not in valid_extensions or os.path.basename(file).startswith('.'):
                continue
            file_path = os.path.join(root, file)
            
            metadata = file_date_extractor.apply(file_path)
            if metadata is not None:
                if (metadata,os.path.getsize(file_path)) not in ordered_repeat_check:
                    ordered_repeat_check.add((metadata,os.path.getsize(file_path)))
                    files_ordered.add((file_path, metadata))
                    continue
            else:
                if (file, os.path.getsize(file_path)) not in not_ordered_repeat_check:
                    not_ordered_repeat_check.add((file_path, os.path.getsize(file_path)))
                    files_not_ordered.add(file_path)
                    continue

for file in files_not_ordered:
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    extention = os.path.splitext(file)[1]
    file_name = os.path.basename(file) 
    new_file_path = os.path.join(new_path, file_name)
    shutil.copy2(file, new_file_path)
    print(f"File {file} copied to {new_file_path}")


for file_path, metadata in files_ordered:
    print(f"File: {file_path}, Date: {metadata}")
print("Files with no date:")
for file_path in files_not_ordered:
    print(f"File: {file_path}")

