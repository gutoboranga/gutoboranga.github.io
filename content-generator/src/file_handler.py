# -*- coding: utf-8 -*-

import os
import json

def read(filename):
    with open(filename) as file:
        return file.read()

def read_json(filename):
    string = read(filename)
    return json.loads(string)
    
def write(filename, content):
    with open(filename, 'w+') as file:
        return file.write(content.encode('utf8'))