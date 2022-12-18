from random import randint
import matplotlib.pyplot as plt
from drawnow import *

fig = plt.figure(1, figsize=(10, 6))
n = 100
n_dice = 3600
num = [0]*11
count = 0

def show_plot():
    label = [
        '2 {0}%'.format(round(num[0]/count*100, 1)),
        '3 {0}%'.format(round(num[1]/count*100, 1)),
        '4 {0}%'.format(round(num[2]/count*100, 1)),
        '5 {0}%'.format(round(num[3]/count*100, 1)),
        '6 {0}%'.format(round(num[4]/count*100, 1)),
        '7 {0}%'.format(round(num[5]/count*100, 1)),
        '8 {0}%'.format(round(num[6]/count*100, 1)),
        '9 {0}%'.format(round(num[7]/count*100, 1)),
        '10 {0}%'.format(round(num[8]/count*100, 1)),
        '11 {0}%'.format(round(num[9]/count*100, 1)),
        '12 {0}%'.format(round(num[10]/count*100, 1))
    ]
    plt.bar(label, num, color='blue')
    plt.xlabel('Number')

for i in range(n):
    for j in range(n_dice):
        num[randint(1, 6) + randint(1, 6)-2] += 1
        count += 1
    drawnow(show_plot)
plt.show()