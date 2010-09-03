#!/usr/bin/python
# -----------------------------------------------------------------------------
# File:   unclutter.py
# Author: Taurus Olson
# Description: "Everything in ist right place..."
#               Move the files to a directory 'file_ext' depending on their
#               extensions.
#               This script is inspired from:
#               Python File and Directory Manipulator 1.0 by Douglas Palovick
#
# Version: 0.2
# -----------------------------------------------------------------------------

import os, glob, shutil, sys

if len(sys.argv) < 2:
    print "Usage:\n%s [DIR]" % sys.argv[0]
    sys.exit(0)

def get_extensions(dir):
    """docstring for get_extensions"""

    if len(sys.argv) < 2:
        print "Usage:\n%s [DIR]" % sys.argv[0]
        sys.exit(0)

    dir = sys.argv[1]

    files = os.listdir(dir)
    extensions = []
    for file in files:
        if os.path.isfile(file):
            base, ext = os.path.splitext(file)
            if ext != "":
                extensions.append(ext)

    set_extensions = []
    for ext in set(extensions):
        set_extensions.append(ext)

    return set_extensions


class Directory(object):
    """docstring for Directory"""
    
    def __init__(self):
        pass

    def unclutter(self, path):
        """Unclutter the dir"""

        self.path = path
        this_file = "file_manip.py"
        file_ext = get_extensions(self.path)

        for file in file_ext:
            dir_base_name = "file_" + file.strip('.')
            filenames = glob.glob(( '*' + file))

            while filenames:
                new_dir = dir_base_name
                if not os.path.exists(new_dir):
                    print "-------%s files-------" % file
                    os.mkdir(new_dir)

                for n in range(len(filenames)):
                    src_file = filenames.pop(0)
                    if src_file != this_file:
                        shutil.copy(src_file, new_dir)
                        os.unlink(src_file)
                        self.display(src_file, new_dir)

    def display(self, source_file, new_directory):
        """docstring for display"""
        self.source_file = source_file
        self.new_directory = new_directory
        print "%s  was moved to %s" %(self.source_file, self.new_directory)
        
directory = Directory()
for dir in os.listdir(sys.argv[1]):
    try:
        directory.unclutter(dir)
    except OSError:
        pass

