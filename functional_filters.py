#from itertools import groupby
#from operator import itemgetter
from collections import defaultdict

# moge napisac nowy algorytm bo okazuje sie ze jednak ladnie mi usuwa copie z dystansem zero.
# jedynie dla zdjec chce miec sprawdzenie przez ORB newet jak odleglosc jest zero zeby niestracic czegosc fajnego 
def remove_duplicates_base_on_humming_distance(
    file_list: list[dict], 
    extension: str, 
    hamming_threshold: int
) -> list[dict]:
    """Removes duplicates for files with a given extension based on hash Hamming distance."""
    
    filtered = [f for f in file_list if f["ext"] == extension and f["hash"] is not None]
    others = [f for f in file_list if f["ext"] != extension or f["hash"] is None]

    kept = []
    seen_hashes = []

    for f in filtered:
        current_hash = f["hash"]
        is_duplicate = any(
            bin(current_hash ^ prev_hash).count("1") <= hamming_threshold
            for prev_hash in seen_hashes
        )
        if not is_duplicate:
            kept.append(f)
            seen_hashes.append(current_hash)

    return kept + others

def remove_jpegs_with_lower_coding_quality(images):
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
    
    return [
        img for img in images
        if not (
            (img["ext"] == ".jpeg" or img["ext"] == ".jpg")
            and has_same_resolution_duplicate_with_higher_coding_quality(img, images)
        )
    ]
    
def remove_jpegs_converted_from_heic_based_on_metadata(file_list):
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





def check_for_copies_without_date(file_list):
    
    file_list = [n for n in file_list if n['date']!= None]
    # Group by hash
    hash_groups = defaultdict(list)
    for img in file_list:
        hash_groups[img['hash']].append(img)

    group_lenght = {}
    same_date = 0
    missing_date = 0
    for group in hash_groups.values():
        group_lenght[len(group)] = group_lenght.get(len(group),0) + 1
        if all([g['date']!= None for g in group]):
            same_date += 1
        else:
            missing_date += 1
        
    return same_date, missing_date, group_lenght
#chatGPT
def remove_exact_duplicates(images):
    def hamming_distance(hash1, hash2):
        return bin(int(hash1, 16) ^ int(hash2, 16)).count('1')

    # Group by hash
    hash_groups = defaultdict(list)
    for img in images:
        hash_groups[img['hash']].append(img)

    deduped = []
    for group in hash_groups.values():
        if len(group) == 1:
            deduped.append(group[0])
            continue

        # If multiple images have the same hash (hamming distance 0)
        # and only one has a 'date', keep that one
        with_date = [img for img in group if 'date' in img and img['date']]
        without_date = [img for img in group if 'date' not in img or not img['date']]

        if len(with_date) == 1:
            deduped.append(with_date[0])
        else:
            # If none or multiple have 'date', just keep the first
            deduped.append(group[0])

    return deduped

