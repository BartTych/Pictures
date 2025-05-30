from abc import ABC, abstractmethod


class Generate_hash(ABC):
    """
    Abstract base class for generating hash representing file.
    Contrete classes intended to implement generation for different extentions.
    """
    @abstractmethod
    def generate(self, path: str) -> dict:
        """
        Generate hash representing file.

        Args:
            path (str): Path to the file.

        Returns:
            dict: Hash representing file.
        """
        pass