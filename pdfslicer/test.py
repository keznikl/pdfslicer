from pdfslicer import PdfSlicer

__author__ = 'Keznikl'

import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.slicer = PdfSlicer()
    def test_slicer_load_file(self):
        self.slicer.slice('test.pdf', 'test-sliced.pdf', 50, 40)

if __name__ == '__main__':
    unittest.main()