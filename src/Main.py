import os
import matplotlib.pyplot as plt
import graph as gr
import util as ut

print("-----------------------------")
print("|  Silahkan input nama file |")
print("|        (eg : tc1)         |")
print("|   (Tanpa ekstensi file)   |")
print("-----------------------------")

print()

filename1 = input("Input nama file koordinat (format : *_1.txt) (eg : tc1_1) : ")
test = "../test/"
path1 = test + filename1 + ".txt"
isfile1 = os.path.isfile(path1)

# Melakukan pengecekan apakah filename terdapat pada folder test atau tidak
while (not isfile1):
    filename1 = input("Ulangi input nama file koordinat (format : *_1.txt) (eg : tc1_1) : ")
    path1 = test + filename1 + ".txt"
    isfile1 = os.path.isfile(path1)

filename2 = input("Input nama file Matriks adjacency (format : *_2.txt) (eg : tc1_2) : ")
path2 = test + filename2 + ".txt"
isfile2 = os.path.isfile(path2)

while (not isfile2):
    filename2 = input("Ulangi input nama file 2 Matriks adjacency (format : *_2.txt) (eg : tc1_2) : ")
    path2 = test + filename2 + ".txt"
    isfile2 = os.path.isfile(path2)

file_data = open(path1, "r")
file_edge = open(path2, "r")

data = file_data.read().splitlines() # baca file teks (dengan readlines yang sekaligus hapus \n)
edge = file_edge.read().splitlines()

n_node = int(data[0])
data.remove(data[0])
int_data = [[0 for j in range(2)] for i in range(len(data))]

arr_node = []
for i in range(len(data)):

    # print("NODE")
    # print(node)
    idx_titik_dua = data[i].index(':')
    node = data[i][:(idx_titik_dua)]
    # print("idx" +str(idx_titik_dua))
    arr_node.append(node)
    string = data[i][idx_titik_dua + 1:len(data[i])]
    x = string.split(",")
    # print(x[0][0])
    # if (x[0][0] == "-"):
    if (x[0][0] == "-"):
        int_data[i][0] = -(float(x[0][1:]))
    else:
        int_data[i][0] = float(x[0])
    # int_data[i][0] = int(x[0])

    if (x[1][0] == "-"):
        int_data[i][1] = -(float(x[1][1:]))
    else:
        int_data[i][1] = float(x[1])

dict = {}
idx = 0
for node in arr_node:
    dict[node] = idx
    idx+= 1

mat_edge = [[0 for j in range(n_node)] for i in range(n_node)]

baris = 0
kolom = 0
for i in range(len(edge)):
    for j in range(len(edge[i])):
        if j % 2 == 0:
            mat_edge[baris][kolom] = int(edge[i][j])
            kolom += 1
    baris += 1
    kolom = 0

g = gr.Graf(n_node)

print("-----------------------------")
print("|   Silahkan input opsi     |")
print("|   1. Koordinat Peta       |")
print("|   2. Koordinat Kartesian  |")
print("-----------------------------")

pil = int(input("Input opsi koordinat : "))

while (pil != 1 and pil != 2):
    pil = int(input("Ulangi input pilihan, pastikan pilihan 1 atau 2 : "))
if pil == 2:
    # Membuat matriks koordinat node
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            m = int_data[i]
            n = int_data[j]

            x1 = m[0]
            y1 = m[1]
            x2 = n[0]
            y2 = n[1]
            jarak = ut.Euclidean(x1,x2,y1,y2)
            g.add_element(i,j,jarak)
            g.add_element(j,i,jarak)
            g.add_element(i,i,0)
else:
    # Membuat matriks koordinat node
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            m = int_data[i]
            n = int_data[j]

            x_lat1 = m[0]
            y_lon1 = m[1]
            x_lat2 = n[0]
            y_lon2 = n[1]
            jarak = ut.Haversine(x_lat1, x_lat2, y_lon2, y_lon2)
            g.add_element(i, j, jarak)
            g.add_element(j, i, jarak)
            g.add_element(i, i, 0)

