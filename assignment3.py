#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""IS211 Assignment 3"""


import csv
import urllib2
import re
import argparse


def downloadData(url):
    """Downloads csv file from url location."""

    response = urllib2.urlopen(url)
    html = csv.reader(response)
    return html


def images(num):
    """Looks for images in file."""

    test = []
    results = 0
    for row in downloadData(num):
        if re.search('jpg|gif|png|jpeg', row[0], re.IGNORECASE):
            test.append(row[0])
            results += 1
    return len(test)


def browser(hits):
    """Calculates the most browser used."""

    counter = 0
    c_list = []
    s_list = []
    f_list = []
    i_list = []
    browser_dict = {}
    for row in downloadData(hits):
        if re.search('Chrome', row[2]):
            c_list.append(row[2])
        elif re.search('Safari', row[2]):
            s_list.append(row[2])
        elif re.search('Firefox', row[2]):
            f_list.append(row[2])
        elif re.search('MSIE', row[2]):
            i_list.append(row[2])
            counter += 1
    browser_dict = {'Chrome': len(c_list), 'Safari': len(s_list), 'Firefox': len(f_list), 'MSIE': len(i_list)}
    return max(browser_dict)


def computation(total):
    """Function that shows the results."""
    row_count = len(list(downloadData(total)))
    image_percentage = images(total) * 100 / row_count
    print "Image requests account for %s percent of all requests." % image_percentage
    print browser(total), "is the most popular browser."



def main():

    if __name__ == "__main__":
        main()

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='Input url', required=True)
args = parser.parse_args()
url = args.url
computation(url)