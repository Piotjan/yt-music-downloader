from pathlib import Path

from pytubefix import YouTube


class YTDownloader:
    @classmethod
    def download(cls, url: str, save_file_path: Path) -> None:
        YouTube(url).streams.first().download()
