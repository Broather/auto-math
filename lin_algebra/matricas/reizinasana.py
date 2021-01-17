from lin_algebra import matrica
A = [2,3]
B = [4,1]

def print_mat(matrix):
    for row in matrix:
        print(row)


def transplanacija(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix))]

print_mat(transplanacija(A))
