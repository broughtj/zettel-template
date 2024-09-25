#!/opt/homebrew/bin python3

import datetime as dt
from textwrap import dedent
import re

def sanitize_filename(title):
    # Remove invalid filename characters and replace spaces with underscores
    return re.sub(r'[^\w\-_\. ]', '', title).replace(' ', '_')

def get_note_type():
    note_types = {'f': 'fleeting', 'p': 'permanent', 's': 'structure'}
    while True:
        note_type = input("Enter the note type (f/p/s): ").lower()
        if note_type in note_types:
            return note_types[note_type]
        else:
            print("Invalid note type. Please choose f (fleeting), p (permanent), or s (structure).")

# Prompt user for title
user_title = input("Enter the title for your note: ")

# Prompt user for note type
note_type = get_note_type()

ts = dt.datetime.now()
zid = ts.strftime("%Y%m%d%H%M%S")
update = ts.strftime("%Y%m%d")

note = dedent(f"""\
    ---
    id: '{zid}'
    title: '{user_title}'
    updated: '{update}'
    keywords: 
    note-type: {note_type}
    ---

    # {user_title}

    Lorem ipsom...

    # References

    - Item 1
    - Item 2
    """)

# Create a sanitized filename using the title and zid
filename = f"{zid} -- {sanitize_filename(user_title)}.md"

with open(f"./notes/{note_type}/{filename}", "w") as f:
    f.write(note)

print(f"Note created: {filename}")
