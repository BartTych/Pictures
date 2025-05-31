import os
from multiprocessing import Pool, cpu_count
import load_date_extractors
import load_resolution_readers
import load_hash_generators
import file_date_extractor
import file_hash_generator
import file_resolution_reader

from concurrent.futures import ThreadPoolExecutor

# Initialize once
date_extractors = load_date_extractors.load_all_handlers()
hash_generators = load_hash_generators.load_all_generators()
resolution_readers = load_resolution_readers.load_all_readers()

date_extractor = file_date_extractor.file_meta_extractor(date_extractors)
hash_generator = file_hash_generator.file_hash_generator(hash_generators)
resolution_reader = file_resolution_reader.file_resolution_reader(resolution_readers)

def process_file(filepath):
    result = {
        "file_path": filepath,
        "ext": os.path.splitext(filepath)[1].lower(),
        "date": date_extractor.apply(filepath),
        "resolution": resolution_reader.apply(filepath),
        "size": os.path.getsize(filepath) if os.path.exists(filepath) else None,
        "hash": hash_generator.apply(filepath)
    }
    print(f"Processed {filepath}")
    return result


def generate_catalog(path, max_workers=8, extensions=None):
    
    file_paths = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(path)
        for file in files
        if not file.startswith('.') and os.path.splitext(file)[1].lower() in extensions
    ]

    #with Pool(processes=max_workers) as pool:
    #    catalog = pool.map(process_file, file_paths)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        catalog = list(executor.map(process_file, file_paths))


    return catalog