import matplotlib.pyplot as plt
import numpy as np
from os import path
import json

mc = "#aa3333"
# bar graph for pages

count = []
with open(path.dirname(__file__) + '/../bill_challenge_datasets/Training/node_classification.csv') as fil:
    for line in file.readlines(fil):
        _, b = tuple(line.strip().split(','))
        if b == "page_type":
            continue
        count.append(int(b))

conn = ["1-1", "1-2", "1-3", "1-4", "2-2", "2-3", "2-4", "3-3", "3-4", "4-4"]
fill = [0] * 10

jzon = json.load(open(path.dirname(__file__) + "/../bill_challenge_datasets/Training/node_features_text.json"))
for k, vs in jzon.items():
    for v in vs:
        t1, t2 = count[int(str(k))], count[int(v)]
        ye = str(min(t1, t2)) + "-" + str(max(t1, t2))
        fill[conn.index(ye)] += 1

ind = np.arange(10) + 1
fig, ax = plt.subplots()
plt.tick_params(left=False, bottom=False, right=False, top=False)
barr = ax.bar(ind, fill, edgecolor="1.0", color=mc, figsize=(13, 4.8))
# plt.figure(figsize=(13, 4.8))
ax.set_xticklabels(conn)
ax.set_title("Connections by page")
ax.legend()
plt.show()
