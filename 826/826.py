import random
import collections

difficulty = []
profit = []
worker = []

[difficulty.append(random.randint(1, 10)) for i in range(10)]
[profit.append(i*5) for i in difficulty]
[worker.append(random.randint(1, 10)) for i in range(5)]


def maxProfitAssignment(difficulty, profit, worker):

    print(difficulty)
    print(profit)
    print(worker)

    diffPro = collections.defaultdict(int)
    for diff, pro in zip(difficulty, profit):
        diffPro[diff] = max(diffPro[diff], pro)
    maxVal = 0
    for x in range(min(difficulty + worker), max(difficulty + worker) + 1):
        diffPro[x] = max(diffPro[x], maxVal)
        maxVal = max(diffPro[x], maxVal)
    return sum(diffPro[w] for w in worker)


print(maxProfitAssignment(difficulty, profit, worker))
