# city - dict{ id: [(neighbour_id , length, street_id)]}


def heapify(tree, i, tree_len, index):
    while tree[i][0] > tree[2 * i + 1][0] or tree[i][0] > tree[2 * i + 2][0]:
        is_right_son = 2 * i + 2 <= tree_len - 1
        if not is_right_son:
            tree[i], tree[2 * i + 1] = tree[2 * i + 1], tree[i]
            index[tree[i][1] - 1], index[tree[2 * i + 1][1] - 1] = index[tree[2 * i + 1][1] - 1], index[tree[i][1] - 1]
            return None
        else:
            if tree[2 * i + 1][0] < tree[2 * i + 2][0]:
                tree[i], tree[2 * i + 1] = tree[2 * i + 1], tree[i] 
                index[tree[i][1] - 1], index[tree[2 * i + 1][1] - 1] = index[tree[2 * i + 1][1] - 1], index[tree[i][1] - 1]
                i = 2 * i + 1
            else:
                tree[i], tree[2 * i + 2] = tree[2 * i + 2], tree[i]
                index[tree[i][1] - 1], index[tree[2 * i + 2][1] - 1] = index[tree[2 * i + 2][1] - 1], index[tree[i][1] - 1]
                i = 2 * i + 2


def heapify_child(tree, i, tree_len, index):
    while int((i + i % 2 - 2) / 2) >= 0 and tree[i][0] < tree[int((i + i % 2 - 2) / 2)][0]:
        tree[i], tree[int((i + i % 2 - 2) / 2)] = tree[int((i + i % 2 - 2) / 2)], tree[i]
        index[tree[i][1] - 1], index[tree[int((i + i % 2 - 2) / 2)][1] - 1] = index[tree[int((i + i % 2 - 2) / 2)][1] - 1], index[tree[i][1] - 1]
        i = int((i + i % 2 - 2) / 2)


def shortest_way(city, start_id, dest_id, check_crimes, crimes_data):
    start_id = coords_to_id[start_id]
    dest_id = coords_to_id[dest_id]
    if check_crimes:
        return [(49.86038222737113, 24.02279563398824)[0], (49.86038222737113, 24.02279563398824)[1]]
    else:
        # tree of unvisited nodes and its id
        tree_len = len(id_to_coords)
        tree = [[150000, i + 1] for i in range(tree_len)]

        # indexes of all nodes in tree
        # you must write node_id - 1 to achieve index of node_id node
        index = list(range(tree_len))

        # from which node we came to a arbitrary node
        from_which_we_came = [0] * tree_len

        # changing data for start node
        from_which_we_came[start_id - 1] = None
        tree[start_id - 1][0] = 0
        index[tree[0][1] - 1], index[start_id - 1] = index[start_id - 1], index[tree[0][1] - 1]
        tree[0] , tree[start_id - 1] = tree[start_id - 1], tree[0]

        try:
            while tree[0] < tree[index[dest_id - 1]]:
                temp_distance = tree[0][0]
                temp_from_node = tree[0][1]
                index[tree[0][1] - 1] = None
                index[tree[-1][1] - 1] = 0
                tree[0], tree[-1] = tree[-1], tree[0]
                del(tree[-1])
                tree_len -= 1
                heapify(tree, 0, tree_len, index)
                for item in city[temp_from_node]:
                    destination = item[0]
                    length = item[1]
                    if not(index[destination - 1] is None):
                        if index[destination - 1] != 0:
                            if tree[index[destination - 1]][0] > temp_distance + length:
                                tree[index[destination - 1]][0] = temp_distance + length
                                from_which_we_came[destination - 1] = temp_from_node
                                heapify_child(tree, index[destination - 1], tree_len, index)
                        else:
                            if tree[index[destination - 1]][0] > temp_distance + length:
                                tree[index[destination - 1]][0] = temp_distance + length
                                from_which_we_came[destination - 1] = temp_from_node
        except:
            pass
        i = from_which_we_came[dest_id - 1]
        result = []
        while i != 0 and i is not None:
            result.append(id_to_coords[i])
            i = from_which_we_came[i - 1]
        return (result, 0)
        

import time

from city import city
from coords_to_id import coords_to_id
from id_to_coords import id_to_coords

start = time.time()
shortest_way(city, (50.022264437932165, 23.97523177005885), (49.83574035405036, 23.978264091169933), False, {})

print('updated', time.time() - start)
