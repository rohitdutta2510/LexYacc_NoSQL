import os

months = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
cwd = os.getcwd()
ls = os.listdir(cwd+'\\worldwide_news')
for file in ls:
    year = file[:4]
    month_name = file[5:-4]
    fp = open(cwd+'\\worldwide_news\\'+file,'r')
    lines = [x.strip().split() for x in fp.readlines()]
    fp.close()
    f = 0
    for line in lines:
        if len(line) == 2:
            day = line[0]
            f = 1
        elif f == 1:
            print(day+'_'+months[month_name]+'_'+year+' '+'_'.join(line))
            f = 0