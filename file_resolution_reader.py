import os

class file_resolution_reader:
    """Class to apply the correct extraction method based on file extension."""
    
    def __init__(self,readers):
        self.readers = readers

    def apply(self, file):

        extention = os.path.splitext(file)[1].lower()

        if extention in self.readers:
            reader = self.readers[extention]
            return reader.read_resolution(file)
        else:
            return None