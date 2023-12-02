import ujson

path_to_file = "/Users/nicetry/Documents/GitHub/nextapp/pythonproject/data/providersearchrequest_json.jsonl"
all_fields = {}

with open(path_to_file, 'r') as aa_file:
    for line in aa_file:
       
       data = usjon.loads(line)
       #print(data['metadata']['oclc_number'])
        for key in data['metadata']['record']:
          if key not in all_fields:
             all_fields[key] = 0
        break