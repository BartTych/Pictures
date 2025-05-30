import Hash_generation.jpeg_heic_hash as jpeg_heic_hash
import Hash_generation.mov_avi_mp4_hash as mov_avi_mp4_hash

#mysle ze ta nazwa jest mylaca Rada_meto, powinienem bardziej nazwac to 
def load_all_generators() -> dict:
    """
    Load handlers here from the directory
    will be improved to load all handlers from a directory if number of handlers will grow
    now it is still manageable. use lower case for extensions only. 

    """
    handlers = {
        ".avi": mov_avi_mp4_hash.Generate_mov_avi_mp4_hash(),
        ".jpeg": jpeg_heic_hash.Generate_jpeg_heic_hash(),
        ".jpg": jpeg_heic_hash.Generate_jpeg_heic_hash(),
        ".heic": jpeg_heic_hash.Generate_jpeg_heic_hash(),
        ".mov": mov_avi_mp4_hash.Generate_mov_avi_mp4_hash(),
        ".mp4": mov_avi_mp4_hash.Generate_mov_avi_mp4_hash(),
        # Add more handlers as needed
    }
    

    return handlers