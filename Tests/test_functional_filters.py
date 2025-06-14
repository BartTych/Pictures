import functional_filters
import catalog_generation
import os
import pathlib
import shutil
from datetime import datetime
import pytest

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

test_cases = [
    # Case 1: three valid files in July 2023
    (
        [
            ("file1.jpg", 48),
            ("file2.jpg", 34),
            ("file3.jpg", 54),

        ],
        [
            ("file1.jpg", 48),
            ("file2.jpg", 34),
            ("file3.jpg", 75),

        ],

        [
            {"file_path": "file3.jpg","hash":54},
        ] 
    ),
    (
        [
            ("file1.jpg", 48),
            ("file2.jpg", 34),

        ],
        [
            ("file1.jpg", 48),
            ("file2.jpg", 34),
            ("file3.jpg", 75),

        ],
        
        [      
        ] 
    ),
]

@pytest.mark.parametrize("cat, base, expected", test_cases)
def test_substract_one_catalog_from_the_othere(cat,base,expected):
    catalog = []
    for path,hash in cat:
        catalog.append({
            "file_path": path,
            "hash": hash
        })

    base_catalog = []
    for path,hash in base:
        base_catalog.append({
            "file_path": path,
            "hash": hash
        })

    result = functional_filters.substract_one_set_from_the_other(catalog, base_catalog)
    assert result == expected
    