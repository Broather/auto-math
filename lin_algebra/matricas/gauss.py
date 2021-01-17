import copy
mtx = [[1, 2, 0, -1],
       [3, 4, 2, 1],
       [-2, 1, 1, 1],
       [-1, -1, 2, 1]]


def print_mtx(mtx):
    for x in mtx:
        print(x)


def gauss(matrix):
    determinants = 1
    matrix_copy = copy.deepcopy(matrix)
# 1.sakārtot rindas lai galvenajā diagonālē nav nulles un pēc iespējas vairāk 1


# 2.dabūt zem katra galvenās diagonāles elementa 0
    # go through each row except the last row
    for k in range(len(matrix_copy)-1):
        # multiplicator is based on [k][k] element and the element below it
        print_mtx(matrix_copy)
        for j in range(k+1, len(matrix_copy)):
            reizinatajs = -1*matrix_copy[j][k]/matrix_copy[k][k]
            # izprintēt darbības: piem. (R1*(-1)+R2)
            print(f'R{k+1}*({reizinatajs})+R{k+2}')
            # each j-row element is based on selected k-row and multiplicator
            for i in range(len(matrix_copy)):
                matrix_copy[j][i] = matrix_copy[k][i] * \
                    reizinatajs + matrix_copy[j][i]
# 3.sareizināt kopā visas galvenās diagonāles elementus lai iegūtu determinantu
    print_mtx(matrix_copy)
    for i in range(len(matrix_copy)):
        determinants *= matrix_copy[i][i]
    return determinants

print(gauss(mtx))
