#!/usr/bin/python

# -----------------------------------------------------------------------------
# File:   unclutter.py
# Author: Taurus Olson
# Description: "Everything in its right place..."
#               Move the files to a directory 'file_ext' depending on their
#               extensions.
#               This script is inspired from:
#               Python File and Directory Manipulator 1.0 by Douglas Palovick
#
# Version: 0.2
# -----------------------------------------------------------------------------

import os, glob, shutil, sys

if len(sys.argv) < 2:
    print "Usage:\n%s SRC_DIR [DEST_DIR]" % sys.argv[0]
    sys.exit(0)

def get_extensions(dir):
    """docstring for get_extensions"""

    # if len(sys.argv) < 2:
    #     print "Usage:\n%s SRC_DIR [DEST_DIR]" % sys.argv[0]
    #     sys.exit(0)

    # dir = sys.argv[1]

    files = os.listdir(dir)
    extensions = []
    for f in files:
        if os.path.isfile(f):
            base, ext = os.path.splitext(f)
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
        this_file = __file__
        extensions = get_extensions(self.path)

        for extension in extensions:
            ext_dir = "file_" + extension.strip('.')
            filenames     = glob.glob(( '*' + extension))

            while filenames:
                new_dir = ext_dir
                if not os.path.exists(new_dir):
                    print "-------%s files-------" % extension
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

