
from abc import ABC, abstractmethod


class Read_meta(ABC):
    """
    Abstract base class for reading data from a file.
    Contrete classes intended to implement the read method for specific file formats.
    """
    @abstractmethod
    def read(self, path: str) -> dict:
        """
        Read data from a file.

        Args:
            path (str): Path to the file.

        Returns:
            dict: Data read from the file.
        """
        pass
   