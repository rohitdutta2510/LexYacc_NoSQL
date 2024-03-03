import sys

countries = ['Australia','India','England','Malaysia','Singapore']

for line in sys.stdin:
    filepath = line.strip()
    fp = open(filepath,'r')
    data = fp.read()
    print(data)
