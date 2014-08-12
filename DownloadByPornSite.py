# -*- coding: utf8 -*-

__author__ = 'ipetrash'

import urllib.request
import re
import os
import sys
import argparse

# Code from: http://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
def sizeof_fmt(num):
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')


def progress(count, block_size, total_size):
    percent = count * block_size * 100.0 / total_size
    print("Download: %s/%s(%3.1f%%)" % (sizeof_fmt(count * block_size), sizeof_fmt(total_size), percent) + ' ' * 20, end='\r')


def create_parser():
    parser = argparse.ArgumentParser(description="Download porn videos by site www.trahun.tv. Serious! lol.")
    parser.add_argument("url", help="Url video.")
    parser.add_argument("dir", help="The folder in which the downloaded video.")
    return parser


def main(args):
    url = args.url
    dir = args.dir
    with urllib.request.urlopen(url) as f:  # Open url
        data = f.read()  # Download context url
        data = data.decode("utf-8")  # Bytes to str
        pattern = r"video_url=(.*?\.flv)"  # Pattern url video
        result = re.search(pattern, data)  # Search link to video :)
        url_video = result.group(1)  # Get one group -- url video
        base_name = os.path.basename(url_video)  # base name file video
        if not os.path.exists(dir):  # If dir not exist, then make
            os.makedirs(dir)
        file_name = os.path.join(dir, base_name)

        print("URL: %s" % url_video)
        print("Dir: %s" % dir)
        print("File: %s" % file_name)
        urllib.request.urlretrieve(url_video, file_name, reporthook=progress)

    return 0


if __name__ == '__main__':
    parser = create_parser()

    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        code = main(args)
        sys.exit(code)

    sys.exit(0)