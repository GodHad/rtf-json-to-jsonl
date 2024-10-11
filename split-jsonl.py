def split_large_jsonl_file(input_file, n):
    total_lines = 0

    # First, count the total number of lines
    with open(input_file, 'r', encoding='utf-8') as infile:
        for _ in infile:
            total_lines += 1

    # Calculate the number of lines per split
    lines_per_file = total_lines // n
    extra_lines = total_lines % n  # Any remaining lines that don't divide evenly
    print(f"Total lines: {total_lines}")
    # Open the input file and split into n output files
    with open(input_file, 'r', encoding='utf-8') as infile:
        for i in range(n):
            output_file = f'part_{i+1}.jsonl'  # Create output file name dynamically
            with open(output_file, 'w', encoding='utf-8') as outfile:
                # Determine how many lines to write to this file
                lines_to_write = lines_per_file + (1 if i < extra_lines else 0)
                
                for _ in range(lines_to_write):
                    line = infile.readline()
                    if line:
                        outfile.write(line)
                    else:
                        break

    print(f"File successfully split into {n} parts.")

# Usage example
input_file = 'part2-1.jsonl'  # Your input file
n = 3  # Split the file into 5 parts
split_large_jsonl_file(input_file, n)
