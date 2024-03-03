import sys

countries = ['Australia','India','England','Malaysia','Singapore']
country_name = sys.argv[1]
data_dict = {country : set() for country in countries}
# print(data_dict)

if country_name in countries:
    for line in sys.stdin:
        contents = line.strip().split('_')
        data_dict[contents[0]].add(contents[-1])
    
    years = sorted(data_dict[country_name])
    if years[0] != years[-1]:
        print(country_name+' '+years[0]+'-'+years[-1]+' response is available.')  #{country_name} {start_year} - {end_year}
    else:
        print(country_name+' '+years[0]+' response is available.')   #{country_name} {year}
    print('\n')
else:
    print('\nInvalid country name given !!!\n')

            