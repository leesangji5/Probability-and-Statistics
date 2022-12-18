from random import randint
import matplotlib.pyplot as plt
from drawnow import *

fig = plt.figure(1)
n = 100
n_dice = 100
num = [0, 0, 0, 0, 0, 0]
count = 0

def show_plot():
    label = [
        '1 {0}%'.format(round(num[0]/count*100, 2)),
        '2 {0}%'.format(round(num[1]/count*100, 2)),
        '3 {0}%'.format(round(num[2]/count*100, 2)),
        '4 {0}%'.format(round(num[3]/count*100, 2)),
        '5 {0}%'.format(round(num[4]/count*100, 2)),
        '6 {0}%'.format(round(num[5]/count*100, 2))
    ]
    plt.bar(label, num, color='blue')
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    plt.axhline(y=count/6, color='r', linestyle='-')

for i in range(n):
    for j in range(n_dice):
        num[randint(1, 6)-1] += 1
        count += 1
    drawnow(show_plot)
plt.show()