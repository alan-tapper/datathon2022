import matplotlib.pyplot as plt
import numpy as np
from os import path

mc = "#aa3333"
# bar graph for pages

count = {}

z = True
with open(path.dirname(__file__) + '/../bill_challenge_datasets/Training/training_graph.csv') as fil:
    for line in file.readlines(fil):
        ai, bi = tuple(line.strip().split(','))
        if z:
            z = False
            continue
        a = int(ai)
        b = int(bi)
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
        if b in count:
            count[b] += 1
        else:
            count[b] = 1

to_d = []
for val in range(1 + max(count.values())):
    to_d.append(0)

for val in count.values():
    to_d[val] += 1



fig, ax = plt.subplots()
ax.plot(list(range(121)), to_d[:121], color=mc)
ax.set_title("Nodes by degree")
plt.show()
