filepath = './main_stats.txt'

file = open(filepath, 'r')

for line in file:
    details = line.strip().split('|')
    key = details[0]
    value = '|'.join(details[1:])
    print(key + '@' + value)

file.close()