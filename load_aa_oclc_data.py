import ujson
import sys

path_to_file = sys.argv[1]
counter = 0
all_fields = {}

with open(path_to_file, 'r') as aa_file:

    for line in aa_file:

        counter = counter + 1
        if counter % 1000 == 0:
            print(counter)
            print(all_fields)


        data = ujson.loads(line)
        for key in data['record']:
            if key not in all_fields:
                all_fields[key] = 0
            
            all_fields[key] = all_fields[key] + 1


        # print(data['metadata'])

