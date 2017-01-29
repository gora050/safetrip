# city - dict{ (latitude, longitude): [((neighbour_latitude, neighbour_longitude), length, street_id)]}


def shortest_way(city, start_id, dest_id, check_crimes, crimes_data):
    temp = [start_id] # queue
    data = {}
    for key in city:
        data[key] = [10**9, None, False]
        """
            data - dictionary
            key - node_id
            value - [shortest_way, from_which_node_we_came, did_we_visit_this_node]
        """
    data[start_id] = [0, None, False]
    while len(temp) >= 1:
        if data[temp[0]][0] < data[dest_id][0]:
            for item in city[temp[0]]:
                if not data[item[0]][2]:
                    if data[temp[0]][0] + item[1] < data[item[0]][0]:
                        data[item[0]][0] = data[temp[0]][0] + item[1]
                        data[item[0]][1] = temp[0]
                    if (not (item[0] in temp)) and (not(data[item[0]][2])) and not(item[0] == dest_id):
                        temp.append(item[0])
        data[temp[0]][-1] = True
        del(temp[0])
    result = []

    crimes_made = 0

    while dest_id != start_id:
        node_from = dest_id
        node_to = data[dest_id][1]
        result.append([dest_id[0], dest_id[1]])
        dest_id = data[dest_id][1]
    result.append([start_id[0], start_id[1]])
    return result, crimes_made

import time
from city_old import city

start = time.time()

shortest_way(city, (50.022264437932165, 23.97523177005885), (49.83574035405036, 23.978264091169933), False, {})

print('not updated', time.time() - start)
