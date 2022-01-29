import matplotlib.pyplot as plt
import numpy as np
from os import path

mc = "#aa3333"
# bar graph for pages

count = [0, 0, 0, 0]

with open(path.dirname(__file__) + '/../bill_challenge_datasets/Training/node_classification.csv') as fil:
    for line in file.readlines(fil):
        _, b = tuple(line.strip().split(','))
        if b == "page_type":
            continue
        count[int(b) - 1] += 1

ind = np.arange(4) + 1
fig, ax = plt.subplots()
plt.tick_params(left=False, bottom=False, right=False, top=False)
barr = ax.bar(ind, count, width=0.6, align="center", edgecolor="1.0", color=mc)
ax.set_title("Nodes by page")
ax.set_xticklabels(["", "Type 1", "", "Type 2", "", "Type 3", "", "Type 4"])
ax.legend()
plt.show()
