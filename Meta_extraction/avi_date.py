
import Meta_extraction.Read_meta as Read_meta
import subprocess
import json
from pathlib import Path

from datetime import datetime

class Read_avi(Read_meta.Read_meta):
    """
    Class for reading AVI files.
    Inherits from Read_meta.
    """

    def read(self, path: str) -> dict:
        """
        Read data from an AVI file.

        Args:
            path (str): Path to the AVI file.

        Returns:
            dict: Data read from the AVI file.
        """
        
        try:
            result = subprocess.run(
            ["exiftool", "-j", "-G", "-time:all", "-a", "-u", path],
            capture_output=True,
            text=True
            )
        except:
            return None

        if result.returncode != 0:
        #raise RuntimeError(f"ExifTool error: {result.stderr}")
            return None
        data = json.loads(result.stdout)
        if not isinstance(data, list) or not data:
        #raise ValueError("Unexpected JSON format: not a list or empty.")
            return None
        metadata = data[0]  # first file's metadata
        dt = metadata.get("EXIF:DateTimeOriginal", None)

        if dt:
            #print("EXIF:DateTimeOriginal:", dt)
            print("avi file reading correctly")
            
            try:
                date = datetime.strptime(dt,'%Y:%m:%d %H:%M:%S')
                return date
            except:
                return None
        else:
            #print("No EXIF:DateTimeOriginal found.")
            return None
        


    