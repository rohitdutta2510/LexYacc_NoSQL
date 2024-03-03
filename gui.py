import tkinter as tk
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

def execute_python_file(file_path):
   try:
      os.system(f'python {file_path}')
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")

def func1():
    global res
    choice = inp_label.get()
    if choice == '1':
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
        res.set('Latest Data Update Done')

window = tk.Tk()
window.title('---- Stats & News - Covid-19 ----')

res = tk.StringVar()
res.set("")

datelabel = tk.Label(window, text = f'\nData extracted on : {get_date_log()}\n')
label0 = tk.Label(window, text = 'Enter:')
label1 = tk.Label(window, text = '1. Get latest data [NOTE : This will take some time]')
label2 = tk.Label(window, text = '2. Stats Info')
label3 = tk.Label(window, text = '3. News / Response')
inp_label = tk.Entry(window)
inp_button = tk.Button(window,text='OK',command=func1)
op_label = tk.Label(window,textvariable= res)

datelabel.grid(row = 0, column = 0, sticky='W')
label0.grid(row = 1, column = 0, sticky='W')
label1.grid(row = 2, column = 0, sticky='W')
label2.grid(row = 3, column = 0, sticky='W')
label3.grid(row = 4, column = 0, sticky='W')
inp_label.grid(row = 5, column = 0)
inp_button.grid(row = 6, column = 0)
op_label.grid(row = 7, column = 0, sticky = 'W')

window.mainloop()