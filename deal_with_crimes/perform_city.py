from city import city
from result import data
out = open("kokoko.py", "w")
out.write("city = {\n")
for key in city:
    out.write(str(key) + " : [")
    for item in city[key]:
        crimes = data.get((key, item[0]), 0)
        out.write("(" + str(item[0]) + "," + str(item[1]) + "," + str(crimes) + "),")
    out.write("],\n")
out.write("}")
out.close()
