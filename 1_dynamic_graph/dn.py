from random import randint
import matplotlib.pyplot as plt
from drawnow import *

fig = plt.figure(1)
n = 100
n_dice = 100000
num = [0, 0, 0, 0, 0, 0]
label = ['1', '2', '3', '4', '5', '6']
i = 0

def show_plot():
    plt.bar(label, num, color='blue')
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    plt.axhline(y=(n_dice*(i+1))/6, color='r', linestyle='-')

for i in range(n):
    for j in range(n_dice):
        num[randint(1, 6)-1] += 1
    drawnow(show_plot)
plt.show()