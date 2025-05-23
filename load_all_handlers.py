

import Processors.Read_avi as Read_avi
import Processors.Read_jpeg as Read_jpeg
import Processors.Read_heic as Read_heic
import Processors.Read_mov_mp4 as Read_mov_mp4

#mysle ze ta nazwa jest mylaca Rada_meto, powinienem bardziej nazwac to 
def load_all_handlers() -> dict:
    """
    Load handlers here from the directory
    will be improved to load all handlers from a directory if number of handlers will grow
    now it is still manageable. use lower case for extensions only. 

    """
    handlers = {
        ".avi": Read_avi.Read_avi(),
        ".jpeg": Read_jpeg.Read_jpeg(),
        ".jpg": Read_jpeg.Read_jpeg(),
        ".heic": Read_heic.Read_heic(),
        ".mov": Read_mov_mp4.Read_mov(),
        ".mp4": Read_mov_mp4.Read_mov(),
        # Add more handlers as needed
    }
    

    return handlers