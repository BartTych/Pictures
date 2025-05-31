from itertools import groupby
from operator import itemgetter



def remove_same_res_jpegs_with_lower_coding_quality(images):
    return [
        img for img in images
        if not (
            (img["ext"] == ".jpeg" or img["ext"] == ".jpg")
            and has_same_resolution_duplicate_with_higher_coding_quality(img, images)
        )
    ]

def has_same_resolution_duplicate_with_higher_coding_quality(img, images):
    for other in images:
        if other['ext'] not in [".jpeg", ".jpg"]:
            continue

    
        if bin(img['hash']^ other['hash']).count('1') <= 4 and other["resolution"] == img["resolution"] and other['size'] > img['size']:
            if img['date'] is not None and other['date'] is None:
                #will put it in log file
                print('lower quality image has date, but higher quality does not. requiring manual user check !!')
            return True
    return False



def remove_duplicates_with_given_ext(file_list,ext):
    """
    Remove duplicate of *.ext files based on their hash.

    Args:
        file_list (list): List of file describing dictionaries.
        
    Returns:
        list: List of file dictionaries with duplicates removed.
    """
    def choose_file_with_date_if_any(group):
        group = list(group)
        # Prefer files with non-None date
        files_with_date = [f for f in group if f.get("date") is not None]
        if files_with_date:
            return files_with_date[0]
        return group[0]


    is_ext = lambda f: f["ext"] == ext
    ext_files = filter(is_ext, file_list)

    # Sort by hash to group duplicates together
    sorted_files_with_ext = sorted(ext_files, key=itemgetter("hash"))

    # Group by hash and take the first file from each group
    unique_files_with_ext = [choose_file_with_date_if_any(group) for _, group in groupby(sorted_files_with_ext, key = itemgetter("hash"))]

    # Keep non-heics unchanged
    non_given_ext = filter(lambda f: f["ext"] != ext, file_list)

    # Combine and return
    return list(non_given_ext) + unique_files_with_ext

def remove_converted_jpegs_with_metadata(file_list):
    """
    Remove JPEG files that were converted from HEIC files based on metadata similarity.
    Requires updated logic for cased with files without metadata.
    Args:
        file_list (list): List of file metadata dictionaries.
        size_tolerance (float): Tolerance for file size difference as a fraction (e.g., 0.1 for 10%).

    Returns:
        list: Filtered list of file metadata dictionaries.
    """
    filtered_files = []
    heic_files = [f for f in file_list if f['ext'] == '.heic']
    jpeg_files = [f for f in file_list if f['ext'] == '.jpeg']

    for jpeg in jpeg_files:
        is_converted = any(
            heic['resolution'] == jpeg['resolution'] and
            heic['date'] == jpeg['date'] 
            for heic in heic_files
        )
        if not is_converted:
            filtered_files.append(jpeg)

    # Add back non-JPEG files and HEIC files
    filtered_files.extend([f for f in file_list if f['ext'] != '.jpeg'])

    return filtered_files


