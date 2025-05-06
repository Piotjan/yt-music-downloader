from argparse import ArgumentParser, Namespace
from pathlib import Path

from src.back.YTDownloader import YTDownloader


def parse_args() -> Namespace:
    parser = ArgumentParser(
        prog="YT Music Downloader",
        description="Download your favourite music directly from YT to mp3 in save way.",
    )
    parser.add_argument("-u", "--url", required=True, help="URL to YouTube film.")
    parser.add_argument(
        "-o",
        "--output_file",
        required=False,
        default=Path(__file__).parent.joinpath("output_music.mp3").as_posix(),
        help="Path to downloaded file.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    YTDownloader.download(args.url, args.output_file)
