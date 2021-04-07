# import Main as main

def Euclidean(x1, x2, y1, y2):
    hasil = ((y2-y1)**2 + (x2-x1)**2)**(0.5)
    hasil = float("{:.2f}".format(hasil))
    # hasil = int(hasil)
    # print(type(hasil))
    return(hasil)


def display_mat(matriks,n_row,n_col):
    for i in range(n_row):
        for j in range(n_col):
            print(matriks[i][j], end="\t")
        print()


def min_arr(arr_total): # return node yg minimal total dr gn + hn nya
    min = arr_total[0][0]
    idx_min = 0
    for i in range(1,len(arr_total)):
        if (arr_total[i][0] < min):
            min = arr_total[i][0]
            idx_min = i
    return idx_min

def copy_arr(arr):
    neo = []
    for i in range(len(arr)):
        neo.append(arr[i])
    return neo