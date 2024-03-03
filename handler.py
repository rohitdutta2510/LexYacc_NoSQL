import os
import sys
from datetime import datetime

# Linux -> cmd = 'python3' | Windows -> cmd = 'python3'
cmd = 'python'

# write to a text file
def writeFile(filename, text):
    f=open(filename,'w',encoding="utf-8")
    f.write(text)
    f.close

# get the last extraction date
def get_date_log():
    file = open('date_log.txt','r')
    date = file.read()
    file.close()
    return date

# function to execute .py files
def execute_python_file(file_path):
   try:
      os.system(f'{cmd} {file_path}')
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")

# function to execute mapper.py, combiner.py, reducer.py files
def execute_map_combine_reduce(call):
    try:
        os.system(call)
    except FileNotFoundError:
        print(f"Error: Failed to execute {call}")

# function to execute percentage calculation scripts
def execute_percent(country, stat_type):
    file_map = {11 : '_active_cases.txt ', 12 : '_daily_deaths.txt ', 13 : '_daily_cases.txt ', 14 : '_new_recovered.txt '}
    map_percent = f'{cmd} module3_mapper_percent.py '
    combine_reduce_percent = f' | sort | {cmd} module3_combiner_percent.py | sort | {cmd} module3_reducer_percent.py '

    start_date = input('Enter Start Date (DD/MM/YYYY Format): ')
    end_date = input('Enter End Date (DD/MM/YYYY Format): ')

    filename = country + file_map[stat_type]
    file_path = './Stats/' + filename

    if os.path.exists(file_path):
        call = map_percent + filename + combine_reduce_percent + start_date + ' ' + end_date
        execute_map_combine_reduce(call)
        return 1, start_date, end_date
    else:
        print(f"\nThe file '{filename}' doesnot exist !!")
        return 0, start_date, end_date
    
# function to execute closest country scripts
def execute_closest(country, stat_type, start_date, end_date):
    file_map = {11 : 'active_cases.txt ', 12 : 'daily_deaths.txt ', 13 : 'daily_cases.txt ', 14 : 'new_recovered.txt '}
    map_closest = f'{cmd} module3_mapper_closest.py ' + file_map[stat_type]
    combine_reduce = f'| sort | {cmd} module3_combiner_closest.py | sort | {cmd} module3_reducer_closest.py '

    call = map_closest + combine_reduce + start_date + ' ' + end_date + ' ' + country
    execute_map_combine_reduce(call)

# function to execute country news as given
def execute_countrynews():
    curr_dir = os.getcwd()
    target_dir = os.path.join(curr_dir,'worldwide_country')

    countries = ['Australia','India','England','Malaysia','Singapore']
    country_name = input('\nEnter the country name from the following (Australia/India/England/Malaysia/Singapore) : ')
    news_dict = {country : [] for country in countries}

    for txt_file in os.listdir(target_dir):
                contents = txt_file.strip().split('_')
                news_dict[contents[0]].append(contents)

    if country_name in countries:
        country_news = news_dict[country_name]   # Gets lists of list
        print(f'\nFor {country_name} the following news as per timeline are available:')
        i = 1
        for news in country_news:
            if len(news) == 2:
                year = news[-1].split('.')[0]
                print(f'{i}) {year}')
                i += 1
            elif len(news) == 4:
                year = news[-1].split('.')[0]
                print(f'{i}) {year} - from {news[1]} to {news[2]}')
                i += 1
        print('\nEnter your choice number :')
        choice = int(input())
        if choice <= 0 or choice >= len(country_news) + 1: # Invalid Choice
            print('\nInvalid Choice given !!!\n')

        else: # Valid choice
            file_name = country_news[choice-1]
            file_name = '_'.join(file_name)
            # print(file_name)
            call = f'{cmd} module3_countrynews_mapper.py '+file_name+ f' | sort | {cmd} module3_countrynews_combiner.py | sort | {cmd} module3_countrynews_reducer.py'
            execute_map_combine_reduce(call)

    else:
        print('\nInvalid country name given !!!\n')

