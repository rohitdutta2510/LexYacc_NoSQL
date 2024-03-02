import sys

for line in sys.stdin:
    key, value = line.strip().split('@')
    details = value.strip().split('|')
    print(key + '@' + '|'.join(details))