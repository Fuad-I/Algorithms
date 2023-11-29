import random
from datetime import datetime

lst = list()
for i in range(4):
    lst.append(input())
    for j in range(15):
        print()
random.shuffle(lst)
print(lst)

with open('Game.txt', 'a') as file:
    file.write('{}'.format(datetime.now()))
    file.write('\n')
    for word in lst:
        file.write(word)
        file.write('\n')
