# Duplicates finder

This script allows you to find duplicating files in your filesystem. It uses
md5 hash to find identical files.

## Prerequisites

The script is written in `Python 3`, so you'll need it's interpretator to run it.


## Usage

To run the script you should specify which folder script will analyze with
 relative path:
    
    python duplicates.py directory
    
or absolute path:
    
    python duplicates.py /Users/user/aa/Downloads/
    
After running the script you will get groups of duplicating files separated by
empty lines.

## Warning

Script may skip files which otherwise generate OS error, for example files
 with too long file path.

## Support

In case of any difficulties or questions please contact <dmitrygach@gmail.com>.