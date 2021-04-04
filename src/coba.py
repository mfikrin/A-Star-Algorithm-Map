
data_file = open("./test/tc1_2.txt","r")
files = data_file.read().splitlines()
matrix = [["*" for j in range(8)] for i in range(8)]

baris = 0
kolom = 0
print(files)
for i in range(len(files)):
    # print(len(file[i]))
    # print(str(i) + "woi")
    for j in range(len(files[i])):
        # print(files[i][j])
        if j % 2 == 0:
            matrix[baris][kolom] = int(files[i][j])
            kolom += 1
    baris += 1
    kolom = 0

for i in range(8):
    for j in range(8):
        print(matrix[i][j], end=" ")
    print()




































# print("A")
# print(file)
# baris = 0
# i = 0
# kolom = 0
# for line in file:
#     if (i % 2 == 0):
#         for j in range(len(line[i])):
#             matrix[baris][kolom] = line[i][j]
#             kolom += 1
#         baris += 1
#     i += 1

# for n in file:
#     for x in n:
#         if x != " " or x != "\n":
#             matrix[baris][kolom] = x
#             kolom += 1
#     baris += 1




