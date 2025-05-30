import os

class flie_hash_generator:
    """Class to apply the correct extraction method based on file extension."""
    
    def __init__(self,generators):
        self.generators = generators

    def apply(self, file):

        extention = os.path.splitext(file)[1].lower()

        if extention in self.generators:
            generator = self.generator[extention]
            return generator.generate_hash(file)
        else:
            return None