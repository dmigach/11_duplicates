import argparse
import hashlib
import os


def calculate_file_hash(file_path):
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as file_handler:
            hasher.update(file_handler.read(1000000))
            return hasher.hexdigest()
    except OSError:
        pass


def find_duplicates(folder_path):
    hashes_dict = {}
    for directory, subdirectories, file_list in os.walk(folder_path):
        for file_name in file_list:
            full_file_path = os.path.join(directory, file_name)
            file_hash = calculate_file_hash(full_file_path)
            hashes_dict.setdefault(file_hash, []).append(full_file_path)
    duplicates_list = [paths for paths in hashes_dict.values()
                       if len(paths) > 1]
    return duplicates_list


def parse_arguments():
    parser = argparse.ArgumentParser(description='Find duplicates')
    parser.add_argument('path', nargs='?',
                        type=str, help='directory path')
    arguments = parser.parse_args()
    return arguments.path


def print_duplicates(duplicates_list):
    for file_paths in duplicates_list:
        print('Group of duplicates:', end='\n\n')
        print('\n'.join(file_paths))
        print('_________________________', end='\n\n')

if __name__ == '__main__':
    path = parse_arguments()
    if not path:
        exit('You should specify path to directory: '
             '"python duplicates.py dir_path"')
    elif not os.path.exists(path):
        exit('Wrong directory path')
    print('---Scan started...This may take awhile...', end='\n\n')
    duplicates = find_duplicates(path)
    print_duplicates(duplicates)
