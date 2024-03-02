import os
import sys

filename = sys.argv[1]
path = './Stats/' + filename

try:
    fp = open(path, 'r')
except:
    print(f'file {filename} does not exist !!')