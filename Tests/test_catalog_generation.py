import pytest
import catalog_generation
import pathlib
import os
import shutil

@pytest.mark.parametrize(
    "file_structure, extensions, expected_count, expected_files",
    [
        # Test 1: flat dir, 2 jpg, 1 pdf
        (
            {
                "image1.jpg": None,
                "image2.jpg": None,
                "document.pdf": None,
            },
            {".jpg"},
            2,
            {"image1.jpg", "image2.jpg"},
        ),
        # Test 2: nested dir, 1 jpg inside subfolder
        (
            {
                "subfolder/image3.jpg": None,
                "subfolder/readme.txt": None,
            },
            {".jpg"},
            1,
            {"subfolder/image3.jpg"},
        ),
        # Test 3: no matching files
        (
            {
                "file1.txt": None,
                "file2.md": None,
            },
            {".jpg"},
            0,
            set(),
        ),
        # Test 4: mixed files + hidden file
        (
            {
                "img1.png": None,
                "img2.png": None,
                ".hiddenfile.png": None,
                "doc.md": None,
            },
            {".png"},
            2,
            {"img1.png", "img2.png"},
        ),
    ]
)

def test_read_all_file_paths_with_extentions_parametrized(
    tmp_path, file_structure, extensions, expected_count, expected_files
):
    # Arrange: create the file structure
    for rel_path in file_structure.keys():
        file_path = tmp_path / rel_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()  # Create empty file
    
    # Act
    result = catalog_generation.read_all_file_paths_with_extentions(
        tmp_path,
        extentions=extensions
    )
    
    # Assert
    assert len(result) == expected_count
    result_files = {str(path).replace(str(tmp_path) + "/", "") for path in result}
    assert result_files == expected_files

def test_creation_of_catalog(tmp_path):
    extensions = {
    '.jpg', '.jpeg', '.mov', '.mp4', '.avi','.heic','.mov', '.mp4', '.avi'
}
    test_data_dir = pathlib.Path(__file__).parent / "resources"
    files = catalog_generation.read_all_file_paths_with_extentions(test_data_dir,extensions)
    for file in files:
        name = os.path.basename(file)
        shutil.copy2(file,tmp_path / name)
    
    catalog = catalog_generation.generate_catalog(tmp_path,extensions)

    
    assert len(catalog) == len(files)
    for n in catalog:
        assert isinstance(n,dict)