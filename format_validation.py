import json

def validate_json_line(line):
    try:
        json.loads(line)
        return True
    except json.JSONDecodeError:
        return False

def validate_large_json(filename):
    with open(filename, 'r', buffering=1024 * 1024) as file:  # Read in 1MB chunks
        valid = True
        for i, line in enumerate(file):
            if not validate_json_line(line):
                print(line)
                print(f"Invalid JSON detected at line {i + 1}")
                valid = False
        if valid:
            print("All lines are valid JSON.")
        else:
            print("Some lines are invalid JSON.")

filename = './merged_file.json'
validate_large_json(filename)
