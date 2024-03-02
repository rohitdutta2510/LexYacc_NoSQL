import sys

start_date = sys.argv[1]
end_date = sys.argv[2]
reference_country = sys.argv[3]

country_name = []
start_stat = {}
end_stat = {}
lowest_diff = 9999999999
closest_country = None

for line in sys.stdin:
    date, country, stats = line.strip().split('|')

    if date == start_date:
        country_name.append(country)
        start_stat[country] = float(stats)
    
    elif date == end_date:
        end_stat[country] = float(stats)

reference_percentage = (end_stat[reference_country] - start_stat[reference_country]) / start_stat[reference_country] + 1e-10

for country in country_name:
    if country == reference_country:
        continue
    try:
        curr_percentage = (end_stat[country] - start_stat[country]) / start_stat[country]
    except:
        curr_percentage = 0
        
    if abs(reference_percentage - curr_percentage) < lowest_diff:
        lowest_diff = abs(reference_percentage - curr_percentage)
        closest_country = country

print(closest_country)