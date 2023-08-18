import os
import time
import hashlib

def get_mtime(file_path):
    """
    Get the last modified time of a file.
    """
    file_stat = os.stat(file_path)
    return time.ctime(file_stat.st_mtime)

def obscure(data):
    """
    Return a SHA256 hash of the data.
    """
    return hashlib.sha256(data.encode()).hexdigest()

def generate_commit_history(directory):
    """
    Generate a mock git commit history based on file mtime.
    """
    history = []
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(foldername, filename)
            obscured_path = obscure(full_path)
            mtime = get_mtime(full_path)
            history.append(f"commit {hash(full_path)}\nDate:   {mtime}\n\n    Modified: {obscured_path}\n\n")
    return "\n".join(history)

def save_to_file(data, output_file):
    """
    Save data to a file.
    """
    with open(output_file, 'w') as f:
        f.write(data)

if __name__ == "__main__":
    dir_path = input("Enter the path of the directory: ")
    output_dir = "git_history_output"
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    output_file_path = os.path.join(output_dir, "commit_history.txt")
    
    commit_history = generate_commit_history(dir_path)
    save_to_file(commit_history, output_file_path)

    print(f"Commit history saved to: {output_file_path}")
