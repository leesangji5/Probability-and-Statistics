from random import randint
import matplotlib.pyplot as plt
from drawnow import *

fig = plt.figure(1)
num = [0, 0, 0]
n = 100
n_rcp = 10
count = 0

def rcp():
    user1 = randint(1, 3)
    user2 = randint(1, 3)
    if user1 == user2:
        num[1] += 1
    elif user1 == 1 and user2 == 2:
        num[2] += 1
    elif user1 == 1 and user2 == 3:
        num[0] += 1
    elif user1 == 2 and user2 == 1:
        num[0] += 1
    elif user1 == 2 and user2 == 3:
        num[2] += 1
    elif user1 == 3 and user2 == 1:
        num[2] += 1
    else:
        num[0] += 1

def show_plot():
    label = [
            'Score {0}%'.format(round(num[0]/count*100, 2)),
            'Tie {0}%'.format(round(num[1]/count*100, 2)),
            'Lose {0}%'.format(round(num[2]/count*100, 2))
    ]
    plt.bar(label, num, color='blue')
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    plt.axhline(y=count/3, color='r', linestyle='-')

for i in range(n):
    for j in range(n_rcp):
        rcp()
        count += 1
    drawnow(show_plot)
plt.show()