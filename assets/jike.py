import os
import re
from pathlib import Path
from typing import List

def parse_bibtex_entries(bibtex_content: str) -> List[str]:
    """Parses a BibTeX file content and returns a list of individual BibTeX entries."""
    # Splitting entries using '@' symbol, but reattaching the '@' to each entry
    entries = bibtex_content.strip().split('@')[1:]
    entries = ['@' + entry.strip() for entry in entries]
    return entries

def extract_citekey(entry: str) -> str:
    """Extracts the cite key from a single BibTeX entry."""
    match = re.search(r'@.*?\{(.*?),', entry)
    if match:
        return match.group(1)
    else:
        raise ValueError("Cite key not found in entry.")

def save_bibtex_entry(entry: str, directory: str) -> None:
    """Saves a single BibTeX entry to a file named after its cite key."""
    citekey = extract_citekey(entry)
    filename = f"{citekey}.bib"
    filepath = Path(directory) / filename
    
    with open(filepath, 'w') as file:
        file.write(entry)
    print(f"Saved {filename}")

def split_bibtex_file(input_file: str, output_dir: str) -> None:
    """Splits a BibTeX file into multiple files, each containing one entry."""
    # Read the entire content of the BibTeX file
    with open(input_file, 'r') as file:
        bibtex_content = file.read()
    
    # Parse the content into individual entries
    entries = parse_bibtex_entries(bibtex_content)
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Save each entry to a separate file
    for entry in entries:
        save_bibtex_entry(entry, output_dir)

if __name__ == "__main__":
    # Input and output paths
    input_bibtex_file = "./input.bib"
    output_directory = "./temp/"
    
    # Split the BibTeX file
    split_bibtex_file(input_bibtex_file, output_directory)
