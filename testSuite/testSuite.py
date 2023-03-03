import datetime
import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('../test_case', pattern='test*.py')
    result = BeautifulReport(test_suite)
    time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M')
    result.report(filename=f'{time}_testreport', description=f'{time}测试报告', report_dir='report')