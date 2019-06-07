#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise

"""


# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir, show=False):
    """
     returns a list of the absolute paths of the special files in the given directory
    :param dir: given directory
    :return: a list of the absolute paths of the special files
    """

    abspath_dir = os.path.abspath(dir)
    files = os.listdir(abspath_dir)
    special_files = []
    for f in files:
        f = os.path.join(abspath_dir, f)
        if os.path.isfile(f):
            if re.search('__\w+__', f):
                if show:
                    print(f)
                special_files.append(f)

    return special_files


def copy_to(paths, dir):
    """
     given a list of paths, copies those files into the given directory
    :param paths:
    :param dir:
    :return:
    """

    if not os.path.exists(dir):
        os.mkdir(dir, os.O_RDWR)
    for abs_filename in paths:
        shutil.copyfile(abs_filename, os.path.abspath(dir) + '\\' + abs_filename.split('\\')[-1])
    return


def zip_to(paths, zippath):
    """
     given a list of paths, zip those files up into the given zipfile
    :param paths:
    :param zippath:
    :return:
    """

    src = os.path.commonprefix(paths)[len(os.path.abspath('.'))+1:]
    shutil.make_archive(zippath.split('.')[0], 'zip', '.', src)
    print(os.path.getsize(zippath))

    return


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        fromdir = args[2]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        fromdir = args[2]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

        # +++your code here+++
        # Call your functions
    if todir:
        copy_to(get_special_paths(fromdir), todir)
    elif tozip:
        zip_to(get_special_paths(fromdir, show=True), tozip)
    else:
        get_special_paths(args[0])


if __name__ == "__main__":
    main()
