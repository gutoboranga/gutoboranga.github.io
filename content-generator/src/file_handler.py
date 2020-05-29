# -*- coding: utf-8 -*-

import os
import json
import collections

def read(filename):
    with open(filename) as file:
        return file.read()

def read_json(filename):
    string = read(filename)
    return json.loads(string, object_pairs_hook=collections.OrderedDict)
    
def write(filename, content):
    with open(filename, 'w+') as file:
        return file.write(content.encode('utf8'))