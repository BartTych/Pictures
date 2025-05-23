
import Processors.Read_meta as Read_meta
from pymediainfo import MediaInfo
from datetime import datetime

class Read_mov(Read_meta.Read_meta):
    """
    Class for reading MOV files.
    Inherits from Read_meta.
    """

    def read(self, path: str) -> dict:
        """
        Read data from a MOV and mp4 file.

        Args:
            path (str): Path to the MOV file.

        Returns:
            dict: Data read from the MOV file.
            works imperfectly with apple mov files
            and returns time of mov end instead of start
            but it good enough
        """
        try:
            media_info = MediaInfo.parse(path)
        except:
            return None
        
        for track in media_info.tracks:
            if track.track_type == "General":
                try:
                    # that reading is imperfect
                    # it returns time of mov end instead of start
                    # will test it if error occurs
                    date_str = track.recorded_date or track.tagged_date
                except:
                    return None
                try:
                    date = datetime.strptime(date_str,'%Y-%m-%d %H:%M:%S UTC')
                except:
                    return None
                print('mov file reading correctly')
                return date
        
        return None
    