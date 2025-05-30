import Hash_generation.hash_generation_meta as hash_gen
from PIL import Image
import pillow_heif
pillow_heif.register_heif_opener()
from imagehash import phash

class Generate_jpeg_heic_hash(hash_gen.Generate_hash):

    def generate(self, path: str) -> dict:
        try:
            with Image.open(path) as img:
                return (phash(img))
        except:
            return None


