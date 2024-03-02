import os
import sys

filename = sys.argv[1]
path = './Stats/' + filename

try:
    fp = open(path, 'r')
except:
    print(f"The file '{path}' does not exist.")
    sys.exit(1)


for line in fp:
    date, stats = line.strip().split('\t')
    date = date.strip()
    stats = stats.strip()

    print(date + '|' + stats)



