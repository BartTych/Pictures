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

    
        if bin(img["hash"] ^ other["hash"]).count("1") <= 5 and other["resolution"] == img["resolution"] and other['size'] > img['size']:
            if img['date'] is not None and other['date'] is None:
                #will put it in log file
                print('lower quality image has date, but higher quality does not. requiring manual user check !!')
            return True
    return False

def remove_jpeg_duplicates(file_metadata_list):
    is_jpeg = lambda f: f["ext"] in [".jpg", ".jpeg"]
    jpeg_files = filter(is_jpeg, file_metadata_list)

    # Sort by hash to group duplicates together
    sorted_jpegs = sorted(jpeg_files, key=itemgetter("hash"))

    # Group by hash and take the first file from each group
    unique_jpegs = [next(group) for _, group in groupby(sorted_jpegs, key=itemgetter("hash"))]

    # Keep non-jpegs unchanged
    non_jpegs = filter(lambda f: f["ext"] not in [".jpg", ".jpeg"], file_metadata_list)

    # Combine and return
    return list(non_jpegs) + unique_jpegs

def remove_heic_duplicates(file_metadata_list):
    """
    Remove duplicate HEIC files based on their hash.
    
    Args:
        file_metadata_list (list): List of file metadata dictionaries.
        
    Returns:
        list: List of file metadata dictionaries with duplicates removed.
    """
    is_heic = lambda f: f["ext"] == ".heic"
    heic_files = filter(is_heic, file_metadata_list)

    # Sort by hash to group duplicates together
    sorted_heics = sorted(heic_files, key=itemgetter("hash"))

    # Group by hash and take the first file from each group
    unique_heics = [next(group) for _, group in groupby(sorted_heics, key=itemgetter("hash"))]

    # Keep non-heics unchanged
    non_heics = filter(lambda f: f["ext"] != ".heic", file_metadata_list)

    # Combine and return
    return list(non_heics) + unique_heics


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