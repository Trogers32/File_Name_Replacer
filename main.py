#!/usr/bin/env python
import os
import re


def rename_files(directory, old_pattern, new_pattern):
    for root, dirs, files in os.walk(directory):
        for f in files:
            if re.search(old_pattern, f) is not None:
                new_name = re.sub(old_pattern, new_pattern, f)
                try:
                    os.rename(os.path.join(root,f), os.path.join(root, new_name))
                except OSError:
                    print("No such file or directory!")


if __name__ == "__main__":
    directory_input = input("Enter your file directory: ")
    old_pattern_input = input("Enter the file name to replace: ")
    new_pattern_input = input("Enter the file name you want: ")

    rename_files(directory_input, old_pattern_input, new_pattern_input)
