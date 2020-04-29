# Convert Markdown table to HTML `<table>` element using md2html

When you need to include a table that has one or more CSS classes applied to one or more of its columns or cells in a Markdown file, you need to use a HTML `<table>` element.

The md2html script makes the job of converting a Markdown-format table to a valid HTML `<table>` element.

Follow the steps in this article when you need to convert a Markdown table to HTML.

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
