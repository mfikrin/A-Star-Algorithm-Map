class Graf:
    def __init__(self, number):
        self.number = number
        self.matrix = [[0 for j in range(number)] for i in range(number)]

    def add_element(self, i, j, jarak):
        self.matrix[i][j] = jarak

    def display_matrix(self):
        for i in range(self.number):
            for j in range(self.number):
                print(self.matrix[i][j], end="\t")
            print()