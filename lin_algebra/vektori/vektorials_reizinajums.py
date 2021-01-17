import copy
from sympy import symbols
a = []
b = []


mtx = [list(symbols('i j k')),
       [a],
       [b]]



def minors(i, matrix):
    matrix_copy = copy.deepcopy(matrix)
    # removes row with index 0 and column with index i
    for row in range(len(matrix_copy)):
        selected_row = matrix_copy[row]
        del selected_row[i]
    del matrix_copy[0]
    return matrix_copy


def izvirzijums(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    atbilde = 0
    for i in range(len(matrix)):
        atbilde += matrix[0][i]*(-1)**(0+i)*izvirzijums(minors(i, matrix))
    return atbilde

print(f'Izvirzījums pēc {mtx[0]} rindas, no masīva {mtx} = {izvirzijums(mtx)}')
