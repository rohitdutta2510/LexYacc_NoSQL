import sys

curr_date = ''
curr_response = []
for line in sys.stdin:
    date,response = line.strip().split()
    print(date,response)