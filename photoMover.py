#!/usr/bin/python3

# move all files with a given extension from sourceDirectory to destination/YYYY/MM/DD/

import os
import argparse
import re
import shutil

parser = argparse.ArgumentParser(description='Move all files with a given extension from source to destination/YYYY/MM/DD/')
parser.add_argument('-e', '--ext', metavar='ext', type=str, default="jpg",
                    help='Only move files with this extension. Default = jpg')
parser.add_argument('-b', '--base', metavar='base', type=str, default="IMG_",
                    help='base of the filename, everything before YYYY. default = "IMG_"')
parser.add_argument('source', metavar='source', type=str, help="Source directory. Default is " + os.getcwd(), nargs='?', default=os.getcwd())
parser.add_argument('dest', metavar="destination", type=str, help="Destination directory. Default is " + os.path.expanduser('~/Pictures'), nargs='?', default=os.path.expanduser('~/Pictures'))


args = parser.parse_args()

photos = os.listdir(args.source)

for file in photos[:]:
    if not file.endswith(args.ext):
        photos.remove(file)

year = re.compile('(?<=' + args.base + ')(\d{4})')
month = re.compile ('(?<=' + args.base + '\d{4})(\d{2})')
day = re.compile ('(?<=' + args.base + '\d{6})(\d{2})')

for file in photos[:]:
    YYYY = year.search(file)
    MM = month.search(file)
    DD = day.search(file)
    if YYYY and MM and DD:
        dest = os.path.join(args.dest, YYYY.group(), MM.group(), DD.group())
        os.makedirs(dest + '/', exist_ok=True)
        shutil.move(os.path.join(args.source, file), os.path.join(dest, file))
        print(f"Moving {os.path.join(args.source, file)} to {os.path.join(dest, file)}")
    else:
        print(f"Couldn't find the year, month, and day in {file}.")