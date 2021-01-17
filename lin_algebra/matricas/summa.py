import copy

A = [[2,-1],[4,5],[1,-2]]
B = [[1,3],[-1,0],[2,4]]

def addi(mtx1, mtx2):
    addition = copy.deepcopy(mtx1)
    if len(mtx1) == len(mtx2):
        for i, row in enumerate(mtx1):
            for j, elem in enumerate(row):
                addition[i][j] = elem + mtx2[i][j]
    return addition

print(addi(A,B))