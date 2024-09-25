import os
import subprocess

def main():
    citekey = input("Enter the citekey for the BibTeX entry: ").strip()
    filename = f"./jike/{citekey}.bib"
    subprocess.call(f"touch {filename}", shell=True)
    #subprocess.call("nvim {filename}", shell=True)
    print(filename)

if __name__ == "__main__":
    main()
