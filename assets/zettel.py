#!/opt/homebrew/bin python3

import datetime as dt
from textwrap import dedent

ts = dt.datetime.now()
zid = ts.strftime("%Y%m%d%H%M%S")
update = ts.strftime("%Y%m%d")
note = dedent(f"""\
    ---
    id: '{zid}'
    title: 
    updated: '{update}'
    keywords: 
    note-type: zettel
    ---

    # Introduction  

    Lorem ipsom...

    # References

    - Item 1
    - Item 2
    """)

with open(f"./notes/{zid}.md", "w") as f:
    f.write(note)

