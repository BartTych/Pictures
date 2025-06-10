
import pathlib
import shutil
import datetime

from Meta_extraction.avi_date import Read_avi

def test_read_date_avi(tmp_path):
    # Arrange
    test_data_dir = pathlib.Path(__file__).parent / "resources"
    
    src_vid_1 = test_data_dir / "800.avi"  
    src_vid_2 = test_data_dir / "1597.AVI"  
    src_vid_3 = test_data_dir / "1597_copy.AVI"  
    
    dst_vid_1 = tmp_path / "800.avi"  
    dst_vid_2 = tmp_path / "1597.AVI"  
    dst_vid_3 = tmp_path / "1597_copy.AVI"  
    
    shutil.copy(src_vid_1, dst_vid_1)
    shutil.copy(src_vid_2, dst_vid_2)
    shutil.copy(src_vid_3, dst_vid_3)
    
    # Act
    reader = Read_avi()
    result_date_1 = reader.read(str(dst_vid_1))
    result_date_2 = reader.read(str(dst_vid_2))
    result_date_3 = reader.read(str(dst_vid_3))
    
    # Assert
    assert isinstance(result_date_1,datetime.datetime)
    assert isinstance(result_date_2,datetime.datetime)
    assert isinstance(result_date_3,datetime.datetime)
    assert result_date_1 != result_date_2
    assert result_date_2 == result_date_3