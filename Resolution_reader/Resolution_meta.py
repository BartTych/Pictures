
from abc import ABC, abstractmethod


class Read_resolution(ABC):
    """
    Abstract base class for reading data from a file.
    Contrete classes intended to implement the read method for specific file formats.
    """
    @abstractmethod
    def read_resolution(self, path: str) -> dict:
        """
        Read resolution from a file.

        Args:
            path (str): Path to the file.

        Returns:
            dict: Resolution data read from the file.
        """
        pass
   