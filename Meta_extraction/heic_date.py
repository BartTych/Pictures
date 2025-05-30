import Meta_extraction.Read_meta as Read_meta
from datetime import datetime

# HEIC
from PIL import Image
import pillow_heif
pillow_heif.register_heif_opener()
import piexif

class Read_heic(Read_meta.Read_meta):
    """
    Class for reading HEIC files.
    Inherits from Read_meta.
    """

    def read(self, path: str) -> dict:
        """
        Read data from a HEIC file.

        Args:
            path (str): Path to the HEIC file.

        Returns:
            dict: Data read from the HEIC file.
        """
        #heic-pillow                       
        try:
            image = Image.open(path)
        except:
            # Handle the case where the file is not a valid HEIC file
            print(f"Error opening HEIC file: {path}")
            return None
        
        try:
            exif_data = image.info.get("exif")
        except:
            # Handle the case where 'exif' is not in image.info
            print("No EXIF data found in HEIC file.")
            return None

        if exif_data:
            exif_dict = piexif.load(exif_data)

            # why decoding is needed
            # because exif_dict["Exif"] is a dictionary with bytes keys
            # and values, and we need to decode the keys and values to strings
            # to get the datetime string
            def safe_decode(value):
                return value.decode() if isinstance(value, bytes) else value
            try:
                str_ = safe_decode(exif_dict["Exif"].get(piexif.ExifIFD.DateTimeOriginal))
                
                try:
                    date = datetime.strptime(safe_decode(str_), '%Y:%m:%d %H:%M:%S')
                    print('heic file reading correctly')
                    return date
                except:
                    # Handle the case where the date format is incorrect
                    print(f"Invalid date format: {str_}")
                    return None
            except:
                # Handle the case where the date format is incorrect or not found
                # or conversion error 
                print("No usable datetime found in EXIF.")
                return None
        else:
            print("No EXIF data found.")
            return None