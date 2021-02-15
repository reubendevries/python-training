data = [4,5,104,105,110,120,130,130,150,
        160,170,183,185,187,188,191,350,360]
min_valid = 100
max_valid = 200

# Process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) -1, -1, -1): 
    if data[index] <= max_valid:
        # we have the index of the last item to keep
        # set 'start' to the position of the first
        # item to delete, which is 1 after 'index'.
        start = index + 1
        break

del data[start:]
print(data)