import os
import sys

countries = ['Australia','India','England','Malaysia','Singapore']
country_name = sys.argv[1]

news_dict = {country : [] for country in countries}

if country_name in countries:
    for line in sys.stdin:
        contents = line.strip().split('_')
        news_dict[contents[0]].append(contents)

    country_news = news_dict[country_name]   # Gets lists of list
    print(f'For {country_name} the following news as per timeline are available:')
    i = 1
    for news in country_news:
        if len(news) == 2:
            year = news[-1].split('.')[0]
            print(f'{i}){year}')
            i += 1
        elif len(news) == 4:
            year = news[-1].split('.')[0]
            print(f'{i}){year} - from {news[1]} to {news[2]}')
            i += 1
    
    choice = int(input('\nEnter your choice number :'))
    if choice <= 0 and choice >= len(country_news): # Invalid Choice
        print('\nInvalid Choice given !!!\n')
        sys.exit()
    else: # Valid choice
        file_name = country_news[choice-1]
        file_name = '_'.join(file_name)
        curr_dir = os.getcwd()
        target_path = os.path.join(curr_dir,'worldwide_country',file_name)
        fp = open(target_path,'r')
        file_contents = fp.read().strip()
        print(file_contents)

else:
    print('\nInvalid country name given !!!\n')

