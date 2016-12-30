import random

def CDF(index, lst):
    ans = []
    for i in range(len(lst)):
        ans.append(sum(lst[0:i+1]))

    for i in range(len(lst)):
        if index > lst[i]:
            index = index - lst[i]
        else:
            return i

x = CDF(random.random(), [0.1,0.2,0.7])
print x
