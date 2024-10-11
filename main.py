import os
import re

def process_file(input_file, output_file):
    # Define the regex pattern to match "$string": and replace with "string:"
    pattern = re.compile(r'"\$([a-zA-Z0-9_]+)":')

    def replace_pattern(match):
        return f'"{match.group(1)}":'

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'a', encoding='utf-8') as outfile:
        while True:
            chunk = infile.read(1024 * 1024)  # Read in 1MB chunks
            if not chunk:
                break  # End of file
            # Replace the pattern in the chunk
            chunk = pattern.sub(replace_pattern, chunk)
            # Write the processed chunk to the output file
            outfile.write(chunk)
        outfile.write("\n")  # Adding a newline between files

def merge_and_replace(start_index, end_index, prefix, suffix, directory, output_file):
    # Ensure the directory path ends with a separator
    if not directory.endswith(os.path.sep):
        directory += os.path.sep
    
    # Clear the output file before starting
    open(output_file, 'w', encoding='utf-8').close()

    for i in range(start_index, end_index + 1):
        # Format the filename with leading zeros
        filename = f"{directory}{prefix}_{i:06d}{suffix}"
        
        # Check if the file exists
        if os.path.exists(filename):
            try:
                # Process the file in chunks and append to the output file
                process_file(filename, output_file)
            except Exception as e:
                # Handle other exceptions
                print(f"Error processing file {filename}: {e}")
        else:
            print(f"Warning: File {filename} does not exist.")

# Specify the range of file indices, prefix, suffix, directory, and output file
start_index = 1          # Starting index
end_index = 20325      # Ending index (e.g., 020325)
prefix = 'domain'        # Prefix of the filenames
suffix = '.txt'              # Suffix (empty string in this case, adjust if needed)
directory = './split_files'  # Directory where the files are located
output_file = 'merged_file.json'

merge_and_replace(start_index, end_index, prefix, suffix, directory, output_file)
