from heapq import *

# from city import city
# from city_old import city

from city import city

def shortest_way(city, start_id, dest_id, check_crimes):
    heap, visited = [(0, 0, start_id, ())], set()
    while heap:
        if not check_crimes:
            temp_distance, temp_crime, temp_node, temp_path = heappop(heap)
        else:
            temp_crime, temp_distance, temp_node, temp_path = heappop(heap)
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
                    if not check_crimes:
                        heappush(heap, (temp_distance + item[1], temp_crime + item[2], item[0], temp_path))
                    else:
                        heappush(heap, (temp_crime + item[2], temp_distance + item[1], item[0], temp_path))
    return None
if __name__ == "__main__":
    import time
    start = time.time()
    result1 = shortest_way(city, (49.877482567130585, 23.94072154685577), (49.87968298435169, 24.01564545148608), False)
    result2 = shortest_way(city, (49.877482567130585, 23.94072154685577), (49.87968298435169, 24.01564545148608), True)
    end = time.time()
    # print(result1[0])
    print("shortest")
    print('crime num', result1[1])
    print('length', result1[2])
    print()
    print()
    print()
    print("safest")
    # print(result2[0])
    print('crime num', result2[1])
    print('length', result2[2])
    print("TIME :", end - start)
