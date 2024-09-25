import os
import re
import yaml
import argparse

def parse_bibtex_entry(file_path):
    with open(file_path, 'r') as file:
        bibtex_entry = file.read().strip()
    return bibtex_entry

def generate_markdown(bibtex_entry, output_path):
    # Extract the title and author from the BibTeX entry
    title_match = re.search(r'title\s*=\s*\{\{(.+?)\}\}', bibtex_entry, re.IGNORECASE)
    author_match = re.search(r'author\s*=\s*\{\{(.+?)\}\}', bibtex_entry, re.IGNORECASE)
    
    title = title_match.group(1) if title_match else "Untitled"
    author = author_match.group(1) if author_match else "Unknown Author"

    # Create YAML header
    yaml_header = {
        'title': title,
        'author': author,
        'bibtex_entry': 'Embedded below'
    }
    
    # Format YAML as string
    yaml_header_str = yaml.dump(yaml_header, default_flow_style=False).strip()

    # Create the Markdown content
    markdown_content = f"---\n{yaml_header_str}\n---\n\n```bibtex\n{bibtex_entry}\n```"

    # Write the Markdown content to the output file
    with open(output_path, 'w') as file:
        file.write(markdown_content)

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Generate a Markdown note from a BibTeX entry.")
    parser.add_argument('input_file', type=str, help="Path to the input BibTeX file.")
    parser.add_argument('output_file', type=str, help="Path to the output Markdown file.")

    args = parser.parse_args()

    # Parse the BibTeX entry from the file
    bibtex_entry = parse_bibtex_entry(args.input_file)

    # Generate the Markdown note with YAML header
    generate_markdown(bibtex_entry, args.output_file)

    print(f"Markdown note generated: {args.output_file}")

if __name__ == "__main__":
    main()
