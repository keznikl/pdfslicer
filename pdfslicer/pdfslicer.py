from pyPdf.pdf import PageObject

__author__ = 'Keznikl'
from pyPdf import PdfFileWriter, PdfFileReader


class PdfSlicer():
    @staticmethod
    def getOutName(iname):
        return iname[:-4] + "_sliced.pdf"
    def slice(self, ifile, ofile=None, marginv=0, marginh=0, columnwidth=0, centerwidth=0, scale=0.9):
        output = PdfFileWriter()
        input = PdfFileReader(file(ifile, "rb"))
        # print the title of document1.pdf
        print "title = %s" % (input.getDocumentInfo().title)
        print "Processing page: "
        for i in xrange(input.getNumPages()):
            print i+1
            # add left column as page
            page = PageObject.createBlankPage(input)
            page.mergePage(input.getPage(i))
            if columnwidth != 0 and centerwidth != 0:
                page.mediaBox.upperRight = (
                    page.mediaBox.getUpperLeft_x() + marginh + columnwidth,
                    page.mediaBox.getUpperRight_y() - marginv
                )
            else:
                page.mediaBox.upperRight = (
                    page.mediaBox.getUpperRight_x() / 2,
                    page.mediaBox.getUpperRight_y() - marginv
                )
            page.mediaBox.lowerLeft = (
                page.mediaBox.getLowerLeft_x() + marginh,
                page.mediaBox.getLowerLeft_y() + marginv,
            )
            page.scale(scale, scale)
            output.addPage(page)

            # add right column as page
            page = PageObject.createBlankPage(input)
            page.mergePage(input.getPage(i))
            if columnwidth != 0 and centerwidth != 0:
                page.mediaBox.lowerLeft = (
                    page.mediaBox.getLowerLeft_x() + marginh + columnwidth + centerwidth,
                    page.mediaBox.getLowerLeft_y() + marginv,
                )
            else:
                page.mediaBox.lowerLeft = (
                    page.mediaBox.getUpperRight_x() / 2,
                    page.mediaBox.getLowerLeft_y() + marginv,
                )
            page.mediaBox.upperRight = (
                page.mediaBox.getUpperRight_x() - marginh,
                page.mediaBox.getUpperRight_y() - marginv
            )
            page.scale(scale, scale)
            output.addPage(page)

        # finally, write "output"
        if ofile is not None:
            outputStream = file(ofile, "wb")
        else:
            outputStream = file(PdfSlicer.getOutName(ifile), "wb")
        output.write(outputStream)
        outputStream.close()