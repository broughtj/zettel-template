#!/usr/bin/env fish

# Check if a filename is provided as an argument
if test (count $argv) -eq 0
    echo "Usage: $argv[0] <filename>"
    exit 1
end

# Create the file with the provided name
touch $argv[1]

# Confirm that the file was created
if test -f $argv[1]
    echo "File '$argv[1]' has been created."
else
    echo "Failed to create the file '$argv[1]'."
end
