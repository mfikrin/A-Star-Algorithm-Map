def Euclidean(x1, x2, y1, y2):
    hasil = ((y2-y1)**2 + (x2-x1)**2)**(0.5)
    return(hasil)

file_data = open("D:\Semester 4 IP 4!!!\Strategi Algoritma (Stima)\Tubes & Tucil\Tucil 3 - A Star Algorithm Map\A-Star-Algorithm-Map\Test1.txt", "r")
data = file_data.readlines()
for i in range(len(data)):
    data[i] = data[i].replace("\n", "")
    data[i] = data[i].replace(",", "")



class Graf:
    def __init__(self, number, matrix):
        self.number = number
        self.matrix = matrix
    def display_matrix(self):
        for i in range(self.number):
            for j in range(self.number):
                print(self.matrix[i][j], end=" ")
            print()
    #def add_element()

mat1 = [[1,2],[3,2]]
g = Graf(len(mat1),mat1)
g.display_matrix()
print(data)
    
    