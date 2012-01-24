from pyPdf import PdfFileWriter, PdfFileReader
import optfunc

import sys
from itertools import izip


class InputDocument(object):
    def __init__(self, filename):
        self.filename = filename
        self.pages = PdfFileReader(open(self.filename, "rb"))

    @property
    def count(self):
        return self.pages.getNumPages()

    def __iter__(self):
        for i in range(self.count):
            yield self.pages.getPage(i)

    def __reversed__(self):
        for i in range(self.count,0,-1):
            yield self.pages.getPage(i-1)

class OutputDocument(object):
    def __init__(self, odd_doc, even_doc):
        self.odd_doc = odd_doc
        self.even_doc = even_doc
        self.output = PdfFileWriter()
        self.merge()

    def merge(self):
        for page_odd, page_even in izip(self.odd_doc, reversed(self.even_doc)):
            self.output.addPage(page_odd)
            self.output.addPage(page_even)

    def write_to_file(self, filename):
        self.output.write(open(filename, "wb"))

@optfunc.arghelp("output_filename", "Desired name of the final merged PDF document. If none given, 'merged.pdf' will be used")
def entry(odd_pages_filename,even_pages_filename, output_filename='merged.pdf'):
    """Usage: %prog <odd_pages_file> <even_pages_file> [--output_filename] - Merge the odd pages and even pages of a document"""
    odd_pages = InputDocument(odd_pages_filename)
    even_pages = InputDocument(even_pages_filename)

    merged_pages = OutputDocument(odd_pages, even_pages)
    merged_pages.write_to_file(output_filename)


if __name__ == "__main__":
    optfunc.run(entry)


