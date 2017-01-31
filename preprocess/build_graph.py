# input format - [[(latitude1, longitude1), (latitude1, longitude1), length]]
# output in a file city.py
# estimated format - dict{ (latitude, longitude): [((neighbour_latitude, neighbour_longitude), length)]

from lviv_ukraine_roads_data import roads_data

def perform_graph(data):
    graph = {}
    for edge in data:
        if edge[0] in graph:
            graph[edge[0]].append((edge[1], edge[2], edge[3]))
        else:
            graph[edge[0]] = [(edge[1], edge[2], edge[3])]
        if edge[1] in graph:
            graph[edge[1]].append((edge[0], edge[2], edge[3]))
        else:
            graph[edge[1]] = [(edge[0], edge[2], edge[3])]
    destination_file = open('city.py', 'w')
    destination_file.write("city = {\n")
    for item in graph:
        destination_file.write(str(item) + ":" + str(graph[item]) + ",\n")
    destination_file.write("}")
    destination_file.close()

perform_graph(roads_data)
