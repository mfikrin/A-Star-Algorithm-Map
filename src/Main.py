import os
import matplotlib.pyplot as plt

def Euclidean(x1, x2, y1, y2):
    hasil = ((y2-y1)**2 + (x2-x1)**2)**(0.5)
    hasil = float("{:.2f}".format(hasil))
    # hasil = int(hasil)
    # print(type(hasil))
    return(hasil)

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def display_mat(matriks,n_row,n_col):
    for i in range(n_row):
        for j in range(n_col):
            print(matriks[i][j], end="\t")
        print()

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
print("-----------------------------")
print("|  Silahkan input nama file |")
print("|        (eg : tc1)         |")
print("|   (Tanpa ekstensi file)   |")
print("-----------------------------")

print()

# filename = input("Input nama file : ") # dicomment buat sementara agar mudah
filename1 = "tc1"
filename2 = "tc1_2"
test = "./test/"
path1 = test + filename1 + ".txt"
path2 = test + filename2 + ".txt"

isfile1 = os.path.isfile(path1)
isfile2 = os.path.isfile(path2)

# Melakukan pengecekan apakah filename terdapat pada folder test atau tidak
while (not isfile1):
    filename1 = input("Ulangi input nama file 1 : ")
    path1 = test + filename1 + ".txt"
    isfile1 = os.path.isfile(path1)

while (not isfile2):
    filename2 = input("Ulangi input nama file 2 : ")
    path2 = test + filename2 + ".txt"
    isfile2 = os.path.isfile(path2)

file_data = open(path1, "r")
file_edge = open(path2, "r")

data = file_data.read().splitlines() # baca file teks (dengan readlines yang sekaligus hapus \n)
edge = file_edge.read().splitlines()

n_node = int(data[0])
print("n node ", n_node)
data.remove(data[0])
int_data = [[0 for j in range(2)] for i in range(len(data))]

arr_node = []
for i in range(len(data)):

    node = data[i][0]
    arr_node.append(node)
    string = data[i][2:len(data[i])]
    x = string.split(",")
    # print(string)
    # print(x)
    # print(x[0])
    # print(x[1])

    int_data[i][0] = int(x[0])
    int_data[i][1] = int(x[1])
print("ARR NODE")
print(arr_node)

dict = {}
idx = 0
for node in arr_node:
    dict[node] = idx
    idx+= 1

print("DICt")
print(dict)

mat_edge = [[0 for j in range(n_node)] for i in range(n_node)]

baris = 0
kolom = 0
# print(edge)
for i in range(len(edge)):
    # print(len(file[i]))
    # print(str(i) + "woi")
    for j in range(len(edge[i])):
        # print(files[i][j])
        if j % 2 == 0:
            mat_edge[baris][kolom] = int(edge[i][j])
            kolom += 1
    baris += 1
    kolom = 0


# for i in range(8):
#     for j in range(8):
#         print(mat_edge[i][j], end=" ")
#     print()

display_mat(mat_edge,n_node,n_node)

# for i in range(len(int_data)):
#     for j in range(2):
#         print(int_data[i][j],end= " ")
#     print()

display_mat(int_data,n_node,2)

g = Graf(n_node)
# g.display_matrix()

# print(data)
#
# print()
for i in range(len(data)):
    for j in range(i+1,len(data)):
        m = int_data[i]
        n = int_data[j]
        # print(m, end=" ")
        # print(n, end=" ")

        x1 = m[0]
        y1 = m[1]
        x2 = n[0]
        y2 = n[1]
        jarak = Euclidean(x1,x2,y1,y2)
        # print(jarak)
        # matriks_adj[i][j] = jarak
        g.add_element(i,j,jarak)
        # matriks_adj[j][i] = jarak
        g.add_element(j,i,jarak)
        # matriks_adj[i][i] = 0
        g.add_element(i,i,0)

print("bobot semua")
g.display_matrix()
# 0       1.41    7.28    5.0     7.28    5.1     1.0     4.47
# 1.41    0       8.54    5.0     8.06    6.32    1.0     5.83
# 7.28    8.54    0       7.21    4.0     2.24    7.62    3.0
# 5.0     5.0     7.21    0       4.47    5.39    4.24    6.08
# 7.28    8.06    4.0     4.47    0       3.61    7.07    5.0
# 5.1     6.32    2.24    5.39    3.61    0       5.39    1.41
# 1.0     1.0     7.62    4.24    7.07    5.39    0       5.0
# 4.47    5.83    3.0     6.08    5.0     1.41    5.0     0
mat_mix = [[0 for j in range(n_node)] for i in range(n_node)]

for i in range(8):
    for j in range(8):
        if mat_edge[i][j] == 1:
            mat_mix[i][j] = g.matrix[i][j]


# for i in range(8):
#     for j in range(8):
#         print(mat_mix[i][j], end="\t")
#     print()
print("woi")
display_mat(mat_mix,n_node,n_node)
print("a*")


dict_temp = {}
idx = 0
for node in arr_node:
    dict_temp[node] = 0



# A B
# A C
# B D
# C F
# D H
# E G
# E H
# F G

# rute = ["A","B"]
def calculate_gn(rute,nodeN):
    gn = 0
    for i in range(len(rute)):
        if (i != len(rute) - 1):
            gn += mat_mix[dict[rute[i]]][dict[rute[i+1]]] 
        else:
            gn += mat_mix[dict[rute[i]]][dict[nodeN]]
    return gn

