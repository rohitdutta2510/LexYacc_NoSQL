import os
from datetime import datetime

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
      os.system(f'python {file_path}')
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")

# function to execute mapper.py, combiner.py, reducer.py files
def execute_map_combine_reduce(call):
   try:
      os.system(f'python {call}')
   except FileNotFoundError:
      print(f"Error: Failed to execute {call}")


# main handler
def main():

    map_reduce_stats = 'python module3_mapper_stats.py | sort | python module3_combiner_stats.py | sort | python module3_reducer_stats.py '
    map_reduce_news = 'python module3_mapper_news.py | sort | python module3_combiner_news.py | sort | python module3_reducer_news.py '

    while True:
        print('---- Stats & News - Covid-19 ----')
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

            option = int(input('\nEnter your choice : '))
            country = input('\nEnter country name : ')

            if option == 1:
                call = map_reduce_stats + country + ' Total_Cases'
                execute_map_combine_reduce(call)

            elif  option == 2:
                call = map_reduce_stats + country + ' Active_Cases'
                execute_map_combine_reduce(call)

            elif  option == 3:
                call = map_reduce_stats + country + ' Total_Deaths'
                execute_map_combine_reduce(call)

            elif  option == 4:
                call =  map_reduce_stats + country + ' Total Recovered'
                execute_map_combine_reduce(call)

            elif  option == 5:
                call =  map_reduce_stats + country + ' Total Tests'
                execute_map_combine_reduce(call)

            elif  option == 6:
                call =  map_reduce_stats + country + ' Deaths/Million'
                execute_map_combine_reduce(call)

            elif  option == 7:
                call =  map_reduce_stats + country + ' Tests/Million'
                execute_map_combine_reduce(call)

            elif  option == 8:
                call =  map_reduce_stats + country + ' New_Cases'
                execute_map_combine_reduce(call)

            elif  option == 9:
                call =  map_reduce_stats + country + ' New_Deaths'
                execute_map_combine_reduce(call)

            elif  option == 10:
                call =  map_reduce_stats + country + ' New_Recovered'
                execute_map_combine_reduce(call)

            elif  option == 11:
                print('\n>> Do you want to get the closest country based on the current query? (Y/N)')
                ip = input()
                if ip == 'Y' or ip == 'y':
                    print('Feature currently not available !!')
            elif  option == 12:
                print('\n>> Do you want to get the closest country based on the current query? (Y/N)')
                ip = input()
                if ip == 'Y' or ip == 'y':
                    print('Feature currently not available !!')
            elif  option == 13:
                print('\n>> Do you want to get the closest country based on the current query? (Y/N)')
                ip = input()
                if ip == 'Y' or ip == 'y':
                    print('Feature currently not available !!')
            elif option == 14:
                print('\n>> Do you want to get the closest country based on the current query? (Y/N)')
                ip = input()
                if ip == 'Y' or ip == 'y':
                    print('Feature currently not available !!')

        elif choice == 3:
            print('\n---- News Menu ----')
            print('1. Retrieve News')
            print('2. Retrieve Response')
            print('3. Retrieve Info Availibility')
            print('4. Retrieve Country News')

            option = int(input('\nEnter your choice : '))
            start_date = input('Enter Start Date (DD/MM/YYYY Format): ')
            end_date = input('Enter End Date (DD/MM/YYYY Format): ')

            if option == 1:
                call = map_reduce_news + start_date + ' ' + end_date
                execute_map_combine_reduce(call)

            elif  option == 2:
                pass
            elif  option == 3:
                pass
            elif  option == 4:
                pass
            
        elif choice == 4:
            exit()


if __name__ == '__main__':
    main()