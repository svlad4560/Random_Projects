import operator
stats = {'a':1000, 'b':3000, 'c': 100, 'd':30000}

print(max(stats.items(), key=operator.itemgetter(1))[0])
