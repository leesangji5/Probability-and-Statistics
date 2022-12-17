from random import randint
import matplotlib.pyplot as plt

user_score = 0
user_tie = 0
user_lose = 0

n = 100000
for i in range(n):
    user1 = randint(1, 3)
    user2 = randint(1, 3)
    if user1 == user2:
        user_tie += 1
    elif user1 == 1 and user2 == 2:
        user_lose += 1
    elif user1 == 1 and user2 == 3:
        user_score += 1
    elif user1 == 2 and user2 == 1:
        user_score += 1
    elif user1 == 2 and user2 == 3:
        user_lose += 1
    elif user1 == 3 and user2 == 1:
        user_lose += 1
    else:
        user_score += 1

label = ['Score', 'Tie', 'Lose']
num = [user_score, user_tie, user_lose]

plt.bar(label, num, color='blue')
plt.xlabel('Result')
plt.ylabel('Frequency')
plt.title('Frequency of Result')
plt.axhline(y=n/3, color='r', linestyle='-')
plt.show()