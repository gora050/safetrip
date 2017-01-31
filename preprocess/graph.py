from lviv_ukraine_roads import roads_data
from math import radians, sqrt, sin, cos, atan2

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

with open("lviv_ukraine_roads_data.py","w") as r_data:

    r_data.write("roads_data = [\n")
    for road in roads_data["features"]:
        last_coord = -1
        for part in roads_data["features"][road]["coordinates"]:
            if last_coord == -1:
                last_coord = part
                continue
            r_data.write("[("+str(last_coord[1])+","+
                         str(last_coord[0])+"),("+
                         str(part[1])+","+
                         str(part[0])+"),"+
                         str(geocalc(last_coord[1], last_coord[0],part[1],part[0]))+","+
                         str(road) +"],\n")
            last_coord = part
    r_data.write("]")
