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
    List all files in a directory with their last modified time. **Quick and Dirty!** Will resolve nested forloops later.
    """
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(foldername, filename)
            print(f"{full_path}: Last modified on {get_mtime(full_path)}")

if __name__ == "__main__":
    dir_path = input("Enter the path of the directory: ")
    list_files_with_mtime(dir_path)
