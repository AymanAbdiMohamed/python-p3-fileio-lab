# lib/file_io.py
from pathlib import Path

def write_file(file_name, file_content):
    """
    Writes content to a file. Overwrites if the file already exists.
    file_name can be a Path object or a string.
    """
    file_path = Path(file_name).with_suffix(".txt")
    file_path.write_text(file_content)


def append_file(file_name, append_content):
    """
    Appends content to an existing file. Creates the file if it doesn't exist.
    """
    file_path = Path(file_name).with_suffix(".txt")
    with file_path.open("a") as f:
        f.write(append_content)


def read_file(file_name):
    """
    Reads the content of a file and returns it.
    """
    file_path = Path(file_name).with_suffix(".txt")
    return file_path.read_text()