# print("MATRKS")
# ut.display_mat(g.matrix,n_node,n_node)

mat_mix = [[0 for j in range(n_node)] for i in range(n_node)]


for i in range(n_node):
    for j in range(n_node):
        if mat_edge[i][j] == 1:
            mat_mix[i][j] = g.matrix[i][j]

def get_key(val):
    for node,value in dict.items():
         if val == value:
             return node


def calculate_gn(rute,nodeN):
    gn = 0
    for i in range(len(rute)):
        if (i != len(rute) - 1):
            gn += mat_mix[dict[rute[i]]][dict[rute[i+1]]]
        else:
            gn += mat_mix[dict[rute[i]]][dict[nodeN]]
    return gn



arr = [] # Untuk menyimpan fn setiap kemungkinan searching
rute = [] # Menyimpan rute

def is_have_edge(node):
    int_node = dict[node]
    count = 0
    for i in range(len(mat_edge[int_node])):
        if (mat_edge[int_node][i] == 1):
            count += 1
    return count

# is_have_edge("H")

def Get_Short_Path(nodeAwal,nodeAkhir):
    iterasi = 0
    if (nodeAwal == nodeAkhir):
        print("Anda Sudah di sana :) ")
    else:
        if (is_have_edge(nodeAkhir) > 0): # Jika node akhir dapat dicapai
            a_star(nodeAwal,nodeAkhir,iterasi)
        else:
            print("Lokasi Tujuan tidak bisa dicapai")

def a_star(nodeAwal, nodeAkhir,iterasi):
    iterasi += 1
    rute.append(nodeAwal)
    if (is_have_edge(nodeAwal) == 1 and iterasi != 1):
        if (len(arr) == 0):
            print("Tidak bisa mencapai lokasi tujuan")
            rute.append("NO")
        else:
            for i in range(len(mat_mix[dict[nodeAwal]])):
                if mat_mix[dict[nodeAwal]][i] != 0:

                    nodeN = get_key(i)

                    gn = calculate_gn(rute,nodeN)
                    # print(gn)
                    hn = g.matrix[i][dict[nodeAkhir]]
                    # print(hn)
                    total = gn + hn
                    # print(total)
                    rute.append(get_key(i))
                    copy_rute = ut.copy_arr(rute)
                    arr_total = [total,copy_rute]
                    arr.append(arr_total)
                    del rute[len(rute)-1:len(rute)]

            if (len(arr) != 0):
                idx_min = ut.min_arr(arr)
                temp = arr[idx_min]
                del arr[idx_min:idx_min + 1]
                node = temp[1][len(temp[1])-1]
                if (node == nodeAkhir):
                    print("Rute Terpendek : ")
                    jarak = calculate_gn(rute,node)
                    rute.append(node)
                    print("Rute : ", end=" ")
                    # print(rute)
                    ut.display_array(rute)
                    rute.append("YES")
                    print("Iterasi : " + str(iterasi))
                    print("Jarak : " + str(jarak))

                else:
                    rute.clear() # Clear Rute

                    for i in range(len(temp[1])):
                        rute.append(temp[1][i]) # Isi Kembali Rute

                    del rute[len(rute)-1:len(rute)]

                    # recursive
                    a_star(get_key(dict[temp[1][len(temp[1])-1]]),nodeAkhir,iterasi)
            else: # klw node awal ga punya tetangga
                print("Tidak ada rute yang dapat dilalui")
                rute.append("NO")
            # else:
            #     print("Tidak bisa mencapai lokasi tujuan Anda")
    else:
        for i in range(len(mat_mix[dict[nodeAwal]])):
            if mat_mix[dict[nodeAwal]][i] != 0:
                nodeN = get_key(i)

                gn = calculate_gn(rute, nodeN)
                # print(gn)
                hn = g.matrix[i][dict[nodeAkhir]]
                # print(hn)
                total = gn + hn
                # print(total)
                rute.append(get_key(i))
                copy_rute = ut.copy_arr(rute)
                arr_total = [total, copy_rute]
                arr.append(arr_total)
                del rute[len(rute) - 1:len(rute)]

        if (len(arr) != 0):
            idx_min = ut.min_arr(arr)
            temp = arr[idx_min]
            # print("ARR")
            # print(arr)
            # print("TEMP")
            # print(temp)
            del arr[idx_min:idx_min + 1]
            node = temp[1][len(temp[1]) - 1]
            # print(node)
            if (node == nodeAkhir):
                print("Rute Terpendek : ")
                jarak = calculate_gn(rute, node)
                rute.append(node)
                print("rute : ", end=" ")
                # print(rute)
                ut.display_array(rute)
                rute.append("YES")
                print("Iterasi : " + str(iterasi))
                print("Jarak : " + str(jarak))

            else:
                rute.clear()  # Clear Rute

                for i in range(len(temp[1])):
                    rute.append(temp[1][i])  # Isi Kembali Rute
                # print("RITEEE")
                # print(rute)
                del rute[len(rute) - 1:len(rute)]
                # print("AFTER DELETE")
                # print(rute)

                # recursive
                a_star(get_key(dict[temp[1][len(temp[1]) - 1]]), nodeAkhir, iterasi)
        else: # klw node awal ga punya tetangga
            print("Tidak ada rute yang dapat dilalui")
            rute.append("NO")
        # else:
        #     print("Tidak bisa mencapai lokasi tujuan Anda")


