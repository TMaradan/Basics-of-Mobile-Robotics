import pyvisgraph as vg
import numpy as np
import matplotlib.pyplot as plt

start = np.array([0.5,0.5])
goal = np.array([5.25,6])

polygon_1 = np.array([[1,1,5,5,2,2],[2,6,6,5,5,2]])
polygon_2 = np.array([[1,1,3,3,4,4],[1,2,2,4.5,4.5,1]])

# Find better way to add first point to each row of each polygon to close the obstacle

#for i in range(len(polygon_1)):
#    polygon_1[len(polygon_1[0])] = polygon_1[i][0]
#    polygon_2[len(polygon_2[0])] = polygon_2[i][0]

polygons_array = np.concatenate((polygon_1,polygon_2))

start_point = vg.Point(start[0], start[1])
goal_point = vg.Point(goal[0], goal[1])

# Automate the creation of vg.Points for the obstacles

#polygons = []

#for i in range(int(len(polygons_array)/2)):
#    for j in range(len(polygons_array[1])):
#        polygons.append(vg.Point(polygons_array[2*i][j],polygons_array[2*i][j]))

polygons = [[vg.Point(1.0,2.5), vg.Point(1.0,6.0), vg.Point(5.0,6.0), vg.Point(5.0,5.0), vg.Point(2.0,5.0), vg.Point(2.0,2.5), vg.Point(1.0,2.5)],
            [vg.Point(1.0,1.0), vg.Point(1.0,2.0), vg.Point(3.0,2.0), vg.Point(3.0,4.5), vg.Point(4.0,4.5), vg.Point(4.0,1.0), vg.Point(1.0,1.0)]]

graph = vg.VisGraph()
graph.build(polygons)

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