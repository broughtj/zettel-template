#!/opt/homebrew/bin python3

import datetime as dt
from textwrap import dedent
import re

def sanitize_filename(title):
    # Remove invalid filename characters and replace spaces with underscores
    return re.sub(r'[^\w\-_\. ]', '', title).replace(' ', '_')

# Prompt user for title
user_title = input("Enter the title for your note: ")

ts = dt.datetime.now()
zid = ts.strftime("%Y%m%d%H%M%S")
update = ts.strftime("%Y%m%d")

note = dedent(f"""\
    ---
    id: '{zid}'
    title: '{user_title}'
    updated: '{update}'
    keywords: 
    note-type: zettel
    ---

    # {user_title}

    Lorem ipsom...

    # References

    - Item 1
    - Item 2
    """)

# Create a sanitized filename using the title and zid
#filename = f"{sanitize_filename(user_title)}_{zid}.md"
filename = f"{zid} -- {sanitize_filename(user_title)}.md"

with open(f"./notes/{filename}", "w") as f:
    f.write(note)

print(f"Note created: {filename}")
