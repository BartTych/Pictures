import pathlib
import shutil
import datetime
# adding Folder_2/subfolder to the system path
from Meta_extraction.heic_date import Read_heic


def test_read_date_heic(tmp_path):
    # Arrange
    test_data_dir = pathlib.Path(__file__).parent / "resources"
    
    src_image_1 = test_data_dir / "1.heic"  # or .heic if supported!
    src_image_2 = test_data_dir / "3.heic"  # or .heic if supported!
    src_image_3 = test_data_dir / "1_copy.heic"  # or .heic if supported!
    
    dst_image_1 = tmp_path / "1.heic"  # or .heic if supported!
    dst_image_2 = tmp_path / "3.heic"  # or .heic if supported!
    dst_image_3 = tmp_path / "1_copy.heic"  # or .heic if supported!
    

    shutil.copy(src_image_1, dst_image_1)
    shutil.copy(src_image_2, dst_image_2)
    shutil.copy(src_image_3, dst_image_3)
    
    # Act
    reader = Read_heic()
    result_date_1 = reader.read(str(dst_image_1))
    result_date_2 = reader.read(str(dst_image_2))
    result_date_3 = reader.read(str(dst_image_3))
    
    assert isinstance(result_date_1, datetime.datetime)
    assert isinstance(result_date_2, datetime.datetime)
    assert isinstance(result_date_3, datetime.datetime)
    
    assert result_date_1 == result_date_3
    assert result_date_1 != result_date_2 
    