print("HELOOOW")
# nilai = calculate_gn(rute,"D")

# print(nilai)
    
def get_key(val):
    for node,value in dict.items():
         if val == value:
             return node

arrs = [[7.24, 1], [10.280000000000001, 2]]
def min_arr(arr_total): # return node yg minimal total dr gn + hn nya
    min = arr_total[0][0]
    idx_min = 0
    for i in range(1,len(arr_total)):
        if (arr_total[i][0] < min):
            min = arr_total[i][0]
            idx_min = i
    return idx_min
a = min_arr(arrs)
print("AAA")
print(a)

# get_key(arr_total[idx_min][1])

# def get_node(rute):
#     for i in range()

arr = []

# A = [1,2,3]
def copy_arr(arr):
    neo = []
    for i in range(len(arr)):
        neo.append(arr[i])
    return neo

# def modif_arr(arr,arr_modif):
#     # arr = []
#     # arr.clear()
#     for i in range(len(arr_modif)):
#         arr.append(arr_modif)

# copy_arr(A)

# def is_in_arr(nodeGoal,arr):


rute = []
def a_star(nodeAwal, nodeAkhir,iterasi): #nodeAwal dan nodeAkhir int

    iterasi += 1

    rute.append(nodeAwal)
    print("RUTE")
    print(rute)

    for i in range(len(mat_mix[dict[nodeAwal]])):
        if mat_mix[dict[nodeAwal]][i] != 0 :
            # gn = mat_mix[dict[nodeAwal]][i]
            # path = []
            print("i :" + str(i))
            nodeN = get_key(i)

            gn = calculate_gn(rute,nodeN)
            print("gn :"+str(gn))
            hn = g.matrix[i][dict[nodeAkhir]]
            print("hn :"+str(hn))
            total = gn + hn
            print("total :" +str(total))
            # path.append(dict[nodeAwal])
            # path.append(i)
            # print("APPEND")
            # print(path)
            rute.append(get_key(i))
            copy_rute = copy_arr(rute)
            print(rute)
            arr_total = [total,copy_rute]
            print("ARR TOTAL")
            print(arr_total)
            arr.append(arr_total)
            print("ARR")
            print(arr)
            del rute[len(rute)-1:len(rute)]
            print("RUTE")
            print(rute)
            print("ARR TOTA")



    print("ARRRRRR")
    print(arr)
    idx_min = min_arr(arr)
    # print(arr)
    # rute.append(get_key(arr[idx_min][1]))
    temp = arr[idx_min]
    print("yemp")
    print(temp)
    del arr[idx_min:idx_min + 1]
    print("AFTER DELE")
    print(arr)
    print(rute)
    print(str(iterasi) + "Selesai")
    # print(temp[1])
    node = temp[1][len(temp[1])-1]
    if (node == nodeAkhir):
        print("Rute Terpendek : ")
        jarak = calculate_gn(rute,node)
        rute.append(node)
        print("rute : ", end=" ")
        print(rute)
        print("Iterasi : " + str(iterasi))
        print("Jarak : " + str(jarak))

    else:
        print(dict[temp[1][len(temp[1])-1]])
        # rute.clear()
        # print("before modif")
        # print(rute)
        # # modif_arr(rute,temp[1])
        # print("After modif")
        # print(rute)
        rute.clear()

        for i in range(len(temp[1])):
            rute.append(temp[1][i])
        print("RUTE ABIS CLEAR")
        print(rute)
        del rute[len(rute)-1:len(rute)]
        # rute = temp[1]
        # rute = copy_arr(temp[1])
        # rute = copy_arr(temp[1])
        a_star(get_key(dict[temp[1][len(temp[1])-1]]),nodeAkhir,iterasi)



def Get_Short_Path(nodeAwal,nodeAkhir):
    iterasi = 0
    a_star(nodeAwal,nodeAkhir,iterasi)
# arrr = ["A","B","D"]
#
# totals = calculate_gn(arrr,"H")
# print(totals)

Get_Short_Path("A","H")
# # x axis values
# x = [5,4,1,7,3,4,6,7,5]
# # corresponding y axis values
# y = [2,1,5,6,9,2,7,9,2]
# plt.plot(x, y, label = "line 1", marker='o')

axis = []
ordinat = []
for i in range(n_node):
    for j in range(n_node):
        if mat_edge[i][j] == 1:
            varx = [int_data[i][0],int_data[j][0]]
            vary = [int_data[i][1],int_data[j][1]]
            axis.append(varx)
            ordinat.append(vary)

print(axis)
print(ordinat)
# fake_axis = [[5, 4], [5, 7], [4, 1], [7, 6], [1, 7], [3, 4], [3, 7], [6, 4]]
# fake_ordinat = [[2, 1], [2, 9], [1, 5], [9, 7], [5, 6], [9, 2], [9, 6], [7, 2]]
for i in range(len(axis)):
    plt.plot(axis[i], ordinat[i], marker='o', color = "blue")
for i in range(len(int_data)):
    plt.annotate(get_key(i),(int_data[i][0], int_data[i][1]))

rute_axis = []
rute_ordinat = []
for i in range(len(rute)):
    rute_axis.append(int_data[dict[rute[i]]][0])
    rute_ordinat.append(int_data[dict[rute[i]]][1])
plt.plot(rute_axis, rute_ordinat, label = "shortest path", marker='o', color = "red")

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.legend()

plt.title('Map')
  
plt.show()
name = input()
plt.title(name)
plt.show()


