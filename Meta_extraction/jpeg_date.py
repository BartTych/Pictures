
import Meta_extraction.Read_meta as Read_meta
import os
from datetime import datetime
from exif import Image as Image_exif

class Read_jpeg(Read_meta.Read_meta):

    """
    Class for reading JPEG files.
    Inherits from Read_meta.
    """

    def read(self, path: str) -> dict:
        """
        Read date  from a JPEG meta file.

        Args:
            path (str): Path to the JPEG file.

        Returns:
            dict: Date read from the JPEG meta file.
            or None if the file no date is available.
        """
        #exif

        with open(path, "rb") as img_file:
            try:
                img = Image_exif(img_file)
            except:
                return None
            
            if img.has_exif:
                # that should be protected by try except
                try:
                    dt_str = getattr(img, "datetime_original", None) or getattr(img, "datetime", None)
                except:
                    # getattr can raise ValueError if the attribute is not found ?? 
                    # return in no date mode
                    print("No usable datetime found in EXIF.")
                    return None

                if dt_str:
                    try:
                        date = datetime.strptime(dt_str, "%Y:%m:%d %H:%M:%S")
                        print('jpeg file reading correctly')
                        return date
                    except:
                        
                        print(f"Invalid date format: {dt_str}")
                        # return in no date mode
                        # log the error
                        return None
                else:
                    print(path)
                    print("No usable datetime found in EXIF.")
                    return None
            else:
                # No EXIF data found
                # return in no date mode
                print("No EXIF data found.")
                return None
        

