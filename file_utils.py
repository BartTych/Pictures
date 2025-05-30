import os
import shutil
# Copy files with no date to the new path

def copy_files_with_no_date(files_not_ordered, new_path):
    """
    Copy files with no date to the specified new path.
    
    Args:
        files_not_ordered (set): Set of file paths with no date.
        new_path (str): Path where files should be copied.
    """
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    for file in files_not_ordered:
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        extention = os.path.splitext(file)[1]
        file_name = os.path.basename(file) 
        new_file_path = os.path.join(new_path, file_name)
        shutil.copy2(file, new_file_path)
        print(f"File {file} copied to {new_file_path}")

def copy_files_with_date(files_ordered, new_path):
    """
    Copy files with date to the specified new path.
    
    Args:
        files_ordered (set): Set of file paths with date.
        new_path (str): Path where files should be copied.
    """
    files_ordered = list(files_ordered)
    files_ordered = sorted(files_ordered, key=lambda x: x[1])
    
    
    file_list, date_list = map(list, zip(*files_ordered))
    files_names = new_names(date_list)
    create_folder_structure(date_list, new_path)
    copy_files_to_new_structure(file_list,date_list, files_names, new_path)

def new_names(date_list):
    """Generates new names for files based on their dates."""
    new_name_list = []
    previous_month = None
    counter = 0
    for date in date_list:
        if date.month != previous_month:
            counter = 0
            previous_month = date.month
        else:
            counter += 1

        #new_name = f"{date.year}_{date.month:02d}_{counter:03d}"
        new_name = counter
        new_name_list.append(new_name)
    return new_name_list

def copy_files_to_new_structure(file_list,date_list, new_name_list, path):
    
    nuber_of_files = len(file_list)
    print(f"file to copy: {nuber_of_files}")
    if not os.path.exists(path):
        os.makedirs(path)
    i = 0
    for file, date, new_name in zip(file_list, date_list, new_name_list):
        year = date.year
        month = date.month
        day = date.day
        extention = os.path.splitext(file)[1][1:] 
        new_file_path = os.path.join(path, str(year), f"{month:02}", f"{new_name}.{extention}")
        shutil.copy2(file, new_file_path)
        print(f"Copying {i+1}/{nuber_of_files}")
        i += 1

def create_folder_structure(date_list, path):
    """
    Create a folder structure based on the metadata of the files.
    
    Args:
        files_ordered (set): Set of tuples containing file paths and metadata.
        new_path (str): Path where the folder structure should be created.
    """
    os.makedirs(path, exist_ok=True)

    #years = {d.year for d in date_list}
    years_months = {(d.year, d.month) for d in date_list}

    #for year in years:
        #os.makedirs(os.path.join(path, str(year)), exist_ok=True)
    for year, month in years_months:
        os.makedirs(os.path.join(path, str(year), f"{month:02}"), exist_ok=True)

