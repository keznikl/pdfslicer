#!C:\Python\python.exe
import sys
from pdftools.pdfslicer import PdfSlicer

if __name__ == "__main__":
	slicer = PdfSlicer()
	print "Args %d, %s" % (len(sys.argv), sys.argv)
	if len(sys.argv) == 3:
		print "Slicing %s, output %s" % (sys.argv[1], sys.argv[2])
		slicer.slice(sys.argv[1], sys.argv[2])
	elif len(sys.argv) == 5:
		print "Slicing %s, output %s, with margins horizontal %s, vertical %s" % (
				sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
		slicer.slice(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
	else:
		print "Usage: pdfslicer.py <ifile> <ofile> [margin-vertical margin-horizontal]"
		sys.exit(2)
	sys.exit(0)
