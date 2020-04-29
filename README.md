# A tiny Python script to turn Markdown-format tables to HTML tables

Unless you are writing Markdown in a flavour that supports CSS classes or merged cells, you need to replace some or all of your tables in Markdown with their inline HTML equivalent.

This is what this little utility is supposed to help with.

## Context

This is my first real stab at producing a standalone executable using [pyinstaller](https://pypi.org/project/PyInstaller/).

I made it to help some of my colleauges who routinely needed to add CSS classes and merge cells in tables with hundreds of rows and/or columns using a Markdown flavour that does not support such niceties.

Although it does work, there are a number of usability issues with the script - I intend to create GitHub Issues to solve these.

If you have any trouble using the script, or have ideas for features, please open a PR or file a GH Issue.

## Usage

1. Save the `md2html.exe` file to a separate folder on your computer.

2. Copy the Markdown table text that you want to convert.

3. Create a new Markdown file in the same folder where you saved `md2html.exe`.

   Paste the Markdown table text that you copied into it.

4. Run `md2html.exe`.

   `md2html.exe` converts the Markdown table in the file that you saved in its parent folder to an HTML `<table>`, and saves it as a `.html` file in the same folder.

   The name of the new `.html` file is the same as the Markdown file that you put the Markdown table text into.

   ***

   NOTE

   If there are no Markdown files in the parent folder of md2html.exe, the program displays a message about this, and shut down.

   If there are more than one Markdown files in the parent folder of md2html.exe, the program uses the first one it detects.
   Note that this might not be the one you need to convert.

   ***

5. Replace the Markdown table you copied in step 2 with the contents of the new `.html` file, and save the original Markdown file that you were working on.

   ***

   NOTE

   Best practice is to delete both the Markdown file with that you created in step 3 and the new `.html` that the script created in the same folder.

   ***
