# 0,1,2,3,4,5,6
G = [
    [0, 0, 0, 0, 3, 0, 0],  # 0
    [1, 0, 1, 0, 1, 0, 0],  # 1
    [0, 1, 0, 1, 0, 0, 0],  # 2
    [0, 0, 1, 0, 1, 1, 0],  # 3
    [1, 1, 0, 1, 0, 0, 0],  # 4
    [0, 0, 0, 1, 0, 0, 0],  # 5
    [0, 0, 0, 1, 0, 0, 0],  # 6
]
# 7 * 7 matrix
for i, node in enumerate(G):
    print("Node " + str(i) + " is connectedis the following edge")
    for index, edge in enumerate(node):
        if edge == 1:
            print(index)
