import os

def read_all_files_in_directory(directory_path):
    """
    Return a list contains all files in the directory.
    """
    files =  []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            files.append(file_name)
    return files
