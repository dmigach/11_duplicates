import argparse
import hashlib
import os


def calculate_file_hash(file_path):
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as file_handler:
            hasher.update(file_handler.read())
            return hasher.hexdigest()
    except OSError:
        pass


def find_duplicates(folder_path):
    hashes_dict = {}
    duplicates_dict = {}
    for directory, subdirectories, file_list in os.walk(folder_path):
        for file_name in file_list:
            full_file_path = os.path.join(directory, file_name)
            file_hash = calculate_file_hash(full_file_path)
            if file_hash in hashes_dict:
                if file_hash not in duplicates_dict:
                    duplicates_dict[file_hash] = [full_file_path]
                duplicates_dict[file_hash].append(full_file_path)
            else:
                hashes_dict[file_hash] = [full_file_path]
    return duplicates_dict


def parse_arguments():
    parser = argparse.ArgumentParser(description='Find duplicates')
    parser.add_argument('path', nargs='?',
                        type=str, help='directory path')
    arguments = parser.parse_args()
    return arguments.path


def print_duplicates(duplicates_dictionary):
    for _, duplicates_list in duplicates_dictionary.items():
        print('Group of duplicates:', end='\n\n')
        print('\n'.join(duplicates_list))
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
