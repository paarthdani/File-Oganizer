# Created By Parth Dani
# Date : 15/04/2020

import os
import shutil
from pathlib import Path

DESKTOP_PATH = "/Users/Parth/Desktop/"
DOWNLOADS_PATH = "/Users/Parth/Downloads/"

DIRECTORIES = {
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"],
    "Media": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".aac",
              ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav",
              ".wma"],
    "Documents": [".oxps", ".XML", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps",
                  ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx", ".csv",
                  ".numbers", ".pdf", ".txt", ".in", ".out"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip", ".jar"]
}

FILE_FORMATS_TO_BE_IGNORED = [".dmg"]

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


def main():
    os.chdir(DOWNLOADS_PATH)
    organize_files_in_downloads()
    os.chdir(DESKTOP_PATH)
    organize_files_in_desktop()


def organize_files_in_downloads():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        # Ignore the file format you want to skip
        if file_format in FILE_FORMATS_TO_BE_IGNORED:
            continue
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
        else:
            directory_path = Path("Other")
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))


def organize_files_in_desktop():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS_TO_BE_IGNORED:
            continue
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            shutil.copy(file_path, DOWNLOADS_PATH + str(directory_path.joinpath(file_path)))
        else:
            directory_path = Path("Other")
            shutil.copy(file_path, DOWNLOADS_PATH + str(directory_path.joinpath(file_path)))
        os.remove(entry)


if __name__ == "__main__":
    main()
