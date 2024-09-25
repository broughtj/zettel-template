## NB: if the Makefile command `make biblio` fails it is likely
## due to an incorrectly specified bib file (prolly without comma
## one of the entries).

import os
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase


def build(outfile):
    biblio = BibDatabase()
    files = os.listdir(f"./jike")
    entries = list()
    
    for file in files:
        if file.endswith(".bib"):
            with open(f"./jike/{file}") as bfile:
                bstr = bfile.read()
            parser = BibTexParser()
            parser.ignore_nonstandard_types = False
            parser.homogenize_fields = False
            bdb = bibtexparser.loads(bstr, parser)  
            if len(bdb.entries) < 1:
                print(f"Unable to process file: {file}")
                continue
            else:
                entries.append(bdb.entries[0])
                #print(f"Processing file: {file}")
                #print(bdb.entries[0])

    biblio.entries = entries
    writer = BibTexWriter()
    writer.indent = ""
    writer.align_values = True
    writer.entry_separator = "\n"

    with open(outfile, 'w') as f:
        f.write(writer.write(biblio))

if __name__ == "__main__":
    outfile = f"./biblio.bib"
    build(outfile)
