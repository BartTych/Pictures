
import Resolution_reader.Resolution_meta as Resolution_meta


class Read_mov_avi_mp4_resolution(Resolution_meta.Read_resolution):
    
    def read_resolution(self, path: str) -> dict:
        """
        Read resolution from a MOV, AVI, or MP4 file.

        Args:
            path (str): Path to the MOV, AVI, or MP4 file.

        Returns:
            dict: Resolution data read from the file.
            or None if the file has no resolution data available.
        """
        try:
            import cv2
            video = cv2.VideoCapture(path)
            if not video.isOpened():
                return None
            
            width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
            video.release()
            
            return {'width': width, 'height': height}
        except Exception as e:
            print(f"Error reading resolution: {e}")
            return None