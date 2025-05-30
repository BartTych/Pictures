import os

class file_hash_generator:
    """Class to apply the correct extraction method based on file extension."""
    
    def __init__(self,generators):
        self.generators = generators

    def apply(self, file):

        extention = os.path.splitext(file)[1].lower()

        if extention in self.generators:
            generator = self.generators[extention]
            return generator.generate(file)
        else:
            return None