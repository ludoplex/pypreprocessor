
import sys
import os
import unittest
from pypreprocessor import pypreprocessor
pypreprocessor.readEncoding = 'utf-8'
pypreprocessor.writeEncoding = 'utf-8'

def testsuite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(DeprecationTest))
    return suite

class DeprecationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pypreprocessor.defines = []
        os.chdir('./tests')
    @classmethod
    def tearDownClass(cls):
        os.chdir('./..')
    def setUp(self):
        super(DeprecationTest, self).setUp()
        pypreprocessor.input = './parseTarget.py'
        pypreprocessor.output = self._testMethodName
    def tearDown(self):
        f = os.path.join(os.getcwd(), pypreprocessor.output)
        pypreprocessor.defines = []
        if(os.path.exists(f)):
            os.remove(f)
        super(DeprecationTest, self).tearDown()
    def test_mode(self):
        pypreprocessor.mode = 'ppcont'
        pypreprocessor.run = True
        pypreprocessor.resume = True
        pypreprocessor.save = False
        pypreprocessor.parse()
        self.assertFalse(os.path.exists(pypreprocessor.output))
    def test_escapeChar(self):
        pypreprocessor.escapeChar = '$'
        pypreprocessor.escape = '#[pypreprocessor]#'
        pypreprocessor.run = True
        pypreprocessor.resume = True
        pypreprocessor.save = False
        pypreprocessor.parse()
        self.assertFalse(os.path.exists(pypreprocessor.output))

    pass

if(__name__ == 'main'):
    unittest.main()