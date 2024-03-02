import sys

if len(sys.argv) < 3:
    print('Inadeqaute command line arguments; Required 2')

country = sys.argv[1]
choice = sys.argv[2]
world = None
cnt_stats = None

for line in sys.stdin:
    key, value = line.strip().split('@')
    stats = value.strip().split('|')
    key = key.strip()
    # print(key)

    if key == country:
        if choice == 'Total_Cases':
            print(f'\nTotal Cases : {stats[0]}')
            cnt_stats = stats[0]

        if choice == 'Active_Cases':
            print(f'\nActive Cases : {stats[6]}')
            cnt_stats = stats[6]

        if choice == 'Total_Deaths':
            print(f'\nTotal Deaths : {stats[2]}')
            cnt_stats = stats[3]

        if choice == 'Total_Recovered':
            print(f'\nTotal Recovered : {stats[4]}')
            cnt_stats = stats[4]

        if choice == 'Total_Tests':
            print(f'\nTotal Tests : {stats[10]}')
            cnt_stats = stats[10]

        if choice == 'Deaths/Million':
            print(f'\nDeath/Million : {stats[9]}')
            cnt_stats = stats[9]

        if choice == 'Tests/Million':
            print(f'\nTests/Million : {stats[11]}')
            cnt_stats = stats[11]

        if choice == 'New_Cases':
            print(f'\nNew Cases : {stats[1]}')
            cnt_stats = stats[1]

        if choice == 'New_Deaths':
            print(f'\nNew Deaths : {stats[3]}')
            cnt_stats = stats[3]

        if choice == 'New_Recovered':
            print(f'\nNew Recovered : {stats[5]}')
            cnt_stats = stats[5]
    
    if key == 'World':
        if choice == 'Total_Cases':
            world = stats[0]

        if choice == 'Active_Cases':
            world = stats[6]

        if choice == 'Total_Deaths':
            world = stats[3]

        if choice == 'Total_Recovered':
            world = stats[4]

        if choice == 'Total_Tests':
            world = stats[10]

        if choice == 'Deaths/Million':
            world = stats[9]

        if choice == 'Tests/Million':
            world = stats[11]

        if choice == 'New_Cases':
            world = stats[1]

        if choice == 'New_Deaths':
            world = stats[3]

        if choice == 'New_Recovered':
            world = stats[5]

# print(world)    

if world != 'N/A' and cnt_stats != 'N/A':
    world = list(world)
    cnt_stats = list(cnt_stats)
    # if '+' in world:
    #     world.remove('+')
    # if '+' in cnt_stats:
    #     cnt_stats.remove('+')
    # if ',' in world:
    #     world.remove(',')
    # if ',' in cnt_stats:
    #     cnt_stats.remove(',')

    world = [x for x in world if x not in ['+', ',']]
    cnt_stats = [x for x in cnt_stats if x not in ['+', ',']]
    
    world = float(''.join(world))
    cnt_stats = float(''.join(cnt_stats))

    print(f'\nWorld Percentage : {cnt_stats/world * 100}\n')
else:
    print('\nWorld percentage for N/A data not possible\n')
