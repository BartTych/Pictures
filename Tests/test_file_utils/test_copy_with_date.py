import os
from datetime import datetime
import pytest

from file_utils import copy_files_with_date  # Update with correct import

test_cases = [
    # Case 1: three valid files in July 2023
    (
        [
            ("file1.jpg", datetime(2023, 7, 25)),
            ("file2.jpg", datetime(2023, 7, 11)),
            ("file3.jpg", datetime(2023, 7, 2)),

        ],
        {
            (2023, 7): ["1.jpg", "2.jpg","3.jpg"],
        }
    ),
    # Case 2: one file with None date should be skipped
    (
        [
            ("file1.jpg", datetime(2023, 8, 5)),
            ("file2.jpg", None),
        ],
        {
            (2023, 8): ["1.jpg"]
        }
    ),
    # Case 3: more complex case
    (
        [
            ("file1.jpg", datetime(2023, 7, 24)),
            ("file2.jpg", datetime(2023, 7, 7)),
            ("file3.jpg", datetime(2023, 7, 25)),
            ("file4.jpg", datetime(2023, 7, 5)),
            ("file3.jpg", datetime(2023, 8, 25)),
            ("file6.jpg", datetime(2023, 8, 25)),
            ("file7.jpg", datetime(2022, 8, 25)),
            ("file8.jpg", datetime(2023, 8, 25)),
            ("file9.jpg", datetime(2023, 8, 25)),

        ],
        {
            (2023, 7): ["1.jpg", "2.jpg","3.jpg", "4.jpg"],
            (2023, 8): ["1.jpg", "2.jpg","3.jpg", "4.jpg"],
            (2022, 8): ["1.jpg"],
        }
    ),
    
]
 
def create_catalog(tmp_path, entries):
    catalog = []
    for i, (filename, date) in enumerate(entries):
        dummy_hash = f"dummyhash{i:03d}"
        file_path = tmp_path / f"{i:02d}_{filename}"
        #file_path = tmp_path / filename
    
        catalog.append({
            "file_path": str(file_path),
            "ext": ".jpg",
            "date": date,
            "resolution": (0, 0),
            "size": i,
            "hash": dummy_hash
        })
    return catalog
    
def create_test_files(tmp_path, entries):
    for i, (filename, date) in enumerate(entries):
        dummy_hash = f"dummyhash{i:03d}"
        #file_path = tmp_path / filename
        file_path = tmp_path / f"{i:02d}_{filename}"
        if date != None:
            content = f"date={date.isoformat()};hash={dummy_hash}"
            file_path.write_text(content)
  
@pytest.mark.parametrize("entries, expected_structure", test_cases)
def test_correct_folder_structure(tmp_path, entries, expected_structure):
    catalog = create_catalog(tmp_path, entries)
    create_test_files(tmp_path, entries)

    output_path = tmp_path / "output"
    copy_files_with_date(str(output_path), catalog)
    
    for (year, month), expected_files in expected_structure.items():
        folder = output_path / f"{year:04d}" / f"{month:02d}"
        assert folder.exists(), f"Expected folder {folder} to exist"

@pytest.mark.parametrize("entries, expected_structure", test_cases)
def test_correct_naming_and_count(tmp_path, entries, expected_structure):
    catalog = create_catalog(tmp_path, entries)
    create_test_files(tmp_path, entries)

    output_path = tmp_path / "output"
    copy_files_with_date(str(output_path), catalog)

    for (year, month), expected_files in expected_structure.items():
        
        folder = output_path / f"{year:04d}" / f"{month:02d}"
        
        # check if number of files is correct and name are as expected 
        actual_files = sorted(os.listdir(folder))
        assert actual_files == sorted(expected_files)

@pytest.mark.parametrize("entries, expected_structure", test_cases)
def test_files_are_in_correct_folders(tmp_path, entries, expected_structure):
    catalog = create_catalog(tmp_path, entries)
    create_test_files(tmp_path, entries)

    output_path = tmp_path / "output"
    copy_files_with_date(str(output_path), catalog)

    for (year, month), expected_files in expected_structure.items():
        
        folder = output_path / f"{year:04d}" / f"{month:02d}" 
        actual_files = sorted(os.listdir(folder))
        
        # check if files have date from folder
         
        
        for actual_file in actual_files :    
            file_content = (folder/actual_file).read_text()
            parts = dict(x.split("=") for x in file_content.split(";"))
            date = datetime.fromisoformat(parts["date"])
            
            assert date.year == year, print('File year incorrect')
            assert date.month == month, print('File month incorrect')

@pytest.mark.parametrize("entries, expected_structure", test_cases)
def test_correct_order_of_files_in_folders(tmp_path, entries, expected_structure):
    catalog = create_catalog(tmp_path, entries)
    create_test_files(tmp_path, entries)

    output_path = tmp_path / "output"
    copy_files_with_date(str(output_path), catalog)

    for (year, month), expected_files in expected_structure.items():
        
        folder = output_path / f"{year:04d}" / f"{month:02d}" 
        actual_files = sorted(os.listdir(folder))
        
        # check if files have date from folder
        # and are ordered correctly 
        dates = []
        for actual_file in actual_files :    
            file_content = (folder/actual_file).read_text()
            parts = dict(x.split("=") for x in file_content.split(";"))
            date = datetime.fromisoformat(parts["date"])
            dates.append(date)
        #check correct order in folder
        assert dates == sorted(dates)     

@pytest.mark.parametrize("entries, expected_structure", test_cases)
def test_each_file_with_date_copied(tmp_path, entries, expected_structure):
    catalog = create_catalog(tmp_path, entries)
    create_test_files(tmp_path, entries)

    output_path = tmp_path / "output"
    copy_files_with_date(str(output_path), catalog)

    set_of_copied_file_hashes = set()
    for (year, month), expected_files in expected_structure.items():
        
        folder = output_path / f"{year:04d}" / f"{month:02d}" 
        actual_files = sorted(os.listdir(folder))
         
        for actual_file in actual_files :    
            file_content = (folder/actual_file).read_text()
            parts = dict(x.split("=") for x in file_content.split(";"))
            hash = parts["hash"]
            set_of_copied_file_hashes.add(hash)
    
    set_of_originall_files_hashes = set()
    for file in catalog:
        if file['date'] != None:
            file_content = (tmp_path/file['file_path']).read_text()
            parts = dict(x.split("=") for x in file_content.split(";"))
            hash = parts["hash"]
            set_of_originall_files_hashes.add(hash)

    assert set_of_originall_files_hashes == set_of_copied_file_hashes,print('Not all files where copied')
        