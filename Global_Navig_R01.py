import pyvisgraph as vg
import numpy as np
import matplotlib.pyplot as plt

start = np.array([0.5,0.5])
goal = np.array([5.25,6])

start_point = vg.Point(start[0], start[1])
goal_point = vg.Point(goal[0], goal[1])

vertices = np.array([[[1,2],[3,2],[3,4],[1,4]],[[4,4],[6,4],[5,5]]])

vertices = np.asarray(vertices)

plt.plot(vertices)
plt.show

# Automate the creation of vg.Points for the obstacles

max_vertices = 0

for i in range(len(vertices)):
    if(len(vertices[i])>max_vertices):
        max_vertices = len(vertices[i])

polygons = [[0 for i in range(max_vertices+1)] for j in range(len(vertices))]

for i in range(len(vertices)):
    for j in range(len(vertices[i])):
        polygons[i][j] = vg.Point(vertices[i][j][0],vertices[i][j][1])
    polygons[i][(len(vertices[i])):(max_vertices+1)] = [polygons[i][0] for k in range(len(vertices[i]),max_vertices+1)]
    #polygons[i][range(len(vertices[i]),max_vertices)] = polygons[i][0]

graph = vg.VisGraph()
graph.build(polygons)
#graph.buffer(margin,join_style=2)

shortest_path = graph.shortest_path(start_point,goal_point)

print(shortest_path)

polygons_x = np.empty((len(polygons),len(polygons[1])+1))
polygons_y = np.empty((len(polygons),len(polygons[1])+1))

for i in range(len(polygons)):
    for j in range(len(polygons[i])):
        polygons_x[i][j] = polygons[i][j].x
        polygons_y[i][j] = polygons[i][j].y
    polygons_x[i][len(polygons[1])] = polygons_x[i][0]
    polygons_y[i][len(polygons[1])] = polygons_y[i][0]

shortest_path_x = np.empty(len(shortest_path))
shortest_path_y = np.empty(len(shortest_path))

for i in range(len(shortest_path)):
    shortest_path_x[i] = shortest_path[i].x
    shortest_path_y[i] = shortest_path[i].y

plt.plot(shortest_path_x,shortest_path_y)
plt.plot(polygons_x.T,polygons_y.T)
plt.show()