import os
import subprocess
import glob

def convert_bibtex_to_yaml(bibtex_file):
    # Derive the output file name by replacing the .bib extension with .yaml
    yaml_file = os.path.splitext(bibtex_file)[0] + '.yaml'
    
    # Construct the Pandoc command
    pandoc_command = [
        'pandoc',
        bibtex_file,
        '-s', 
        '-f', 'biblatex', 
        '-t', 'markdown',
        '-o', yaml_file
    ]
    
    # Execute the command using subprocess
    subprocess.run(pandoc_command, check=True)
    
    print(f"Converted {bibtex_file} to {yaml_file}")

def process_bibtex_files(directory):
    # Find all .bib files in the specified directory
    bibtex_files = glob.glob(os.path.join(directory, '*.bib'))
    
    # Iterate over each .bib file and convert it to a .yaml file
    for bibtex_file in bibtex_files:
        convert_bibtex_to_yaml(bibtex_file)

def main():
    # Specify the directory containing the .bib files
    directory = './bibtex'  # Replace with your directory
    
    # Process all .bib files in the directory
    process_bibtex_files(directory)

if __name__ == "__main__":
    main()
