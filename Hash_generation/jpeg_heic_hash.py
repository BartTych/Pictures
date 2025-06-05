import Hash_generation.hash_generation_meta as hash_gen
from PIL import Image
import pillow_heif
pillow_heif.register_heif_opener()
from imagehash import phash


class Generate_jpeg_heic_hash(hash_gen.Generate_hash):

    
    def generate(self, path: str) -> int:
        try:
            with Image.open(path) as img:
                img = img.convert('RGB')  # Normalize to prevent mode-related issues
                hash_str = str(phash(img))  # e.g., 'ff00aa11...'
                return int(hash_str, 16)    # Cast hex string to int
                #return phash(img)    # Cast hex string to int
                    
        except Exception as e:
            print(f"Error generating hash for {path}: {e}")
            return None
    
