import os

def list_files_in_directory(directory, output_file):
    with open(output_file, 'w') as scp_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                scp_file.write(file_path + '\n')

# Example usage:
directory = 'C:/Users/lukas/voxforge/acoustic_model/wav'
output_file = 'test.scp'
list_files_in_directory(directory, output_file)