#!/opt/homebrew/bin python3

import datetime as dt
from textwrap import dedent

ts = dt.datetime.now()
today = ts.strftime("%Y%m%d")
note = dedent(f"""\
    ---
    date: '{today}'
    keywords: 
    note-type: daily 
    ---

    # Morning Reflection

    Lorem ipsom...

    # Evening Reflection

    Lorem ipsom...

    """)

with open(f"./dailies/{today}.md", "w") as f:
    f.write(note)

