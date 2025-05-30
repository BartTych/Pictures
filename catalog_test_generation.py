import load_date_extractors
import load_resolution_readers
import load_hash_generators

import file_date_extractor as file_date_extractor
import file_hash_generator as file_hash_generator
import file_resolution_reader as file_resolution_reader
from multiprocessing import Pool, cpu_count

import os

date_extractors = load_date_extractors.load_all_handlers()
hash_generators = load_hash_generators.load_all_generators()
resolution_readers = load_resolution_readers.load_all_readers()

date_extractor = file_date_extractor.file_meta_extractor(date_extractors)
hash_generator = file_hash_generator.file_hash_generator(hash_generators)
resolution_reader = file_resolution_reader.file_resolution_reader(resolution_readers)



def process_file(filepath):
    return {
        "file_path": filepath,
        "ext": os.path.splitext(filepath)[1].lower(),
        "date": date_extractor.apply(filepath),
        "resolution": resolution_reader.apply(filepath),
        "size": os.path.getsize(filepath) if os.path.exists(filepath) else None,
        "hash": hash_generator.apply(filepath)
    }

path = '/Users/bart_mac/Desktop/zdjecia_test/sandbox'
def generate_catalog(path):
    """
    Generate catalog of files in the given path.
    
    Args:
        path (str): Path to the directory containing files.
        
    Returns:
        list: List of tuples containing file metadata.
    """
   
    file_paths = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(path)
        for file in files if not file.startswith('.') and os.path.splitext(file)[1].lower() in {'.jpg', '.jpeg', '.heic', '.mov', '.mp4', '.avi'}
    ]

    catalog = []

    #if __name__ == "__main__":
    #    with Pool(processes = 7) as pool:
    #        catalog = pool.map(process_file, file_paths) 
    
    for file in file_paths:
        try:
            catalog.append(process_file(file))
        except:
            print(f"Error processing file {file}: {e}")
    #print(f"Total files processed: {len(catalog)}")


    return catalog

    