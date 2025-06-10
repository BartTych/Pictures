
from Resolution_reader.mov_avi_mp4_resolution import Read_mov_avi_mp4_resolution
import pathlib
import shutil

def test_read_resolution_on_copied_image(tmp_path):
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
    reader = Read_mov_avi_mp4_resolution()
    result_resolution_1 = reader.read_resolution(str(dst_vid_1))
    result_resolution_2 = reader.read_resolution(str(dst_vid_2))
    result_resolution_3 = reader.read_resolution(str(dst_vid_3))
    result_resolution_4 = reader.read_resolution(str(dst_vid_4))
    result_resolution_5 = reader.read_resolution(str(dst_vid_5))
    result_resolution_6 = reader.read_resolution(str(dst_vid_6))
    result_resolution_7 = reader.read_resolution(str(dst_vid_7))
    result_resolution_8 = reader.read_resolution(str(dst_vid_8))
    result_resolution_9 = reader.read_resolution(str(dst_vid_9))

    # Assert
    assert result_resolution_1 is not None, "Hash should not be None"
    assert result_resolution_2 is not None, "Hash should not be None"
    assert result_resolution_3 is not None, "Hash should not be None"
    assert result_resolution_4 is not None, "Hash should not be None"
    assert result_resolution_5 is not None, "Hash should not be None"
    assert result_resolution_6 is not None, "Hash should not be None"
    assert result_resolution_7 is not None, "Hash should not be None"
    assert result_resolution_8 is not None, "Hash should not be None"
    assert result_resolution_9 is not None, "Hash should not be None"
    
    assert result_resolution_1 != 0, "Hash should not be zero"
    assert result_resolution_2 != 0, "Hash should not be zero"
    assert result_resolution_3 != 0, "Hash should not be zero"
    assert result_resolution_4 != 0, "Hash should not be zero"
    assert result_resolution_5 != 0, "Hash should not be zero"
    assert result_resolution_6 != 0, "Hash should not be zero"
    assert result_resolution_7 != 0, "Hash should not be zero"
    assert result_resolution_8 != 0, "Hash should not be zero"
    assert result_resolution_9 != 0, "Hash should not be zero"

    assert result_resolution_1 == {'height':1280,'width': 720}
    assert result_resolution_2 == {'height':1280,'width': 720}
    assert result_resolution_3 == {'height':1280,'width': 720}
    assert result_resolution_4 == {'height':1080,'width': 1920}
    assert result_resolution_5 == {'height':1080,'width': 1920}
    assert result_resolution_6 == {'height':1080,'width': 1920}
    assert result_resolution_7 == {'height':480,'width': 640}
    assert result_resolution_8 == {'height':480,'width': 640}
    assert result_resolution_9 == {'height':480,'width': 640}
    

    '''
    import pathlib
    import shutil
    import pytest
    from Resolution_reader.mov_avi_mp4_resolution import Read_mov_avi_mp4_resolution

    @pytest.mark.parametrize("filename, expected_resolution", [
    ("745.mp4", {'height':1280,'width':720}),
    ("746_copy.mp4", {'height':1280,'width':720}),
    ("746.mp4", {'height':1280,'width':720}),
    ("785.mov", {'height':1080,'width':1920}),
    ("786_copy.mov", {'height':1080,'width':1920}),
    ("786.mov", {'height':1080,'width':1920}),
    ("800.avi", {'height':480,'width':640}),
    ("1597.AVI", {'height':480,'width':640}),
    ("1597_copy.AVI", {'height':480,'width':640}),
    ])
    
    def test_read_resolution_on_copied_video(tmp_path, filename, expected_resolution):
    # Arrange
    test_data_dir = pathlib.Path(__file__).parent / "resources"
    src_video = test_data_dir / filename
    dst_video = tmp_path / filename
    shutil.copy(src_video, dst_video)
    
    # Act
    generator = Read_mov_avi_mp4_resolution()
    result_resolution = generator.read_resolution(str(dst_video))
    
    # Assert
    assert result_resolution is not None, "Resolution should not be None"
    assert result_resolution != 0, "Resolution should not be zero"
    assert result_resolution == expected_resolution
    '''