from pyPdf.pdf import PageObject

__author__ = 'Keznikl'
from pyPdf import PdfFileWriter, PdfFileReader


class PdfSlicer():
    @staticmethod
    def getOutName(iname):
        return iname[:-4] + "_sliced.pdf"
    def slice(self, ifile, ofile=None, marginv=0, marginh=0):
        output = PdfFileWriter()
        input = PdfFileReader(file(ifile, "rb"))
        # print the title of document1.pdf
        print "title = %s" % (input.getDocumentInfo().title)

        for i in xrange(input.getNumPages()):

            # add left column as page
            page = PageObject.createBlankPage(input)
            page.mergePage(input.getPage(i))
            page.mediaBox.upperRight = (
                page.mediaBox.getUpperRight_x() / 2,
                page.mediaBox.getUpperRight_y() - marginv
            )
            page.mediaBox.lowerLeft = (
                page.mediaBox.getLowerLeft_x() + marginh,
                page.mediaBox.getLowerLeft_y() + marginv,
            )
            output.addPage(page)

            # add right column as page
            page = PageObject.createBlankPage(input)
            page.mergePage(input.getPage(i))
            page.mediaBox.lowerLeft = (
                page.mediaBox.getUpperRight_x() / 2,
                page.mediaBox.getLowerLeft_y() + marginv,
            )
            page.mediaBox.upperRight = (
                page.mediaBox.getUpperRight_x() - marginh,
                page.mediaBox.getUpperRight_y() - marginv
            )
            output.addPage(page)

        # finally, write "output"
        if ofile is not None:
            outputStream = file(ofile, "wb")
        else:
            outputStream = file(PdfSlicer.getOutName(ifile), "wb")
        output.write(outputStream)
        outputStream.close()