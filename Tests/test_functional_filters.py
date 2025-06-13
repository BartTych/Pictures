import functional_filters
import catalog_generation
import os
import pathlib
import shutil

def test_remove_duplicates_based_on_humming_distance(tmp_path):
    extensions = {
    '.jpg', '.jpeg', '.mov', '.mp4', '.avi','.heic','.mov', '.mp4', '.avi'
}
    test_data_dir = pathlib.Path(__file__).parent / "resources"
    files = catalog_generation.read_all_file_paths_with_extentions(test_data_dir,extensions)
    for file in files:
        name = os.path.basename(file)
        shutil.copy2(file,tmp_path / name)
    
    catalog = catalog_generation.generate_catalog(tmp_path,extensions)

    # do sprawdzenia co sie dzieje jak dam duze litery
    assert len(functional_filters.remove_duplicates_base_on_humming_distance(catalog,".avi",0)) == len(catalog) - 1
    assert len(functional_filters.remove_duplicates_base_on_humming_distance(catalog,".mov",0)) == len(catalog) - 1
    assert len(functional_filters.remove_duplicates_base_on_humming_distance(catalog,".mp4",0)) == len(catalog) - 1
    assert len(functional_filters.remove_duplicates_base_on_humming_distance(catalog,".jpeg",0)) == len(catalog)
    assert len(functional_filters.remove_duplicates_base_on_humming_distance(catalog,".jpg",0)) == len(catalog) - 1
    assert len(functional_filters.remove_duplicates_base_on_humming_distance(catalog,".JPG",0)) == len(catalog) - 1
    assert len(functional_filters.remove_duplicates_base_on_humming_distance(catalog,".heic",0)) == len(catalog) - 1
    assert len(functional_filters.remove_duplicates_base_on_humming_distance(catalog,".HEIC",0)) == len(catalog) - 1
    assert len(functional_filters.remove_jpegs_converted_from_heic_based_on_metadata(catalog)) == len(catalog) - 1
    
def test_removing_jpeg_converted_from_heic(tmp_path):
    extensions = {
    '.jpg', '.jpeg', '.mov', '.mp4', '.avi','.heic','.mov', '.mp4', '.avi'
}
    test_data_dir = pathlib.Path(__file__).parent / "resources"
    files = catalog_generation.read_all_file_paths_with_extentions(test_data_dir,extensions)
    for file in files:
        name = os.path.basename(file)
        shutil.copy2(file,tmp_path / name)
    
    catalog = catalog_generation.generate_catalog(tmp_path,extensions)

    assert len(functional_filters.remove_jpegs_converted_from_heic_based_on_metadata(catalog)) == len(catalog) - 1