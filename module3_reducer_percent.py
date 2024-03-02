import sys
import datetime

start_date = sys.argv[1]
end_date = sys.argv[2]
start_stat = None
end_stat = None

for line in sys.stdin:
    try:
        date, stats = line.strip().split('|')
    except:
        sys.exit(1)

    if date == start_date:
        start_stat = stats
    if date == end_date:
        end_stat = stats

if start_stat is not None and end_stat is not None:
    start_stat = float(start_stat)
    end_stat = float(end_stat)

    try:
        change_percentage = (end_stat - start_stat)/start_stat * 100
    except:
        change_percentage = 0
        
    print(f'\nChange percentage : {change_percentage}\n')