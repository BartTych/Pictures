import pathlib
import shutil
import datetime
from Meta_extraction.jpeg_date import Read_jpeg  # adjust import!


def test_read_date_jpeg(tmp_path):
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
    reader = Read_jpeg()
    result_date_1 = reader.read (str(dst_image_1))
    result_date_2 = reader.read(str(dst_image_2))
    result_date_3 = reader.read(str(dst_image_3))
    
    # Assert
    assert isinstance(result_date_1, datetime.datetime) 
    assert isinstance(result_date_2, datetime.datetime)
    assert isinstance(result_date_3, datetime.datetime)
    assert result_date_1 != result_date_2
    assert result_date_1 == result_date_3