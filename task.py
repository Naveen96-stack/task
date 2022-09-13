import operator
with open("grocery.txt",'r') as f:
    data=f.read().split()
counts = dict()
for word in data:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
sorted_d = dict( sorted(counts.items(), key=operator.itemgetter(1),reverse=True))
for i,j in sorted_d.items():
    print(j,i)