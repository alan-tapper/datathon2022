from os import path

right = []
z = True
with open(path.dirname(__file__) + "/test_labels.csv", "r") as fil:
    for line in fil.readlines():
        if z:
            z = False
            continue
        right.append(int(line.strip()))
h = 0
print("source,target")
with open(path.dirname(__file__) + "/../bill_challenge_datasets/Test Dataset/test_edges.csv", "r") as fil:
    for line in fil.readlines():
        if not z:
            z = True
            continue
        if right[h] == 1:
            print(line.strip())
        h += 1