# main handler
def main():

    map_reduce_stats = f'{cmd} module3_mapper_stats.py | sort | {cmd} module3_combiner_stats.py | sort | {cmd} module3_reducer_stats.py '
    map_reduce_news = f'{cmd} module3_mapper_news.py | sort | {cmd} module3_combiner_news.py | sort | {cmd} module3_reducer_news.py '
    map_reduce_response = f'{cmd} module3_mapper_response.py | sort | {cmd} module3_combiner_response.py | sort | {cmd} module3_reducer_response.py '
    map_reduce_info_range = f'{cmd} module3_country_mapper.py | sort | {cmd} module3_country_combiner.py | sort | {cmd} module3_country_reducer.py '

    while True:
        try:
            print('\n---- Stats & News - Covid-19 ----')
            print(f'\nData extracted on : {get_date_log()}\n')
            print('1. Get latest data [NOTE : This will take some time]')
            print('2. Stats Info')
            print('3. News / Response')
            print('4. Exit')

            choice = int(input('\nEnter your choice : '))
            
            if choice == 1:
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
                writeFile('date_log.txt', formatted_datetime)

                print('>> Extracting Covid-19 stats\n')
                execute_python_file('module1.py')
                
                print('>> Extracting Active Cases\n')
                execute_python_file('module1_1.py')
                
                print('>> Extracting Daily Deaths\n')
                execute_python_file('module1_2.py')

                print('>> Extracting New Recovered\n')
                execute_python_file('module1_3.py')

                print('>> Extracting New Cases\n')
                execute_python_file('module1_4.py')

                print('>> Extracting Covid-19 News\n')
                execute_python_file('module2_news.py')

                print('>> Extracting Covid-19 Response\n')
                execute_python_file('module2_response.py')

                print('>> Extracting Covid-19 Country Info\n')
                execute_python_file('module2_australia.py')
                execute_python_file('module2_england.py')
                execute_python_file('module2_india.py')
                execute_python_file('module2_malaysia.py')
                execute_python_file('module2_singapore.py')

            elif choice == 2:
                while True:
                    try:
                        print('\n---- Stats Menu ----')
                        print('1. Total Cases')
                        print('2. Active Cases')
                        print('3. Total Deaths')
                        print('4. Total Recovered')
                        print('5. Total Tests')
                        print('6. Deaths/Million')
                        print('7. Tests/Million')
                        print('8. New Cases')
                        print('9. New Deaths')
                        print('10. New Recovered')
                        print('11. Change in active cases in %')
                        print('12. Change in daily deaths in %')
                        print('13. Change in new cases in %')
                        print('14. Change in new recovered in %')
                        print('15. Return to previous menu')

                        option = int(input('\nEnter your choice : '))

                        if option == 15:
                            break

                        if option == 1:
                            country = input('\nEnter country name : ')
                            call = map_reduce_stats + country + ' Total_Cases'
                            execute_map_combine_reduce(call)

                        elif  option == 2:
                            country = input('\nEnter country name : ')
                            call = map_reduce_stats + country + ' Active_Cases'
                            execute_map_combine_reduce(call)

                        elif  option == 3:
                            country = input('\nEnter country name : ')
                            call = map_reduce_stats + country + ' Total_Deaths'
                            execute_map_combine_reduce(call)

                        elif  option == 4:
                            country = input('\nEnter country name : ')
                            call =  map_reduce_stats + country + ' Total_Recovered'
                            execute_map_combine_reduce(call)

                        elif  option == 5:
                            country = input('\nEnter country name : ')
                            call =  map_reduce_stats + country + ' Total_Tests'
                            execute_map_combine_reduce(call)

                        elif  option == 6:
                            country = input('\nEnter country name : ')
                            call =  map_reduce_stats + country + ' Deaths/Million'
                            execute_map_combine_reduce(call)

                        elif  option == 7:
                            country = input('\nEnter country name : ')
                            call =  map_reduce_stats + country + ' Tests/Million'
                            execute_map_combine_reduce(call)

                        elif  option == 8:
                            country = input('\nEnter country name : ')
                            call =  map_reduce_stats + country + ' New_Cases'
                            execute_map_combine_reduce(call)

                        elif  option == 9:
                            country = input('\nEnter country name : ')
                            call =  map_reduce_stats + country + ' New_Deaths'
                            execute_map_combine_reduce(call)

                        elif  option == 10:
                            country = input('\nEnter country name : ')
                            call =  map_reduce_stats + country + ' New_Recovered'
                            execute_map_combine_reduce(call)

                        elif  option == 11:
                            country = input('\nEnter country name : ')
                            flag, start_date, end_date = execute_percent(country, 11)
                            if flag == 1:
                                print('\nDo you want to retrieve the closest country based on current metrics? (Y/N) : ', end = '')
                                ip = input()
                                if ip == 'Y' or ip == 'y':
                                    execute_closest(country, 11, start_date, end_date)

                        elif  option == 12:
                            country = input('\nEnter country name : ')
                            flag, start_date, end_date = execute_percent(country, 12)
                            if flag == 1:
                                print('\nDo you want to retrieve the closest country based on current metrics? (Y/N) : ', end = '')
                                ip = input()
                                if ip == 'Y' or ip == 'y':
                                    execute_closest(country, 12, start_date, end_date)

                        elif  option == 13:
                            country = input('\nEnter country name : ')
                            flag, start_date, end_date = execute_percent(country, 13)
                            if flag == 1:
                                print('\nDo you want to retrieve the closest country based on current metrics? (Y/N) : ', end = '')
                                ip = input()
                                if ip == 'Y' or ip == 'y':
                                    execute_closest(country, 13, start_date, end_date)

                        elif option == 14:
                            flag, start_date, end_date = execute_percent(country, 14)
                            if flag == 1:
                                print('\nDo you want to retrieve the closest country based on current metrics? (Y/N) : ', end = '')
                                ip = input()
                                if ip == 'Y' or ip == 'y':
                                    execute_closest(country, 14, start_date, end_date)
                        
                        else:
                            print('\nInvalid option !!\n')

                    except:
                        continue

            elif choice == 3:
                while True:
                    try:
                        print('\n---- News Menu ----')
                        print('1. Retrieve News')
                        print('2. Retrieve Response')
                        print('3. Retrieve Info Availibility')
                        print('4. Retrieve Country News')
                        print('5. Return to main menu')

                        option = int(input('\nEnter your choice : '))

                        if option == 5:
                            break

                        if option == 1:
                            start_date = input('Enter Start Date (DD/MM/YYYY Format): ')
                            end_date = input('Enter End Date (DD/MM/YYYY Format): ')
                            call = map_reduce_news + start_date + ' ' + end_date
                            execute_map_combine_reduce(call)

                        elif  option == 2:
                            start_date = input('Enter Start Date (DD/MM/YYYY Format): ')
                            end_date = input('Enter End Date (DD/MM/YYYY Format): ')
                            call = map_reduce_response + start_date + ' ' + end_date
                            execute_map_combine_reduce(call)

                        elif  option == 3:
                            country = input('\nEnter country name : ')
                            call = map_reduce_info_range + country
                            execute_map_combine_reduce(call)

                        elif  option == 4:
                            execute_countrynews()
                        
                        else:
                            print('\nInvalid option !!\n')
                    except:
                        continue

            elif choice == 4:
                sys.exit(0)
            else :
                print('\nInvalid option !!\n')
        except:
            continue
            


if __name__ == '__main__':
    main()