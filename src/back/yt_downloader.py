from pathlib import Path

from pytubefix import YouTube


class YTDownloader:
    @classmethod
    def download(cls, url: str, save_file_path: str) -> None:
        file_path = Path(save_file_path)
        YouTube(url).streams.first().download(
            file_path.parent.as_posix(), file_path.name
        )

    @staticmethod
    def _convert_mp4_to_mp3(mp4_file: Path, mp3_file: Path) -> None:
        pass
