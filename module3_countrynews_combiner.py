import os
import sys


curr_dir = os.getcwd()
target_dir = os.path.join(curr_dir,'worldwide_country')
for line in sys.stdin:
    line = line.strip()
    print(line)
    