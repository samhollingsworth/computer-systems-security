# !/usr/bin/env python
#
#   COMP 116
#   LAB 9: Fuzzer
#   BY: Samuel Hollingsworth
#

#import requests
import os
import re

site = input("Site Address: ")
result = requests.get(site)

## Check for XSS Vulnerabilities
if result.text.find('<input ') != -1:
    print('Possible XSS Vulnerability Found at %s' % site)

else:
    exit()

## Find all possible inputs on site
inputs = re.findall('<input type=.* name="(.*)" [a-z]', result.text)

path = input('What is the path of the SecLists file? ')

for filename in os.listdir(path):
    filename = path + '/' + filename
    file = open(filename, "r")

    for line in file:

        for inputname in inputs:
            payload = {}
            payload[inputname] = line

        r = requests.post(site, data = payload)

file.close()
