import random
import json

def generate_random_sample(input_file, output_file, sample_size):
    with open(input_file,'r') as input_stream:
        #read all lines from input
        all_lines = [json.loads(line) for line in input_stream]

        #sample lines
        random_sample = random.sample(all_lines, min(sample_size), len(all_lines))

        with open(output_file, 'w') as output_stream:
            for item in random_sample:
                #write sample to output file
                output_stream.write(json.dumps(item, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    #define filepaths and sample size
    input_file_path = ''
    output_file_path = ''
    sample_size = 10000

#call function
generate_random_sample(input_file_path, output_file_path, sample_size)