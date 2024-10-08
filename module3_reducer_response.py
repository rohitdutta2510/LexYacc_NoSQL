import sys
import datetime

range_start = list(map(int, sys.argv[1].split('/')))
range_end = list(map(int, sys.argv[2].split('/')))

try:
    range_start = datetime.date(range_start[2],range_start[1],range_start[0])
    range_end = datetime.date(range_end[2],range_end[1],range_end[0])
except:
    print('\nInvalid date !!\n')
    sys.exit()

# print(range_start,range_end)

for line in sys.stdin:
    org_date,response = line.strip().split()
    try:
        date = list(map(int,org_date.split('_')))
    except:
        continue
    date = datetime.date(date[2],date[1],date[0])
    if date >= range_start and date <= range_end:
        print('/'.join(org_date.split('_')),' '.join(response.split('_')))
