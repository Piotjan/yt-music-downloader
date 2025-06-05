from pathlib import Path

from pytubefix import YouTube


class YTDownloader:
    @classmethod
    def download(cls, url: str, save_file_path: str) -> None:
        output_file = Path(save_file_path)
        YouTube(url).streams.filter(type="audio").first().download(
            output_file.parent.as_posix(), output_file.name
        )
