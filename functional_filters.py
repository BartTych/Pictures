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
    extension = extension.lower() 
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
        if is_duplicate:
            pass
            # possible additional logic to keep file with date
        if not is_duplicate:
            kept.append(f)
            seen_hashes.append(current_hash)

    return kept + others

    
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


def substract_one_set_from_the_other(catalog, base_catalog):

    set_of_base_catalog = set()
    for n in base_catalog:
        set_of_base_catalog.add(n['hash'])

    new_catalog = [n for n in catalog if n['hash'] not in set_of_base_catalog]
    return new_catalog
    # works by createnig set of hashes from one catalog

    # [n in catalog if n['hash'] not in set_of_first_catolog]