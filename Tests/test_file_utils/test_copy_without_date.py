import os
from datetime import datetime
import pytest

from file_utils import copy_files_without_date

cases = [
    # Case 1: two valid files in July 2023
    (
        [
            ("file1.jpg", datetime(2014,7,8)),
            ("file2.jpg", None),
            ("file3.jpg", None),
        ],
        ["file2.jpg", "file3.jpg"]
    ),
    # Case 2: one file with None date should be skipped
    (
        [
            ("file1.jpg", None),
            ("file2.jpg", None),
            ("file2.jpg", None)
        ],
        ["file1.jpg","file2.jpg","file2_1.jpg"]
    ),
]

@pytest.mark.parametrize("entries, expected_files",cases)
def test_expected_files_exist(tmp_path,entries,expected_files):
    catalog = []

    for i, (filename, date) in enumerate(entries):
        file_path = tmp_path / filename
        file_path.write_text(f"file content {i+1}")
        catalog.append({
            "file_path": str(file_path),
            "ext": ".jpg",
            "date": date,
            "resolution": (0, 0),
            "size": file_path.stat().st_size,
            "hash": f"dummyhash{i}"
        })

    output_path = tmp_path / "output"
    copy_files_without_date(str(output_path), catalog)

    assert output_path.exists()
    actual_files = sorted(os.listdir(output_path))
    assert actual_files == expected_files

@pytest.mark.parametrize("entries, expected_files",cases)
def test_all_files_are_copied(tmp_path,entries,expected_files):
    catalog = []

    for i, (filename, date) in enumerate(entries):
        file_path = tmp_path / filename
        file_path.write_text(f"file content {i+1}")
        catalog.append({
            "file_path": str(file_path),
            "ext": ".jpg",
            "date": date,
            "resolution": (0, 0),
            "size": file_path.stat().st_size,
            "hash": f"dummyhash{i}"
        })

    output_path = tmp_path / "output"
    copy_files_without_date(str(output_path), catalog)

    set_of_copied_file_hashes = set()
    
    folder = output_path 
    actual_files = sorted(os.listdir(folder))
    
    for actual_file in actual_files :    
        hash = (folder/actual_file).read_text()
        set_of_copied_file_hashes.add(hash)

    set_of_originall_files_hashes = set()
    for file in catalog:
        if file['date'] == None:
            hash = (tmp_path/file['file_path']).read_text()
            set_of_originall_files_hashes.add(hash)
    
    assert set_of_copied_file_hashes == set_of_originall_files_hashes
