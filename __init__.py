from flask import Flask, request, session, render_template
from math import radians, sqrt, sin, cos, atan2
import json

import math
from shortest_way import shortest_way
from crimes import crimes
from crimes_pieces import crimes_pieces
from lviv_ukraine_roads import roads_data

app = Flask(__name__)

def break_line(lat1, lng1, get_id):
    last_part = -1
    min_d = [10**50, 0,0]
    for part in roads_data["features"][int(get_id)]["coordinates"]:
        if last_part == -1:
            last_part = part
            continue
        a = (last_part[1] - part[1])/(last_part[0] - part[0]+0.0000001)
        b = part[1] - a*part[0]
        bh = lat1 + 1/a * lng1
        x = (bh-b)/(a+1/a)
        if max([x,part[0],last_part[0]]) == x or  min([x,part[0],last_part[0]]) == x:
            last_part = part
            continue
        d = abs(-a*lng1 + lat1 - b)/math.sqrt(a**2 + 1)
        if min_d[0] > d:
            min_d = [d, part, last_part]
        last_part = part
    return [min_d[1],[lng1, lat1], min_d[2]]

def geocalc(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon1 - lon2

    EARTH_R = 6372.8

    y = sqrt(
        (cos(lat2) * sin(dlon)) ** 2
        + (cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)) ** 2
        )
    x = sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(dlon)
    c = atan2(y, x)
    return EARTH_R * c

def my_reversed(lst):
    return (lst[1], lst[0])

@app.route('/map')
def build_way():
    import city
    # id1 id2 lat1 lng1 lat2 lng2
    # request.args["id1"]
    lat1 = float(request.args["lat1"])
    lat2 = float(request.args["lat2"])
    lng1 = float(request.args["lng1"])
    lng2 = float(request.args["lng2"])
    get_id = request.args["id1"]
    print(lat2, lng2, request.args["id2"])
    lst2 = break_line(lat2, lng2, request.args["id2"])
    print(lst2)
    print("_________________________")
    lst1 = break_line(lat1, lng1, get_id)
    #print("\n\n",lst1,"\n\n",lst2,"\n\n")
    try:
        city.city[(lat1,lng1)].append((my_reversed(lst1[0]),  geocalc(lat1,lng1,lst1[0][0],lst1[0][1])/2 ,request.args["id1"]))
        city.city[(lat1,lng1)].append((my_reversed(lst1[2]), geocalc(lat1,lng1,lst1[2][0],lst1[2][1])/2,request.args["id1"]))
    except:
        city.city[(lat1,lng1)] = [(my_reversed(lst1[0]),  geocalc(lat1,lng1,lst1[0][0],lst1[0][1])/2 ,request.args["id1"]),
                                  (my_reversed(lst1[2]), geocalc(lat1,lng1,lst1[2][0],lst1[2][1])/2,request.args["id1"])]

    try:
        city.city[(lat2,lng2)].append((my_reversed(lst2[0]), geocalc(lat2,lng2,lst2[0][0],lst2[0][1])/2 , request.args["id2"]))
        city.city[(lat2,lng2)].append((my_reversed(lst2[2]), geocalc(lat2,lng2,lst2[2][0],lst2[2][1])/2 , request.args["id2"]))
    except:
        city.city[(lat2,lng2)] = [(my_reversed(lst2[0]), geocalc(lat2,lng2,lst2[0][0],lst2[0][1])/2 , request.args["id2"]),
                                  (my_reversed(lst2[2]), geocalc(lat2,lng2,lst2[2][0],lst2[2][1])/2 , request.args["id2"])]

    city.city[tuple(my_reversed(lst1[0]))].append((tuple(my_reversed(lst1[1])), geocalc(lat1,lng1,lst1[0][0],lst1[0][1])/2 , request.args["id1"]))
    city.city[tuple(my_reversed(lst1[2]))].append((tuple(my_reversed(lst1[1])), geocalc(lat1,lng1,lst1[2][0],lst1[2][1])/2 , request.args["id1"]))
    print(lst2)
    city.city[tuple(my_reversed(lst2[0]))].append((tuple(my_reversed(lst2[1])), geocalc(lat2,lng2,lst2[0][0],lst2[0][1])/2 , request.args["id2"]))
    city.city[tuple(my_reversed(lst2[2]))].append((tuple(my_reversed(lst2[1])), geocalc(lat2,lng2,lst2[2][0],lst2[2][1])/2 , request.args["id2"]))

    shortest = shortest_way(city.city, (lat1, lng1), (lat2, lng2), 0, crimes_pieces, crimes)
    safest = shortest_way(city.city, (lat1, lng1), (lat2, lng2), 1, crimes_pieces, crimes)
    optimal = shortest_way(city.city, (lat1, lng1), (lat2, lng2), 2, crimes_pieces, crimes)

    # res = shortest_way(city.city, (lat1, lng1), (lat2, lng2), 1, crimes_pieces, crimes)
    # res1 = shortest_way(city.city, (lat1, lng1), (lat2, lng2), 0, crimes_pieces, crimes)

    return json.dumps([safest, shortest, optimal])
    #return(shortest_way(city.city, (lat1, lng1), (lat2, lng2)))
    #return json.dumps(roads_data["features"][int(request.args["id1"])]["coordinates"])


    #return "<br>".join(dir(request))
@app.route('/')
def index():
    crimed_roads = {}
    maxcrime = -1
    for road in crimes:
        try:
            crimed_roads[road] = [roads_data["features"][road]["coordinates"], crimes[road]]
            maxcrime = max(maxcrime, crimes[road])
        except KeyError:
            pass
    return render_template('index.html', crime = crimed_roads, maxcrime = maxcrime)

if __name__ == "__main__":
    app.run(debug=True)
