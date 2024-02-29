import os

def splitter():
    years = ['2023','2024']
    for i in range(len(years)):
        fp = open('./worldwide_news/'+years[i]+'.txt','r')
        lines = [x.strip().split() for x in fp.readlines()]
        fp.close()

        month = ''
        for j in range(len(lines)):
            if len(lines[j]) == 1:
                if lines[j][0] != month:
                    month = lines[j][0]
                    f = open('./worldwide_news/'+years[i]+'_'+month+'.txt','w')
            if len(lines[j]):
                f.write(' '.join(lines[j])+'\n')

        f.close()
        os.remove('./worldwide_news/'+years[i]+'.txt')