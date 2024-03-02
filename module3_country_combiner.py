import sys


for line in sys.stdin:
    line = line.strip()
    edit_line = line[:-4]  # Removing the '.txt' extension
    print(edit_line)