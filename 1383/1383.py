import random
import numbers

n = 10

speed = []
efficiency = []

i = n

for i in range(10):
    speed.append(random.randint(1,10))
    efficiency.append(random.randint(1, 10))


print(speed)
print(efficiency)

def get_best_workers(k):
    quality = [speed[x]*efficiency[x] for x in range(n)]
    quality.sort()
    return sum(quality[-k:])

