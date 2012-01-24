This is a simple little script for merging two PDFs. In particular, it's for people who own a sheet-fed scanner that can only scan one side of a piece of paper. A typical usage scenario with these scanners, and double-sided paper is:

 1. Do the scan on the first side of the stack of papers. This generates a PDF with all the odd-numbered pages (1,3,5,etc.)
 2. Flip the stack of paper around and scan again. This generates a PDF, in reverse order, with the even-numbered pages (10,8,6,4,2)
 3. Ponder as to how to turn that into a single document

Given these two PDF documents, this script will merge them into, with all the pages in the right order. Note that we assume that the even-numbered pages will be
in reverse order.

### Requirements

You'll need PyPDF, which is available via `pip` as well as `optfunc`, which you can get here: https://github.com/simonw/optfunc 
