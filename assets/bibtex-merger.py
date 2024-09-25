import os
import re
from typing import List, Tuple

def parse_bibtex_file(file_path: str) -> List[Tuple[str, str]]:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    entries = re.findall(r'(@\w+\{[^@]+\})', content, re.DOTALL)
    parsed_entries = []
    
    for entry in entries:
        key_match = re.search(r'@\w+\{(\w+),', entry)
        if key_match:
            key = key_match.group(1)
            parsed_entries.append((key.lower(), entry))
    
    return parsed_entries

def merge_bibtex_files(directory: str, output_file: str):
    all_entries = []
    
    for filename in os.listdir(directory):
        if filename.endswith('.bib'):
            file_path = os.path.join(directory, filename)
            all_entries.extend(parse_bibtex_file(file_path))
    
    # Sort entries based on the lowercase key
    all_entries.sort(key=lambda x: x[0])
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for _, entry in all_entries:
            outfile.write(entry + '\n\n')

if __name__ == "__main__":
    import sys
    
    #if len(sys.argv) != 3:
    #    print("Usage: python script.py <input_directory> <output_file>")
    #    sys.exit(1)
    
    #input_directory = sys.argv[1]
    #output_file = sys.argv[2] 
    input_directory = "./jike"
    output_file = "references.bib"
    
    merge_bibtex_files(input_directory, output_file)
    print(f"Merged BibTeX entries have been written to {output_file}")
