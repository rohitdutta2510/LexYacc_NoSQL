import os
import sys

file_type = sys.argv[1]

country_list = ['France', 'UK', 'Russia', 'Italy', 'Germany', 'Spain', 'Poland', 'Netherlands', 'Ukraine', 'Belgium', 'USA', 'Mexico', 
                'Canada', 'Cuba', 'Costa Rica', 'Panama', 'India', 'Turkey', 'Iran', 'Indonesia', 'Philippines', 'Japan', 'Israel', 
                'Malaysia', 'Thailand', 'Vietnam', 'Iraq', 'Bangladesh', 'Pakistan', 'Brazil', 'Argentina', 'Colombia', 'Peru', 'Chile', 
               "Bolivia", "Uruguay", "Paraguay", "Venezuela", "South_Africa", "Morocco", "Tunisia", "Ethiopia", "Libya", "Egypt", "Kenya", 
               "Zambia", "Algeria", "Botswana", "Nigeria", "Zimbabwe", "Australia", "Fiji", "Papua New Guinea", "New Caledonia", "New Zealand" ]

for country in country_list:
    filepath = './Stats/' + country + '_' + file_type

    try:
        fp = open(filepath, 'r')
    except:
        continue


    for line in fp:
        date, stats = line.strip().split('\t')
        date = date.strip()
        stats = stats.strip()

        print(date + '|' + country + '|' + stats)
