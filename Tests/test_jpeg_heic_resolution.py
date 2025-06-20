import pathlib
import shutil
from Resolution_reader.jpeg_heic_resolution import Read_jpeg_heic_resolution

def test_read_resolution_on_copied_files(tmp_path):

    test_data_dir = pathlib.Path(__file__).parent / "resources"
    src_image_1 = test_data_dir / "DSC_0007.JPG"  # or .heic if supported!
    src_image_2 = test_data_dir / "DSC_0021.JPG"  # or .heic if supported!
    src_image_3 = test_data_dir / "IMG_20190817_111750.jpg"  # or .heic if supported!
    
    src_image_4 = test_data_dir / "1.heic"  # or .heic if supported!
    src_image_5 = test_data_dir / "3.heic"

    dst_image_1 = tmp_path / "DSC_0007.JPG.jpg"
    dst_image_2 = tmp_path / "DSC_0008.JPG.jpg"
    dst_image_3 = tmp_path / "DSC_0007_copy.JPG"
    
    dst_image_4 = tmp_path / "1.heic"  # or .heic if supported!
    dst_image_5 = tmp_path / "3.heic"


    shutil.copy(src_image_1, dst_image_1)
    shutil.copy(src_image_2, dst_image_2)
    shutil.copy(src_image_3, dst_image_3)
    shutil.copy(src_image_4, dst_image_4)
    shutil.copy(src_image_5, dst_image_5)


    reader = Read_jpeg_heic_resolution()

    resolution_1 = reader.read_resolution(dst_image_1)
    resolution_2 = reader.read_resolution(dst_image_2)
    resolution_3 = reader.read_resolution(dst_image_3)
    resolution_4 = reader.read_resolution(dst_image_4)
    resolution_5 = reader.read_resolution(dst_image_5)

    assert resolution_1 == (5984, 3366)
    assert resolution_2 == (3366, 5984)
    assert resolution_3 == (4632, 2608)
    assert resolution_4 == (3024, 4032)
    assert resolution_5 == (4032, 3024)