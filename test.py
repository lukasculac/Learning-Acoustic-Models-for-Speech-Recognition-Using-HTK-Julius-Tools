import os
import subprocess

# Define paths to your files and directories
julius_bin = r"C:/Users/lukas/voxforge/bin/julius-4.6-win32bin/bin/julius.exe"
jconf_file = r"C:/Users/lukas/voxforge/acoustic_model/julius.jconf"
test_filelist = r"C:/Users/lukas/voxforge/acoustic_model/files_path.txt"
output_mlf = r"C:/Users/lukas/voxforge/acoustic_model/recognition_output.lab"
expected_mlf = r"C:/Users/lukas/voxforge/acoustic_model/words.mlf"
dict_file = r"C:/Users/lukas/voxforge/acoustic_model/dict_julius"
# Create a function to run Julius in batch mode
def run_julius():
    try:
        command = [julius_bin, "-C", jconf_file]
        print("Running command:", command)  # Debug: Print the command
        subprocess.run(command, check=True)
        print("Julius recognition completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Julius: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Create a function to evaluate the results using HResults
def evaluate_results():
    hresults_bin = "HResults"  # Make sure HResults is in your PATH or provide full path
    try:
        command = [hresults_bin, "-I", expected_mlf, dict_file, output_mlf]
        print("Running command:", command)  # Debug: Print the command
        subprocess.run(command, check=True)
        print("Evaluation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during evaluation: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main script execution
if __name__ == "__main__":
    # Run Julius in batch mode
    run_julius()
    
    # Evaluate the results
    evaluate_results()