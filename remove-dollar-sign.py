import json

input_file = 'full_indexer_domain.jsonl'  # Replace with your input file name
output_file = 'part2-1.jsonl'  # Replace with your desired output file name

def process_line(line):
    try:
        # Parse the JSON line into a Python dictionary
        data = json.loads(line)
        
        # Traverse the dictionary and replace keys
        def replace_keys(obj):
            if isinstance(obj, dict):
                new_obj = {}
                for key, value in obj.items():
                    # Remove $ from keys
                    new_key = key[1:] if key.startswith('$') else key
                    # Recursively process the value
                    new_obj[new_key] = replace_keys(value)
                return new_obj
            elif isinstance(obj, list):
                return [replace_keys(item) for item in obj]
            else:
                return obj
        
        processed_data = replace_keys(data)
        
        # Convert the dictionary back to a JSON string
        return json.dumps(processed_data)
    
    except json.JSONDecodeError:
        # Handle the case where the line is not a valid JSON
        print("Warning: Could not decode line. Skipping.")
        return None

# Open the input file and process it line by line
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        processed_line = process_line(line)
        if processed_line:
            outfile.write(processed_line + '\n')

print(f"Processing complete. Output written to {output_file}")
