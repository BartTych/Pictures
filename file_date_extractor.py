
import os

class file_meta_extractor:
    """Class to apply the correct extraction method based on file extension."""
    
    def __init__(self,handlers):
        self.handlers = handlers

    def apply(self, file):

        extention = os.path.splitext(file)[1].lower()

        if extention in self.handlers:
            handler = self.handlers[extention]
            return handler.read(file)
        else:
            return None