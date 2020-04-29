from bs4 import BeautifulSoup
import sys
import markdown
import os
import fnmatch
from pathlib import Path


def run():

    # check that there is at least one markdown file in the current folder
    markdownFiles = []
    # full path of input md
    inputFile = ""
    # name of input md without file extension, to be used as name for output html
    outputFileName = ""

    for entry in os.listdir("."):
        if fnmatch.fnmatch(entry, "*.md"):
            markdownFiles.append(entry)
    if len(markdownFiles) == 0:
        print("Please provide a Markdown file with the table to convert.")
        return
    if len(markdownFiles) > 1:
        print(
            f"More than one Markdown file detected in current folder. Using {markdownFiles[0]} as input file.")

    # populating inputFile
    inputFile = markdownFiles[0]

    # populating outputFileName based on inputFile
    outputFileName = Path(inputFile).stem

    # f = str(args.input)

    with open(inputFile, 'r') as myfile:
        table_md = myfile.read()

    table_html = markdown.markdown(
        table_md, extensions=['markdown.extensions.tables'])

    soup = BeautifulSoup(table_html, "html.parser")

    soup.prettify("utf-8")

    fout = outputFileName + ".html"

    with open(fout, "w", encoding='utf-8') as file:
        file.write(str(soup))

    print(f"Please find the {fout} output file in the current folder.")


def main():
    run()


if __name__ == "__main__":
    main()
