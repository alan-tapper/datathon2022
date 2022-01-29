import matplotlib.pyplot as plt
import numpy as np
from os import path

mc = "#aa3333"
# bar graph for pages

count = [0, 0, 0, 0]

z = False
a, b = 0, 0
with open(path.dirname(__file__) + '/../bill_challenge_datasets/Training/random_subgraph.csv') as fil:
    for line in file.readlines(fil):
        if not z:
            z = True
            continue
        _, ia, ib = line.strip().split(',')
        a, b = int(ia), int(ib)

print(a, b)
