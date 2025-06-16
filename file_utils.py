
import os
import shutil
from collections import defaultdict
from datetime import datetime

def copy_files_with_date(path, catalog):
    # Group by (year, month)
    length = len([n for n in catalog if n['date'] != None])
    left_to_copy = length
    grouped = defaultdict(list)
    for entry in catalog:
        date = entry["date"]
        if date is None:
            continue  # Skip files without a valid date
        year_month = (date.year, date.month)
        grouped[year_month].append(entry)

    for (year, month), entries in grouped.items():
        # Sort entries by exact date
        entries.sort(key=lambda x: x["date"])
        
        # Create target directory
        folder = os.path.join(path, f"{year:04d}", f"{month:02d}")
        os.makedirs(folder, exist_ok=True)

        # Rename and copy
        for i, entry in enumerate(entries, 1):
            ext = entry["ext"]
            new_filename = f"{i}{ext}"
            dst_path = os.path.join(folder, new_filename)
            print(f"{left_to_copy} / {length}")
            print(entry["file_path"])
            shutil.copy2(entry["file_path"], dst_path)
            left_to_copy += -1

def copy_files_without_date(path, catalog):
    os.makedirs(path, exist_ok=True)
    length = len([n for n in catalog if n['date'] != None])
    left_to_copy = length
    for entry in catalog:
        if entry["date"] is not None:
            continue

        src = entry["file_path"]
        base = os.path.basename(src)
        name, ext = os.path.splitext(base)
        dst = os.path.join(path, base)

        counter = 1
        while os.path.exists(dst):
            dst = os.path.join(path, f"{name}_{counter}{ext}")
            counter += 1
        print(f"{left_to_copy} / {length}")
        print(src)
        shutil.copy2(src, dst)
        left_to_copy += -1