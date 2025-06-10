from Hash_generation.mov_avi_mp4_hash import Generate_mov_avi_mp4_hash
import pathlib
import shutil

def test_generate_phash_on_copied_image(tmp_path):
    # Arrange
    test_data_dir = pathlib.Path(__file__).parent / "resources"
    
    src_vid_1 = test_data_dir / "745.mp4"  
    src_vid_2 = test_data_dir / "746_copy.mp4"      
    src_vid_3 = test_data_dir / "746.mp4"   
    src_vid_4 = test_data_dir / "785.mov"  
    src_vid_5 = test_data_dir / "786_copy.mov"  
    src_vid_6 = test_data_dir / "786.mov"  
    src_vid_7 = test_data_dir / "800.avi"  
    src_vid_8 = test_data_dir / "1597.AVI"  
    src_vid_9 = test_data_dir / "1597_copy.AVI"  
    
    dst_vid_1 = tmp_path / "745.mp4"  
    dst_vid_2 = tmp_path / "746_copy.mp4"      
    dst_vid_3 = tmp_path / "746.mp4"   
    dst_vid_4 = tmp_path / "785.mov"  
    dst_vid_5 = tmp_path / "786_copy.mov"  
    dst_vid_6 = tmp_path / "786.mov"  
    dst_vid_7 = tmp_path / "800.avi"  
    dst_vid_8 = tmp_path / "1597.AVI"  
    dst_vid_9 = tmp_path / "1597_copy.AVI"  
    
    shutil.copy(src_vid_1, dst_vid_1)
    shutil.copy(src_vid_2, dst_vid_2)
    shutil.copy(src_vid_3, dst_vid_3)
    shutil.copy(src_vid_4, dst_vid_4)
    shutil.copy(src_vid_5, dst_vid_5)
    shutil.copy(src_vid_6, dst_vid_6)
    shutil.copy(src_vid_7, dst_vid_7)
    shutil.copy(src_vid_8, dst_vid_8)
    shutil.copy(src_vid_9, dst_vid_9)
    
    # Act
    generator = Generate_mov_avi_mp4_hash()
    result_hash_1 = generator.generate(str(dst_vid_1))
    result_hash_2 = generator.generate(str(dst_vid_2))
    result_hash_3 = generator.generate(str(dst_vid_3))
    result_hash_4 = generator.generate(str(dst_vid_4))
    result_hash_5 = generator.generate(str(dst_vid_5))
    result_hash_6 = generator.generate(str(dst_vid_6))
    result_hash_7 = generator.generate(str(dst_vid_7))
    result_hash_8 = generator.generate(str(dst_vid_8))
    result_hash_9 = generator.generate(str(dst_vid_9))

    # Assert
    assert result_hash_1 is not None, "Hash should not be None"
    assert result_hash_2 is not None, "Hash should not be None"
    assert result_hash_3 is not None, "Hash should not be None"
    assert result_hash_4 is not None, "Hash should not be None"
    assert result_hash_5 is not None, "Hash should not be None"
    assert result_hash_6 is not None, "Hash should not be None"
    
    assert isinstance(result_hash_1, int), "Hash should be an integer"
    assert isinstance(result_hash_2, int), "Hash should be an integer"
    assert isinstance(result_hash_3, int), "Hash should be an integer"
    assert isinstance(result_hash_4, int), "Hash should be an integer"
    assert isinstance(result_hash_5, int), "Hash should be an integer"
    assert isinstance(result_hash_6, int), "Hash should be an integer"

    assert result_hash_1 != 0, "Hash should not be zero"
    assert result_hash_2 != 0, "Hash should not be zero"
    assert result_hash_3 != 0, "Hash should not be zero"
    assert result_hash_4 != 0, "Hash should not be zero"
    assert result_hash_5 != 0, "Hash should not be zero"
    assert result_hash_6 != 0, "Hash should not be zero"

    assert result_hash_1 != result_hash_3, "Hash should be different for different mp4"
    assert result_hash_2 == result_hash_3, "Hash should be same for exact copy"
    
    assert result_hash_4 != result_hash_6, "Hash should be different for different mp4"
    assert result_hash_5 == result_hash_6, "Hash should be same for exact copy"
    
    assert result_hash_8 == result_hash_9
    assert result_hash_7 != result_hash_8