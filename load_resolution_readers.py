
import Resolution_reader.jpeg_heic_resolution as jpeg_heic_resolution
import Resolution_reader.mov_avi_mp4_resolution as mov_avi_mp4_resolution

def load_all_readers() -> dict:
    """
    Load resolution readers here from the directory.
    Will be improved to load all readers from a directory if the number of readers grows.
    Now it is still manageable. Use lower case for extensions only.
    """
    readers = {
        ".avi": mov_avi_mp4_resolution.Read_mov_avi_mp4_resolution(),
        ".jpeg": jpeg_heic_resolution.Read_jpeg_heic_resolution(),
        ".jpg": jpeg_heic_resolution.Read_jpeg_heic_resolution(),
        ".heic": jpeg_heic_resolution.Read_jpeg_heic_resolution(),
        ".mov": mov_avi_mp4_resolution.Read_mov_avi_mp4_resolution(),
        ".mp4": mov_avi_mp4_resolution.Read_mov_avi_mp4_resolution(),
        # Add more readers as needed
    }
    
    return readers