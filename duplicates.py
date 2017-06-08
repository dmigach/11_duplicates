import argparse
import hashlib
import os
import sys


def calculate_file_hash(file_path):
    """
    :param file_path:
    :return: string with md5 hash
    """
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file_handler:
        hasher.update(file_handler.read())
        return hasher.hexdigest()


def find_duplicates(folder_path):
    """
    Recursively walks through subfolders and files and gathers duplicate info
    to dictionary
    :param folder_path:
    :return: dictionary, where file hash is key and paths to duplicate files
    separated by \n for printing is value
    """
    hashes_dict = {}
    duplicates_dict = {}
    for directory, subdirectories, file_list in os.walk(folder_path):
        for file_name in file_list:
            full_file_path = os.path.join(directory, file_name)
            file_hash = calculate_file_hash(full_file_path)
            if file_hash in hashes_dict:
                # Complex expression below is 'Check if there is record about
                # duplicates already in dictionary, if yes - append one more
                # file path to it, if no - create new record with two duplicate
                # file paths'
                duplicates_dict[file_hash] =\
                    duplicates_dict[file_hash] + '\n{}'.format(full_file_path)\
                    if file_hash in duplicates_dict else\
                    '{}\n{}'.format(full_file_path, hashes_dict[file_hash])
            else:
                hashes_dict[file_hash] = full_file_path
    return duplicates_dict


def parse_arguments():
    """
    :return: string with path to directory
    """
    parser = argparse.ArgumentParser(description='Find duplicates')
    parser.add_argument('path', nargs='?',
                        type=str, help='directory path')
    arguments = parser.parse_args()
    return arguments.path


if __name__ == '__main__':
    path = parse_arguments()
    if not path:
        sys.exit('You should specify path to directory: '
                 '"python duplicates.py dir_path"')
    elif not os.path.exists(path):
        print('Wrong directory path')
    print('---Scan started...This may take awhile...', end='\n\n')
    duplicates = find_duplicates(path)
    for _, value in duplicates.items():
        print('Group of duplicates:', end='\n\n')
        print(value)
        print('_________________________')
        print('')
