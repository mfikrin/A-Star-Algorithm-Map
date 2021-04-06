# importing the required module
import matplotlib.pyplot as plt
import Main as main
  
# x axis values
x1 = [5,4,1,7,3,4,6,7,5]
# corresponding y axis values
y1 = [2,1,5,6,9,2,7,9,2]
# A 5,2
for i in range(len(int_data)):
    plt.annotate(main.get_key(i),(int_data[i][0], int_data[i][1]))
# plt.annotate("A", (5, 2))
# # B 4,1
# plt.annotate("B", (4, 1))
# # C 7,9
# plt.annotate("C", (7, 9))
# # D 1,5
# plt.annotate("D", (1, 5))
# # E 3,9
# plt.annotate("E", (3, 9))
# # F 6,7
# plt.annotate("F", (6, 7))
# # G 4,2
# plt.annotate("G", (4, 2))
# # H 7,6
# plt.annotate("H", (7, 6))
# A B
# A C
# B D
# C F
# D H
# E G
# E H
# F G
# plotting the points 
plt.plot(x1, y1, label = "line 1", marker='o')


  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

plt.legend()
# giving a title to my graph
plt.title('My first graph!')
  
# function to show the plot
plt.show()








# import networkx as nx
# # import matplotlib as pyplot

# G = nx.complete_graph(5)
# nx.draw(G)

# B = [[0., 1., 1., 0., 0., 0., 0., 0.,],[1., 0., 0., 1., 0., 0., 0., 0.,],[1., 0., 0., 0., 0., 1., 0., 0.,],[0., 1., 0., 0., 0., 0., 0., 1.,],[0., 0., 0., 0., 0., 0., 1., 1.,],[0., 0., 1., 0., 0., 0., 1., 0.,],[0., 0., 0., 0., 1., 1., 0., 0.,],[0., 0., 0., 1., 1., 0., 0., 0.,]
