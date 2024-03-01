import sys
import datetime

# range_start = list(map(int,input('Enter Range Start Date (DD/MM/YYYY Format): ').split('/')))
# range_end = list(map(int,input('Enter Range End Date (DD/MM/YYYY Format): ').split('/')))

range_start = [5,7,2021]
range_end = [5,7,2022]

range_start = datetime.date(range_start[2],range_start[1],range_start[0])
range_end = datetime.date(range_end[2],range_end[1],range_end[0])

for line in sys.stdin:
    org_date,news = line.strip().split()
    try:
        date = list(map(int,org_date.split('_')))
    except:
        continue
    date = datetime.date(date[2],date[1],date[0])
    if date >= range_start and date <= range_end:
        print('/'.join(org_date.split('_')),' '.join(news.split('_')))