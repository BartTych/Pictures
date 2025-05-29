
from multiprocessing import Pool, cpu_count
import os
from PIL import Image
import pillow_heif
pillow_heif.register_heif_opener()

from imagehash import phash

hash_list = []
duplicates_list = []
path = "/Users/bart_mac/Desktop/zdjecia_test/sandbox"

def hash_image(file_path):
    try:
        with Image.open(file_path) as img:
            return (phash(img), file_path, os.path.getsize(file_path))
    except Exception:
        return None

def detect_if_duplicate(hash_val, hash_list, toler=4):
    for i, (h, _, _) in enumerate(hash_list):
        if hash_val - h <= toler:
            return i
    return -1

if __name__ == '__main__':
    

    # Step 1: Collect all file paths
    file_paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.startswith('.'):
                file_paths.append(os.path.join(root, file))

    # Step 2: Parallel hash computation
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(hash_image, file_paths)

    # Step 3: Deduplication pass
    hash_list = []
    duplicates_list = []

    for item in results:
        if item is None:
            continue
        hash_val, file_path, file_size = item
        dup_index = detect_if_duplicate(hash_val, hash_list, toler=4)
        if dup_index != -1:
            existing_hash, existing_path, existing_size = hash_list[dup_index]
            if file_size > existing_size:
                duplicates_list.append((existing_path, file_path, existing_size, file_size))
                hash_list[dup_index] = (hash_val, file_path, file_size)
            else:
                duplicates_list.append((file_path, existing_path, file_size, existing_size))
        else:
            hash_list.append((hash_val, file_path, file_size))

    print("Unique files with their hashes:")
    for hash_value, file_path, file_size in hash_list:
        print(f"Hash: {hash_value}, File: {file_path}, Size: {file_size} bytes")

    print("\nDuplicates found:")
    for dup_file, kept_file, dup_size, kept_size in duplicates_list:
        print(f"Duplicate: {dup_file} (Size: {dup_size} bytes) kept: {kept_file} (Size: {kept_size} bytes)")




# solution to the problem of attaching metadata to images:
# proble is i add files with metadata to the input folder but there are alse copies without metadata
# so the logic of duplicates has to choose the one with metadata


# will include metadata in logic of what is a duplicate
# for the seme size it is easy, remove the one without metadata or random if both have metadata or not

# but for resized images there are two options:
# - if reduced resolution has metadata stop the program and ask user because it seems that he attached new metadata to smaller image by mistake
# - if reduced resolution has no metadata, remove it


# logics of what is a duplicate:
# jpeg can have have a exact copy or a resized version
# goal is to remove same size duplicates and remove resized duplicates

# heic can have a copy as heic or jpeg
# gaol is to remove heic duplicates and remove jpeg duplicates

# that logic is not exploring all possibilities jet
