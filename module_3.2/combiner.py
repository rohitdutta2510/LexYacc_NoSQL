import sys

curr_date = ''
curr_news = []
for line in sys.stdin:
    date,news = line.strip().split()
    if date != curr_date:
        curr_news.append(news)
        curr_date = date