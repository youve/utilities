#!/usr/bin/env python3
''' Since upgrade to qt6, when qutebrowser crashes a page that has previously crashed, the
Try again no longer works because "Not allowed to navigate top frame to data URL", and
we're left with multiple rounds of base64 encoded garbage but the original url is still
visible in urlencoded form. This program extracts the url
'''

import argparse
import os

from urllib.parse import unquote

def get_start_str(data):
    '''
    Assumes the url either starts with http:// or https://
    '''
    assert "http" in data
    http ="http%3A%2F%2F"
    https = "https%3A%2F%2F"
    if http in data:
        return http
    else:
        return https

def get_end_str(data):
    '''
    The first occurrence of the url is followed by a </title> tag, but this requires
    pasting a ton of garbage  into the terminal. It is enough to paste only the last
    line of the garbage, in which case a <br> is looked for.
    '''
    title_tag = "%3C%2Ftitle%3E"
    br_tag = "%3Cbr%3E"
    assert "2Ftitle" in data or "3Cbr" in data
    if title_tag in data:
        return title_tag
    else:
        return br_tag

def trim(data):
    '''Return the piece of data that starts with http(s):// and ends with either
    </title> or <br>, still in urlencoded form
    '''
    start = data.index(get_start_str(data))
    end = data.index(get_end_str(data))
    return data[start:end]

def decode_enough_times(data):
    '''
    If the data has been through multiple URL encodings and only the last line of garbage
    is pasted into the terminal, then instead of %3A for a colon we might have %253A or
    %25253A or possibly any number of times. We will decode this just enough times to be
    able to process it elsewhere.
    '''
    start = get_start_str(data)
    end = get_end_str(data)
    looped = 0
    while start not in data or end not in data:
        # the asserts in get_start_str and get_end_str ensure this will halt eventually
        data = unquote(data)
        start = get_start_str(data)
        end = get_end_str(data)
        looped += 1
        if os.getenv("DEBUG"):
            print(f"decode_enough_times looped {looped}")
    return data

def de_amp(data):
    looped = 0
    while "&amp" in data:
        data = data.replace("&amp;", "&")
        looped += 1
        if os.getenv("DEBUG"):
            print(f"de_amp looped {looped}")
    return data

parser = argparse.ArgumentParser(description='Translate qutebrowser garbage back into a url')
parser.add_argument('data', type=str, help='Garbage from qutebrowser')

args = parser.parse_args()

print(de_amp(unquote(unquote(trim(decode_enough_times(args.data))))))
