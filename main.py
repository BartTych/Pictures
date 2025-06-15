
#from catalog_test_generation import FileMetadataExtractor
import functional_filters
import pickle

import file_utils

import time



from catalog_generation import generate_catalog

path = '/Users/bart_mac/Desktop/05'
destination = '/Users/bart_mac/Desktop/new_05'
destination_no_date = '/Users/bart_mac/Desktop/new_05_no_date'

extensions = {
    '.jpg', '.jpeg', '.mov', '.mp4', '.avi','.heic','.mov', '.mp4', '.avi'
}

start = time.perf_counter()

# to wymaga sprawdzenia unit testami 
catalog = generate_catalog(path, extensions = extensions)

#catalog = pickle.load(open("catalog.pkl", "rb"))


end = time.perf_counter()

elapsed = end - start
num_files = len(catalog)
per_file = elapsed / num_files if num_files else 0

print(f"\nProcessed {num_files} files in {elapsed:.2f} seconds.")
print(f"Average time per file: {per_file:.4f} seconds.")

# picle catalog 
#pickle.dump(catalog, open("catalog.pkl", "wb"))

#sorted(catalog, key=lambda x: x["date"] if x["date"] is not None else 0)

#remove no hash files
#catalog = [n for n in catalog if n['hash'] == None]
#catalog = [n for n in catalog if n['hash'] != None]

for n in catalog:
    print(n['file_path'])

print(f"Total files processed: {len(catalog)}")

#for n in catalog:
#    print(f"{n['hash']}")


#same_date,missing_date,lenght_dict = functional_filters.check_for_copies_without_date(catalog)
#print(f"same date: {same_date} missing_date {missing_date}")

#powtorzenia = sorted(list(lenght_dict.items()))

#for n, m in powtorzenia:
#    print(f"lenght {n} ilosc {m}")

#catalog = functional_filters.remove_jpegs_with_lower_coding_quality(catalog)

#catalog = functional_filters.remove_duplicates_base_on_humming_distance(catalog,'.mov', 0)    
#catalog = functional_filters.remove_duplicates_base_on_humming_distance(catalog,'.avi', 0)    
#catalog = functional_filters.remove_duplicates_base_on_humming_distance(catalog,'.mp4', 0)    
#catalog = functional_filters.remove_duplicates_base_on_humming_distance(catalog,'.heic', 0)    
#catalog = functional_filters.remove_duplicates_base_on_humming_distance(catalog,'.jpeg', 0)    
#catalog = functional_filters.remove_duplicates_base_on_humming_distance(catalog,'.jpg', 0)    

#catalog = [n for n in catalog if n['date']== None]


file_utils.copy_files_with_date(destination, catalog)
file_utils.copy_files_without_date(destination_no_date, catalog)

#print(f"length: {len(catalog)}")



