import pathlib
import shutil
import pytest
import sys
# adding Folder_2/subfolder to the system path
sys.path.insert(0, pathlib.Path(__file__).parent/'Hash_generation')
from Hash_generation.jpeg_heic_hash import Generate_jpeg_heic_hash  # adjust import!

def test_generate_phash_on_copied_image(tmp_path):
    # Arrange
    test_data_dir = pathlib.Path(__file__).parent / "resources"
    
    src_image_1 = test_data_dir / "DSC_0007.JPG"  # or .heic if supported!
    src_image_2 = test_data_dir / "DSC_0008.JPG"  # or .heic if supported!
    src_image_3 = test_data_dir / "DSC_0007_copy.JPG"  # or .heic if supported!
    
    src_image_4 = test_data_dir / "1.heic"  # or .heic if supported!
    src_image_5 = test_data_dir / "3.heic"  # or .heic if supported!
    src_image_6 = test_data_dir / "1_copy.heic"  # or .heic if supported!
    
    dst_image_1 = tmp_path / "DSC_0007.JPG.jpg"
    dst_image_2 = tmp_path / "DSC_0008.JPG.jpg"
    dst_image_3 = tmp_path / "DSC_0007_copy.JPG.jpg"
    
    dst_image_4 = tmp_path / "1.heic"  # or .heic if supported!
    dst_image_5 = tmp_path / "3.heic"  # or .heic if supported!
    dst_image_6 = tmp_path / "1_copy.heic"  # or .heic if supported!
    

    shutil.copy(src_image_1, dst_image_1)
    shutil.copy(src_image_2, dst_image_2)
    shutil.copy(src_image_3, dst_image_3)
    shutil.copy(src_image_4, dst_image_4)
    shutil.copy(src_image_5, dst_image_5)
    shutil.copy(src_image_6, dst_image_6)
    
    # Act
    generator = Generate_jpeg_heic_hash()
    result_hash_1 = generator.generate(str(dst_image_1))
    result_hash_2 = generator.generate(str(dst_image_2))
    result_hash_3 = generator.generate(str(dst_image_3))
    result_hash_4 = generator.generate(str(dst_image_4))
    result_hash_5 = generator.generate(str(dst_image_5))
    result_hash_6 = generator.generate(str(dst_image_6))

    # Assert
    assert result_hash_1 is not None, "Hash should not be None"
    assert isinstance(result_hash_1, int), "Hash should be an integer"
    assert result_hash_1 != 0, "Hash should not be zero"
    assert result_hash_1 != result_hash_2, "Hash should be different for different pictures"
    assert result_hash_1 == result_hash_3, "Hash should be same for exact copy"

    assert result_hash_4 is not None, "Hash should not be None"
    assert isinstance(result_hash_4, int), "Hash should be an integer"
    assert result_hash_4 != 0, "Hash should not be zero"
    assert result_hash_4 != result_hash_5, "Hash should be different for different pictures"
    assert result_hash_4 == result_hash_6, "Hash should be same for exact copy"
