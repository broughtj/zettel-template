import re
import argparse
import yaml

def parse_bibtex_entry(file_path):
    with open(file_path, 'r') as file:
        bibtex_entry = file.read().strip()
    return bibtex_entry

def bibtex_to_yaml(bibtex_entry):
    # Extract fields from the BibTeX entry
    fields = {}
    entry_type_match = re.match(r'@\w+\{([^,]+),', bibtex_entry)
    if entry_type_match:
        fields['type'] = entry_type_match.group(0).strip('@').split('{')[0]

    key_value_pairs = re.findall(r'(\w+)\s*=\s*\{(.+?)\}', bibtex_entry, re.DOTALL)
    for key, value in key_value_pairs:
        fields[key.lower()] = value.strip()

    return fields

def generate_yaml(bibtex_entry, output_path):
    # Convert BibTeX entry to a dictionary
    yaml_content = bibtex_to_yaml(bibtex_entry)
    
    # Dump the dictionary to a YAML formatted string
    yaml_str = yaml.dump(yaml_content, default_flow_style=False).strip()

    # Write the YAML content to the output file
    with open(output_path, 'w') as file:
        file.write(yaml_str)

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Convert a BibTeX entry to YAML format.")
    parser.add_argument('input_file', type=str, help="Path to the input BibTeX file.")
    parser.add_argument('output_file', type=str, help="Path to the output YAML file.")

    args = parser.parse_args()

    # Parse the BibTeX entry from the file
    bibtex_entry = parse_bibtex_entry(args.input_file)

    # Generate the YAML content
    generate_yaml(bibtex_entry, args.output_file)

    print(f"YAML file generated: {args.output_file}")

if __name__ == "__main__":
    main()
