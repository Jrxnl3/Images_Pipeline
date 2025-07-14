from abc import ABC, abstractmethod
from pathlib import Path


class Processing_Strategy(ABC):

    @abstractmethod
    def process(self, file_path: Path, output_path: Path):
        pass
