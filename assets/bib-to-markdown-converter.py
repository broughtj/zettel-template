#!/usr/bin/env python3

import os
import subprocess

# Prompt the user for a filename
citekey = input("Enter the name of the file you want to create: ")
filename = f"./jike/{citekey}.bib"
yamlname = f"./notes/literature/{citekey}.md"

# Check if the filename is empty
if not citekey:
    print("Filename cannot be empty.")
    exit(1)

# Create the file with the provided name
try:
    open(filename, 'a').close()
    print(f"File '{filename}' has been created.")
except IOError:
    print(f"Failed to create the file '{filename}'.")
    exit(1)

# Edit the file
try:
    subprocess.run(["nvim", filename], check=True)
except subprocess.CalledProcessError:
    print("Error occurred while trying to open the file with nvim.")
    exit(1)

# Generate the markdown note file
try:
    result = subprocess.run(
        ["pandoc", filename, "-s", "-f", "biblatex", "-t", "markdown"],
        capture_output=True,
        text=True,
        check=True
    )
    with open(yamlname, "w") as f:
        f.write(result.stdout)
    print(f"Markdown file '{yamlname}' has been created.")
except subprocess.CalledProcessError:
    print("Error occurred while trying to convert the file with pandoc.")
    exit(1)

print("Process completed successfully.")