axis = []
ordinat = []
for i in range(n_node):
    for j in range(n_node):
        if mat_edge[i][j] == 1:
            varx = [int_data[i][0], int_data[j][0]]
            vary = [int_data[i][1], int_data[j][1]]
            axis.append(varx)
            ordinat.append(vary)

# Menampilkan peta awal
for i in range(len(axis)):
    plt.plot(axis[i], ordinat[i], marker='o', color="blue")
for i in range(len(int_data)):
    plt.annotate(get_key(i), (int_data[i][0], int_data[i][1]))

plt.xlabel('x - axis')
plt.ylabel('y - axis')

# plt.legend()
plt.title("Map")
plt.show()

def is_in_dict(nodeInput):
    for node in dict.keys():
        if nodeInput == node:
            return True
    return False

print("List Daerah : ")
for i in range(len(arr_node)):
    print(str(i+1) + ". "+arr_node[i])

print("-----------------------------")
print("|   Dari mana mau ke mana   |")
print("|           ???             |")
print("-----------------------------")




nodeAwal = input("Input asal (Node Awal) : ")
while(not is_in_dict(nodeAwal)):
    nodeAwal = input("Ulangi input asal (Node Awal) : ")
nodeAkhir = input("Input tujuan (Node Akhir) : ")
while(not is_in_dict(nodeAkhir)):
    nodeAkhir = input("Ulangi input tujuan (Node Akhir) : ")

Get_Short_Path(nodeAwal,nodeAkhir)

# Menampilkan peta awal
for i in range(len(axis)):
    plt.plot(axis[i], ordinat[i], marker='o', color="blue")
for i in range(len(int_data)):
    plt.annotate(get_key(i), (int_data[i][0], int_data[i][1]))

# rute_axis = []
# rute_ordinat = []
# for i in range(len(rute)-1):
#     rute_axis.append(int_data[dict[rute[i]]][0])
#     rute_ordinat.append(int_data[dict[rute[i]]][1])

rute_axis = []
rute_ordinat = []
for i in range(len(rute)-1):
    rute_axis.append(int_data[dict[rute[i]]][0])
    rute_ordinat.append(int_data[dict[rute[i]]][1])
if (rute[len(rute)-1] == "YES"): # Klw sampai ke node akhir / tujuan
    plt.plot(rute_axis, rute_ordinat, label="shortest path", marker='o', color="red")
    plt.legend()

plt.xlabel('x - axis')
plt.ylabel('y - axis')



plt.title('Map')

plt.show()





