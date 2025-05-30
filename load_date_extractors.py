

import Meta_extraction.avi_date as avi_date
import Meta_extraction.jpeg_date as jpeg_date
import Meta_extraction.heic_date as heic_date
import Meta_extraction.mov_mp4_date as mov_mp4_date

#mysle ze ta nazwa jest mylaca Rada_meto, powinienem bardziej nazwac to 
def load_all_handlers() -> dict:
    """
    Load handlers here from the directory
    will be improved to load all handlers from a directory if number of handlers will grow
    now it is still manageable. use lower case for extensions only. 

    """
    handlers = {
        ".avi": avi_date.Read_avi(),
        ".jpeg": jpeg_date.Read_jpeg(),
        ".jpg": jpeg_date.Read_jpeg(),
        ".heic": heic_date.Read_heic(),
        ".mov": mov_mp4_date.Read_mov(),
        ".mp4": mov_mp4_date.Read_mov(),
        # Add more handlers as needed
    }
    

    return handlers