import random
import ujson

def generate_random_sample(input_file, output_file, sample_size):
    with open(input_file,'r') as input_stream:
        #read all lines from input -- maybe this is causing the problem w processing the very large files
        all_lines = [ujson.loads(line)["metadata"] for line in input_stream]

        #sample lines
        random_sample = random.sample(all_lines, min(sample_size, len(all_lines)))

        with open(output_file, 'w') as output_stream:
            for i, item in enumerate(random_sample, start=1):
                #write sample to output file
                output_stream.write(ujson.dumps(item, ensure_ascii=False) + '\n')
                #print progress message every 100 lines processed
                #if i % 100 == 0:
                    #print(f'processed {i} lines out of {len(random_sample)}')

if __name__ == '__main__':
    #define filepaths and sample size
    input_file_path = '/Volumes/LaCie/2023 python datasets/briefrecords_json.jsonl'
    output_file_path = '/Users/nicetry/Documents/GitHub/nextapp/pythonproject/data/randomtest_briefrecords.jsonl'
    sample_size = 10

#call function
generate_random_sample(input_file_path, output_file_path, sample_size)