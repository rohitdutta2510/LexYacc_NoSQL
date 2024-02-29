import sys

filepath = '../Stats.txt'

while(True):
    country = input('\nEnter country name : ')
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
    choice = int(input('\nEnter choice : '))

    file = open(filepath, 'r')

    for line in file:
        details = line.split('\t')
        # print(details)
        if details[0] == country:
            # print(country)
            if choice == 1:
                print(details[1])
            elif choice == 2:
                print(details[7])
            elif choice == 3:
                print(details[3])
            elif choice == 4:
                print(details[5])
            elif choice == 5:
                print(details[11])
            elif choice == 6:
                print(details[10])
            elif choice == 7:
                print(details[12])
            elif choice == 8:
                print(details[2])
            elif choice == 9:
                print(details[4])
            elif choice == 10:
                print(details[6])