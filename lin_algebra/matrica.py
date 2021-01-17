
class matrica:
    def __init__(self, matrix):
        self.matrix = matrix

    def transplanacija(self):
        return [[row[i] for row in self.matrix] for i in range(len(self.matrix))]


matrix = [[1, 2],
          [3, 4]]

my_matrix = matrica(matrix)

for row in my_matrix.transplanacija().transplanacija():
    print(row)


for row in matrix:
    print(row)