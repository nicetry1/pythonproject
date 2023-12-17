import random
import json

def generate_random_sample(input_file, output_file, sample_size):
    with open(input_file, 'r') as input_stream, open(output_file, 'w') as output_stream:
       
        #initialize JSON decoder
        json_decoder = json.JSONDecoder()

        i = 0
        for line in input_stream: 
                #decode one at a time
                obj, pos = json_decoder.raw_decode(line)

                #sample the object
                if random.random() < sample_size / (i + 1): 
                        #write sample to output file
                        output_stream.write(json.dumps(obj, ensure_ascii=False)+ '\n')

                i += 1

                #print progress message 
                if i % 100 == 0:
                        print(f'processed {i} lines')

                #stop processing if the desired sample size is reached
                if i >= sample_size:
                        break
                
                if __name__ == '__main__':
                        #define filepaths and sample size
                        input_file_path = '/Volumes/LaCie/2023 python datasets/providersearchrequest_json.jsonl'
                        output_file_path = '/Users/nicetry/Documents/GitHub/nextapp/pythonproject/data/random_providersearch.jsonl'
                        sample_size = 100

                        #call function
                        generate_random_sample(input_file_path, output_file_path, sample_size)