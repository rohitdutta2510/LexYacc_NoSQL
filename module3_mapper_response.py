import os

months = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}

curr_dir = os.getcwd()
target_dir = os.path.join(curr_dir,'worldwide_response')

dir_contents = os.listdir(target_dir)
# print(dir_contents)

for txt_file in dir_contents:
    year = txt_file[:4]
    month_name = txt_file[5:-4]
    file_path = os.path.join(target_dir,txt_file)
    fp = open(file_path,'r')
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
