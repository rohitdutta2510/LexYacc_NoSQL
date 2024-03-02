import sys

curr_date = ''
curr_news = []
for line in sys.stdin:
    date,news = line.strip().split()
    print(date,news)