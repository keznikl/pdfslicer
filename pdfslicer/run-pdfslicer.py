#!C:\Python\python.exe
import sys
from pdftools.pdfslicer import PdfSlicer

if __name__ == "__main__":
    slicer = PdfSlicer()
    print "Args %d, %s" % (len(sys.argv), sys.argv)
    if len(sys.argv) == 2:
        print "Slicing %s, output %s" % (sys.argv[1], sys.argv[1] + "sliced")
        slicer.slice(sys.argv[1])
    elif len(sys.argv) == 3:
        print "Slicing %s, output %s" % (sys.argv[1], sys.argv[2])
        slicer.slice(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        print "Slicing %s, output %s, with margins vertical %s, horizontal %s" % (
                sys.argv[1],
                PdfSlicer.getOutName(sys.argv[1]),
                sys.argv[2], sys.argv[3])
        slicer.slice(
                sys.argv[1],
                marginv = int(sys.argv[2]),
                marginh = int(sys.argv[3])
                )
    elif len(sys.argv) == 5:
        print "Slicing %s, output %s, with margins vertical %s, horizontal %s" % (
                sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        slicer.slice(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    elif len(sys.argv) == 6:
        print "Slicing %s, output %s, with margins vertical %s, horizontal %s, column width: %s, center width: %s" % (
                sys.argv[1],
                PdfSlicer.getOutName(sys.argv[1]),
                sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        slicer.slice(
                sys.argv[1],
                marginv = int(sys.argv[2]),
                marginh = int(sys.argv[3]),
                columnwidth = int(sys.argv[4]),
                centerwidth = int(sys.argv[5])
                )
    elif len(sys.argv) == 7:
        print "Slicing %s, output %s, with margins vertical %s, horizontal %s, column width: %s, center width: %s" % (
                sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
        slicer.slice(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
    else:
        print "Usage: pdfslicer.py <ifile> [ofile] [margin-vertical margin-horizontal] [column-width center-width]"
        sys.exit(2)
	sys.exit(0)
