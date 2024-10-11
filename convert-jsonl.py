import ijson
import json

def convert_json_array_to_jsonl(input_file_path, output_file_path):
    """
    Converts a large JSON array file to JSON Lines format using streaming.
    """
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w') as outfile:
        # Use ijson to stream through the JSON array
        parser = ijson.items(infile, 'item')
        
        for item in parser:
            outfile.write(json.dumps(item) + '\n')

# Specify the paths to your input and output files
input_file = 'full_indexer_domain.json'  # Path to your large JSON array file
output_file = 'full_indexer_domain.jsonl'    # Path where the JSON Lines file will be saved

# Perform the conversion
convert_json_array_to_jsonl(input_file, output_file)
