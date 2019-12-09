from iomanager import read_file

cities = read_file("data_tsp.txt")
for c in cities:
    c.print_city()
