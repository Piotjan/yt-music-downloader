import abc
import atexit
import os
import uuid
from pathlib import Path

from src import TEMP_DIR


class _BaseFile(abc.ABC):
    def __init__(self, path: str | Path | None) -> None:
        self.path = path
        atexit.register(self._clean_up)

    @property
    def directory(self) -> Path:
        return self.path.parent

    @property
    def name(self) -> str:
        return str(self.path.name)

    @abc.abstractmethod
    def _clean_up(self) -> None: ...


class TempFile(_BaseFile):
    def __init__(self) -> None:
        super().__init__(TEMP_DIR.joinpath(str(uuid.uuid4())))
        if not self.path.parent.is_dir():
            os.mkdir(self.path.parent)
        open(self.path, "w").close()

    def _clean_up(self) -> None:
        open(self.path, "r").close()
        os.remove(self.path)
