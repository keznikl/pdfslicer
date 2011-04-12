from pdfslicer import PdfSlicer

__author__ = 'Keznikl'

import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.slicer = PdfSlicer()
    def test_slicer_load_file(self):
        self.slicer.slice('test.pdf',  marginv=50, marginh= 55, columnwidth=245, centerwidth=15)

if __name__ == '__main__':
    unittest.main()
