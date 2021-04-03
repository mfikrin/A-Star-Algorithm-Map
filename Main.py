def Euclidean(x1, x2, y1, y2):
    hasil = ((y2-y1)**2 + (x2-x1)**2)**(0.5)
    hasil = float("{:.2f}".format(hasil))
    # print(type(hasil))
    return(hasil)


class Graf:
    
    def __init__(self, number):
        self.number = number
        self.matrix = [[0 for j in range(number)] for i in range(number)]
    def add_element(self,i,j,jarak):
        self.matrix[i][j] = jarak
    def display_matrix(self):
        for i in range(self.number):
            for j in range(self.number):
                print(self.matrix[i][j], end="\t")
            print()

# Euclidean(5,3,2,9)
file_data = open("test/tc1.txt", "r")
data = file_data.readlines()
for i in range(len(data)):
    data[i] = data[i].replace("\n", "")

n_node = int(data[0])
print("n node ", n_node)
data.remove(data[0])
int_data = [[0 for j in range(2)] for i in range(len(data))]
for i in range(len(data)):
    string = data[i][2:len(data[i])]
    x = string.split(",")
    print(string)
    print(x)
    print(x[0])
    print(x[1])

    int_data[i][0] = int(x[0])
    int_data[i][1] = int(x[1])



for i in range(len(int_data)):
    for j in range(2):
        print(int_data[i][j],end= " ")
    print()

g = Graf(n_node)
g.display_matrix()

print(data)
    

for i in range(len(data)):
    for j in range(i+1,len(data)):
        m = int_data[i]
        n = int_data[j]
        print(m, end=" ")
        print(n, end=" ")

        x1 = m[0]
        y1 = m[1]
        x2 = n[0]
        y2 = n[1]
        jarak = Euclidean(x1,x2,y1,y2)
        print(jarak)
        # matriks_adj[i][j] = jarak
        g.add_element(i,j,jarak)
        # matriks_adj[j][i] = jarak
        g.add_element(j,i,jarak)
        # matriks_adj[i][i] = 0
        g.add_element(i,i,0)

g.display_matrix()
