from crimes import crimes
from lviv_ukraine_roads_data import roads_data

out = open("result.txt", 'w')
out.write("data = {\n")
for street_id in crimes:
    all_crimes = crimes[street_id]
    all_length = 0
    street_pieces = []
    for item in roads_data:
        if item[-1] == street_id:
            street_pieces.append(item)
            all_length += item[-2]
    for item in street_pieces:
        temp_crime = all_crimes * item[-2] / all_length
        out.write("(" + str(item[0]) + "," + str(item[1]) + ") : " + str(temp_crime) + ",\n")
        out.write("(" + str(item[1]) + "," + str(item[0]) + ") : " + str(temp_crime) + ",\n")
out.write("}")
out.close()
