import os
import time

def get_mtime(file_path):
    """
    Get the last modified time of a file.
    """
    file_stat = os.stat(file_path)
    return time.ctime(file_stat.st_mtime)


def list_files_with_mtime(directory):
    """
    List all files in a directory with their last modified time.
    """
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            list_files_with_mtime(full_path)
        else:
            print(f"{full_path}: Last modified on {get_mtime(full_path)}")
