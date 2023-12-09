print('Test: ', __file__)

from time import sleep
for i in range(30):
    sleep(5)
    print(i, 'Ááá (I wake up)')

print(f'Test ({__file__}) done')
