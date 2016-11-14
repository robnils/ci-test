import os
import sys
import unittest

from xmlrunner import xmlrunner


def additional_tests():
    setup_file = sys.modules['__main__'].__file__
    print setup_file
    setup_dir = os.path.abspath(os.path.dirname(setup_file))
    print setup_dir
    return unittest.defaultTestLoader.discover(setup_dir)

if __name__ == '__main__':
    testsuit = additional_tests()
    result = xmlrunner.XMLTestRunner(output='test-reports').run(testsuit)
    if not result.wasSuccessful():
        exit(1)
    exit(0)