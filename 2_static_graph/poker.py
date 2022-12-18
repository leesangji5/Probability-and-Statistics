import random
# 422160번당 1회

n = 4331600
result = 0
for i in range(n):
    a = random.sample(range(1, 53), 6)
    if 1 in a and 2 in a and 3 in a and 4 in a and 5 in a:
        result += 1

print(result)