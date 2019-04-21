'''
This file will generate the html report of the test cases. 
As of now we are running this file by importing the test case class.
'''

import unittest
import HtmlTestRunner as ht
import os
import callhub_phonebook.test_phonebook as ft
class MyTestSuite(unittest.TestCase):
  
    def test_Issue(self):
        direct = os.getcwd()
        iphone_test = unittest.TestSuite()
        iphone_test.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(ft.test_callhub)])
        outfile = open(direct + "\callHub_test.html", "w")
  
        runner1 = ht.HTMLTestRunner(
            stream=outfile,
            report_title='Test Report',
            descriptions='Test your script'
        )
  
        runner1.run(iphone_test)

if __name__ == '__main__':
    unittest.main()