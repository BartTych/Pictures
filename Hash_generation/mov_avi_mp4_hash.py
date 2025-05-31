
import Hash_generation.hash_generation_meta as hash_gen
import cv2
import imagehash
from PIL import Image
import hashlib
import os
import numpy as np

class Generate_mov_avi_mp4_hash(hash_gen.Generate_hash):
    
    
    def generate(self,path, num_frames=10):
        cap = cv2.VideoCapture(path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_hashes = []
        
        for i in range(num_frames):
            frame_idx = int(i * total_frames / num_frames)
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
            ret, frame = cap.read()
            if not ret:
                continue
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(frame)
            h = imagehash.phash(pil_img)
            frame_hashes.append(str(h))
        
        cap.release()
        return hash(''.join(frame_hashes))
    

    '''
    def generate(self,path):
        # Ensure path is a proper string
        if not isinstance(path, str):
            raise ValueError("Expected string path to video file.")
        
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            raise IOError(f"Failed to open video file: {path}")
        
        # Example: read one frame
        ret, frame = cap.read()
        print("Frame read:", ret)
        cap.release()
    '''
