import pathlib
import shutil
import pytest
from Hash_generation.jpeg_heic_hash import Generate_jpeg_heic_hash  # adjust import!

def test_generate_phash_on_copied_image(tmp_path):
    # Arrange
    test_data_dir = pathlib.Path(__file__).parent / "resources"
    src_image_1 = test_data_dir / "DSC_0007.JPG"  # or .heic if supported!
    src_image_2 = test_data_dir / "DSC_0008.JPG"  # or .heic if supported!
    src_image_3 = test_data_dir / "DSC_0007_copy.JPG"  # or .heic if supported!
    

    dst_image_1 = tmp_path / "DSC_0007.JPG.jpg"
    dst_image_2 = tmp_path / "DSC_0008.JPG.jpg"
    dst_image_3 = tmp_path / "DSC_0007_copy.JPG.jpg"
    

    shutil.copy(src_image_1, dst_image_1)
    shutil.copy(src_image_2, dst_image_2)
    shutil.copy(src_image_3, dst_image_3)
    
    # Act
    generator = Generate_jpeg_heic_hash()
    result_hash_1 = generator.generate(str(dst_image_1))
    result_hash_2 = generator.generate(str(dst_image_2))
    result_hash_3 = generator.generate(str(dst_image_3))


    # Assert
    assert result_hash_1 is not None, "Hash should not be None"
    assert isinstance(result_hash_1, int), "Hash should be an integer"
    assert result_hash_1 != 0, "Hash should not be zero"
    assert result_hash_1 != result_hash_2, "Hash should be different for different pictures"
    assert result_hash_1 == result_hash_3, "Hash should be same for exact copy"
