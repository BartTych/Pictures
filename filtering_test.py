
#from catalog_test_generation import FileMetadataExtractor
import functional_filters


import time



from catalog_test_generation import generate_catalog

path = '/Users/bart_mac/Desktop/zdjecia_test/sandbox'

extensions = {
    '.jpg', '.jpeg', '.mov', '.mp4', '.avi','.heic'
}
extensions = {
    '.mov', '.mp4', '.avi'
}

start = time.perf_counter()
catalog = generate_catalog(path,max_workers=6,extensions = extensions)

end = time.perf_counter()

elapsed = end - start
num_files = len(catalog)
per_file = elapsed / num_files if num_files else 0

print(f"\nProcessed {num_files} files in {elapsed:.2f} seconds.")
print(f"Average time per file: {per_file:.4f} seconds.")

#sorted(catalog, key=lambda x: x["date"] if x["date"] is not None else 0)

print(f"Total files processed: {len(catalog)}")

catalog = functional_filters.remove_same_res_jpegs_with_lower_coding_quality(catalog)
catalog = functional_filters.remove_converted_jpegs_with_metadata(catalog)# that requires no meta data handling

# Remove copies besed on hash and extension
for ext in extensions:
    catalog = functional_filters.remove_duplicates_with_given_ext(catalog, ext)


# what filers for pictures are missing?
# looks good for now

# movies
# one method to remove duplicates with same ext and hash.

#for file_data in catalog:
#    print(f"File: {file_data["file_path"]}, Date: {file_data["date"]}, Resolution: {file_data["resolution"]},size: {file_data["size"]}, Hash: {file_data["hash"]}")

print(f"Total files processed: {len(catalog)}")

