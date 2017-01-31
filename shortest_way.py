from heapq import *

# from city import city
# from city_old import city

from city import city

def shortest_way(city, start_id, dest_id, mode, crimes_pieces, crimes):
    visited = set()
    if mode <= 1:
        heap = [(0, 0, start_id, ())]
    else:
        heap = [(0, 0, start_id, (), set())]
    while heap:
        if mode == 0:
            temp_distance, temp_crime, temp_node, temp_path = heappop(heap)
        if mode == 1:
            temp_crime, temp_distance, temp_node, temp_path = heappop(heap)
        if mode == 2:
            temp_crime, temp_distance, temp_node, temp_path, temp_visited_streets = heappop(heap)
        if temp_node not in visited:
            visited.add(temp_node)
            temp_path = (temp_node, temp_path)
            if temp_node == dest_id:
                list_path = []
                try:
                    while True:
                        list_path.append(temp_path[0])
                        temp_path = temp_path[1]
                except:
                    return(list_path, temp_crime)
            for item in city[temp_node]:
                if item[0] not in visited:
                    if mode == 0:
                        heappush(heap, (temp_distance + item[1], temp_crime + crimes_pieces.get((temp_node, item[0]), 0), item[0], temp_path))
                    if mode == 1:
                        heappush(heap, (temp_crime + crimes_pieces.get((temp_node, item[0]), 0), temp_distance + item[1], item[0], temp_path))
                    if mode == 2:
                        new_crime = temp_crime
                        if item[2] not in temp_visited_streets:
                            temp_visited_streets.add(item[2])
                            new_crime += crimes.get(item[2], 0)
                        heappush(heap, (new_crime, temp_distance + item[1], item[0], temp_path, temp_visited_streets))
    return None
