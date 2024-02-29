import os
from datetime import datetime

def writeFile(filename, text):
    f=open(filename,'w',encoding="utf-8")
    f.write(text)
    f.close

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

def main():
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

        elif choice == 2:
            print('\n---- Stats Menu ----')
            print('1. Total Cases')
            print('2. Active Cases')
            print('3. Total Deaths')
            print('4. Total Recovered')
            print('5. Total Tests')
            print('6. Death/Million')
            print('7. Tests/Million')
            print('8. New Case')
            print('9. New Death')
            print('10. New Recovered')
            print('11. Change in active cases in %')
            print('12. Change in daily deaths in %')
            print('13. Change in new cases in %')
            print('14. Change in new recovered in %')

            option = int(input('\nEnter your choice : '))

            if option == 1:
                pass
            elif  option == 2:
                pass
            elif  option == 3:
                pass
            elif  option == 4:
                pass
            elif  option == 5:
                pass
            elif  option == 6:
                pass
            elif  option == 7:
                pass
            elif  option == 8:
                pass
            elif  option == 9:
                pass
            elif  option == 10:
                pass
            elif  option == 11:
                pass
            elif  option == 12:
                pass
            elif  option == 13:
                pass
            elif option == 14:
                pass

        elif choice == 3:
            pass
        elif choice == 4:
            exit()


if __name__ == '__main__':
    main()