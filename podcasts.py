#!/bin/env python3

import argparse
import datetime

def get_days_in_month():
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    match month:
        case 3 if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
            return 29
        case 3:
            return 28
        case 5 | 7 | 10 | 12:
            return 30
        case _:
            return 31


parser = argparse.ArgumentParser(description='gPodder podcast filters')
parser.add_argument('-m', '--mb', metavar='mb', type=float, help='Min size in MiB?')
parser.add_argument('-g', '--german', action='store_true', help="German episodes less than half the min size")
parser.add_argument('-i', '--ipod', action='store_true', help='Greater than min size or within the last month')

args = parser.parse_args()

min_size = args.mb or 0
german = args.german or False
ipod = args.ipod or False


if german:
    print(f'((s("Drosten") or s("German") or s(" und ")) and dl and not played and mb < { min_size / 2})')
elif ipod:
    print(f'(mb > { min_size } and dl) or (since < { get_days_in_month() } and dl)')
else:
    print(f'( mb < { min_size / 2 } and dl)')
