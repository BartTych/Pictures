from Meta_extraction.mov_mp4_date import Read_mov_mp4
import pathlib
import shutil
import datetime

def test_read_date_mov_mp4(tmp_path):
    # Arrange
    test_data_dir = pathlib.Path(__file__).parent / "resources"
    
    src_vid_1 = test_data_dir / "745.mp4"  
    src_vid_2 = test_data_dir / "746_copy.mp4"      
    src_vid_3 = test_data_dir / "746.mp4"   
    src_vid_4 = test_data_dir / "785.mov"  
    src_vid_5 = test_data_dir / "786_copy.mov"  
    src_vid_6 = test_data_dir / "786.mov"  
    
    dst_vid_1 = tmp_path / "745.mp4"  
    dst_vid_2 = tmp_path / "746_copy.mp4"      
    dst_vid_3 = tmp_path / "746.mp4"   
    dst_vid_4 = tmp_path / "785.mov"  
    dst_vid_5 = tmp_path / "786_copy.mov"  
    dst_vid_6 = tmp_path / "786.mov"  
    
    

    shutil.copy(src_vid_1, dst_vid_1)
    shutil.copy(src_vid_2, dst_vid_2)
    shutil.copy(src_vid_3, dst_vid_3)
    shutil.copy(src_vid_4, dst_vid_4)
    shutil.copy(src_vid_5, dst_vid_5)
    shutil.copy(src_vid_6, dst_vid_6)
    
    # Act
    reader = Read_mov_mp4()
    result_date_1 = reader.read(str(dst_vid_1))
    result_date_2 = reader.read(str(dst_vid_2))
    result_date_3 = reader.read(str(dst_vid_3))
    result_date_4 = reader.read(str(dst_vid_4))
    result_date_5 = reader.read(str(dst_vid_5))
    result_date_6 = reader.read(str(dst_vid_6))
    
    # Assert
    assert isinstance(result_date_1,datetime.datetime)
    assert isinstance(result_date_2,datetime.datetime)
    assert isinstance(result_date_3,datetime.datetime)
    assert isinstance(result_date_4,datetime.datetime)
    assert isinstance(result_date_5,datetime.datetime)
    assert isinstance(result_date_6,datetime.datetime)

    # rownosci 
    assert result_date_1 != result_date_3
    assert result_date_2 == result_date_3
    assert result_date_4 != result_date_6
    assert result_date_5 == result_date_6 
    