import collections


difficulty = [3, 5, 9, 2, 3]
workers = [3, 9, 5]
profit = [6, 10, 18, 4, 6]

a = collections.defaultdict(int)



def maxProfitAssignment(difficulty, profit, worker):

    diffPro = collections.defaultdict(int)
    for diff, pro in zip(difficulty, profit):
        diffPro[diff] = max(diffPro[diff], pro)
    maxVal = 0
    for x in range(min(difficulty + worker), max(difficulty + worker) + 1):
        diffPro[x] = max(diffPro[x], maxVal)
        maxVal = max(diffPro[x], maxVal)
    return sum(diffPro[w] for w in worker)


print(maxProfitAssignment(difficulty, profit, workers))
