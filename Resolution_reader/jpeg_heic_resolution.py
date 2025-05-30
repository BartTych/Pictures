
import Resolution_reader.Resolution_meta as Resolution_meta
from PIL import Image,ImageOps

class Read_jpeg_heic_resolution(Resolution_meta.Read_resolution):
    """
    Class for reading resolution from JPEG and HEIC files.
    Inherits from Resolution_meta.Read_resolution.
    """

    def read_resolution(self, path: str) -> tuple[int, int] | None:
        """
        Read resolution from a JPEG or HEIC file.

        Args:
            path (str): Path to the JPEG or HEIC file.

        Returns:
            dict: Resolution data read from the file.
            or None if the file has no resolution data available.
        """
        
        try:
            with Image.open(path) as img:
                img = ImageOps.exif_transpose(img)  # Handle EXIF orientation
                width, height = img.size
        except:
            return None
        return width, height