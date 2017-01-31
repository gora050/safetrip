# city - dict{ (latitude, longitude): [((neighbour_latitude, neighbour_longitude), length, street_id, crimes_num)]}




def shortest_way(city, start_id, dest_id, check_crimes, crimes_data):
    temp = [start_id] # queue
    data = {}
    for key in city:
        if check_crimes:
            data[key] = [10**9, [], 10**9, None, False]
            """
                data - dictionary
                key - node_id
                value - [min_crimes_num, street_set, shortest_way, from_which_node_we_came, did_we_visit_this_node]
            """
        else:
            data[key] = [10**9, None, False]
            """
                data - dictionary
                key - node_id
                value - [shortest_way, from_which_node_we_came, did_we_visit_this_node]
            """
    if check_crimes:
        data[start_id] = [0, [], 0, None, False]
        while len(temp) >= 1:
            if data[temp[0]][0] <= data[dest_id][0]:
                for item in city[temp[0]]:
                    if not data[item[0]][4]:
                        if item[2] in data[temp[0]][1]:
                            if data[temp[0]][0] < data[item[0]][0] or (data[temp[0]][0] == data[item[0]][0] and data[temp[0]][2] + item[1] < data[item[0]][2]): # перевірити crimes number
                                data[item[0]][0] = data[temp[0]][0]
                                data[item[0]][1] = data[temp[0]][1].copy()
                                data[item[0]][2] = data[temp[0]][2] + item[1]
                                data[item[0]][3] = temp[0]
                                if (not (item[0] in temp)) and (not(data[item[0]][4])) and not(item[0] == dest_id):
                                    temp.append(item[0])
                        else:
                            try:
                                current_crime = crimes_data[item[2]]
                            except:
                                current_crime = 0
                            if data[temp[0]][0] + current_crime < data[item[0]][0] or (data[temp[0]][0] + current_crime == data[item[0]][0] and data[temp[0]][2] + item[1] < data[item[0]][2]):
                                data[item[0]][0] = data[temp[0]][0] + current_crime
                                data[item[0]][1] = data[temp[0]][1].copy()
                                data[item[0]][1].append(item[2])
                                data[item[0]][2] = data[temp[0]][2] + item[1]
                                data[item[0]][3] = temp[0]
                                if (not (item[0] in temp)) and (not(data[item[0]][4])) and not(item[0] == dest_id):
                                    temp.append(item[0])
            data[temp[0]][-1] = True
            del(temp[0])
    else:
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
    visited_streets = set()

    while dest_id != start_id:
        node_from = dest_id
        if check_crimes:
            node_to = data[dest_id][3]
        else:
            node_to = data[dest_id][1]
        for neighbour in city[node_from]:
            if neighbour[0] == node_to:
                visited_streets.add(neighbour[2])
        result.append([dest_id[0], dest_id[1]])
        if check_crimes:
            dest_id = data[dest_id][3]
        else:
            dest_id = data[dest_id][1]
    result.append([start_id[0], start_id[1]])
    for item in visited_streets:
        try:
            crimes_made += crimes_data[item]
        except:
            pass
    return result, crimes_made
