
import catalog_test_generation
import functional_filters



path = '/Users/bart_mac/Desktop/zdjecia_test/sandbox'
catalog = catalog_test_generation.generate_catalog(path)

sorted(catalog, key=lambda x: x["date"] if x["date"] is not None else 0)

for file_data in catalog:
    print(f"File: {file_data["file_path"]}, Date: {file_data["date"]}, Resolution: {file_data["resolution"]},size: {file_data["size"]}, Hash: {file_data["hash"]}")

print(f"Total files processed: {len(catalog)}")
print(f"file with hash: {len([f for f in catalog if f["hash"] is not None])}")
print(f"file with date: {len([f for f in catalog if f["date"] is not None])}")
print(f"file with resolution: {len([f for f in catalog if f["resolution"] is not None])}")


catalog = functional_filters.remove_same_res_jpegs_with_lower_coding_quality(catalog)
catalog = functional_filters.remove_converted_jpegs_with_metadata(catalog)

catalog = functional_filters.remove_jpeg_duplicates(catalog)
catalog = functional_filters.remove_heic_duplicates(catalog)



for file_data in catalog:
    print(f"File: {file_data["file_path"]}, Date: {file_data["date"]}, Resolution: {file_data["resolution"]},size: {file_data["size"]}, Hash: {file_data["hash"]}")

print(f"Total files processed: {len(catalog)}")
print(f"file with hash: {len([f for f in catalog if f["hash"] is not None])}")
print(f"file with date: {len([f for f in catalog if f["date"] is not None])}")
print(f"file with resolution: {len([f for f in catalog if f["resolution"] is not None])}")
