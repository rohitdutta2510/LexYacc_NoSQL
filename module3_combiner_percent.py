import sys

month_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}


for line in sys.stdin:
    try:
        date, stats = line.strip().split('|')
    except:
        sys.exit(1)

    stats = stats.strip()
    month, day, year = date.split()
    day = day.replace(',', '').strip()
    month = month.strip()
    year = year.strip()
    final_date = day + '/' + month_dict[month] + '/' + year

    print(final_date + '|' + stats)