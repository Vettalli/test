import os

def get_file_size(file_path):
    return os.path.getsize(file_path)


def get_latest_file(folder):
    files = [os.path.join(folder, f) for f in os.listdir(folder)]
    return max(files, key=os.path.getctime)