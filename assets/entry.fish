#!/usr/bin/env fish

# Prompt the user for a filename
echo -n "Enter the name of the file you want to create: "
read citekey
set filename "./jike/$citekey.bib"
set yamlname "./notes/$citekey.md"

# Check if the filename is empty
if test -z "$filename" 
    echo "Filename cannot be empty."
    exit 1
end

# Create the file with the provided name
touch "$filename"

# Confirm that the file was created
if test -f "$filename"
    echo "File '$filename' has been created."
else
    echo "Failed to create the file '$filename'."
end

# Edit the file 
nvim "$filename"

# Generate the markdown note file
pandoc "$filename" -s -f biblatex -t markdown > "$yamlname"
