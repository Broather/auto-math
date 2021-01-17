import copy
test = [[1,2,-1],
       [3,-1,0],
       [2,3,-1]]

def print_mtx(mtx):
    for x in mtx:
        print(x)


def minors(i, j, matrix):
    matrix_copy = copy.deepcopy(matrix)
    # removes row with index j and column with index i
    for row in range(len(matrix_copy)):
        selected_row = matrix_copy[row]
        del selected_row[i]
    del matrix_copy[j]
    return matrix_copy


def izvirzijums(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    atbilde = 0
    for i in range(len(matrix)):
        atbilde += matrix[0][i]*(-1)**(0+i)*izvirzijums(minors(i, 0, matrix))
    return atbilde


def muli_const(const, matrix):
    return [[elem * const for elem in row] for row in matrix]


def transplanacija(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def adjunktu_matrica(matrix):
    matrix_copy = copy.deepcopy(matrix)
    matrix_copy_copy = copy.deepcopy(matrix_copy)
    for i in range(len(matrix_copy)):
        for j in range(len(matrix_copy)):
            matrix_copy_copy[i][j] = (-1)**(i+j) * \
                izvirzijums(minors(i, j, matrix_copy))
    # for some reason I get an inverse of what I want
    return matrix_copy_copy


def inverss(matrix):
    if izvirzijums(matrix) == 0:
        print(
            f'matricai {matrix} neeksistē inversa matrica, jo tās determinants ir 0')
        return matrix
    else:
        atbilde = muli_const(
            (1/izvirzijums(matrix)), adjunktu_matrica(matrix))
        return atbilde


# print_mtx(inverss(test))
print_mtx(inverss(test))
