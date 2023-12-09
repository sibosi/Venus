print('Test: ', __file__)

from time import sleep
for i in range(24):
    sleep(5)
    print('Zzz (I sleep)')

print(f'Test ({__file__}) done')
