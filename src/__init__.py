from pathlib import Path

_FILE_DIR = Path(__file__).parent
PROJECT_DIR = _FILE_DIR.parent
TEMP_DIR = PROJECT_DIR.joinpath("temp")
