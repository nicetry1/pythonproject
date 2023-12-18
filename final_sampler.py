import random
import ujson

def generate_random_sample(input_file, output_file, sample_size):
  
    with open(input_file,'r') as input_stream:
        total_length = sum(1 for _ in input_stream)
        input_stream.seek(0)
        random_index = random.sample(range(total_length), sample_size)
        
        print(f"The numbers have been generated")

        with open(output_file, 'w') as output_stream:
            with open(input_file, 'r') as input_stream:
                for line_number, line in enumerate(input_stream):
                    if line_number in random_index:
                        random_lines = ujson.loads(line)["metadata"]
                        #write sample to output file
                        output_stream.write(ujson.dumps(random_lines) + '\n')
        
                        if line_number % 100 == 0:
                            print(f"Processed {line_number} lines.")

if __name__ == '__main__':
    #define filepaths, sample size
    input_file_path = '/Volumes/LaCie/2023 python datasets/title_json.jsonl'
    output_file_path = '/Users/nicetry/Documents/GitHub/nextapp/pythonproject/data/randomtest_title.jsonl'
    sample_size = 1000

#start function
generate_random_sample(input_file_path, output_file_path, sample_size)