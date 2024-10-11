import json

def validate_json_schema(line):
    try:
        data = json.loads(line)
        # Example: Check if "name" is a string and "age" is an integer
        if not isinstance(data.get('name'), str) or not isinstance(data.get('age'), int):
            return False
        return True
    except json.JSONDecodeError:
        return False

def validate_schema_large_json(filename):
    with open(filename, 'r', buffering=1024 * 1024) as file:  # Read in 1MB chunks
        valid = True
        for i, line in enumerate(file):
            if not validate_json_schema(line):
                print(f"Invalid schema detected at line {i + 1}")
                valid = False
        if valid:
            print("All lines conform to the schema.")
        else:
            print("Some lines do not conform to the schema.")

filename = './merged_file.json'
validate_schema_large_json(filename)
