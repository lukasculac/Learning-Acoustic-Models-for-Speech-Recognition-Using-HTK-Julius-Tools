def remove_last_sp_from_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Split the line into parts
            parts = line.split()
            
            # Check if the last part is 'sp'
            if parts and parts[-1] == 'sp':
                # Remove the last 'sp'
                parts = parts[:-1]
            
            # Join the parts back into a single line
            new_line = ' '.join(parts) + '\n'
            
            # Write the modified line to the output file
            outfile.write(new_line)

# Example usage
input_file = 'dict_julius'
output_file = 'julius_dict'
remove_last_sp_from_file(input_file, output_file)