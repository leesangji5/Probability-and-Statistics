from random import randint
import matplotlib.pyplot as plt
from drawnow import *

fig = plt.figure(1)
n = 100
n_dice = 10000
num = [0]*11
label = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

def show_plot():
    plt.bar(label, num, color='blue')
    plt.xlabel('Number')
    plt.ylabel('Frequency')

for i in range(n):
    for j in range(n_dice):
        num[randint(1, 6) + randint(1, 6)-2] += 1
    drawnow(show_plot)
plt.show()