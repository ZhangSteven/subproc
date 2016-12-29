"""
Test the sub.py
"""

import unittest2



class TestSub(unittest2.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSub, self).__init__(*args, **kwargs)

    def setUp(self):
        """
            Run before a test function
        """
        pass



    def tearDown(self):
        """
            Run after a test finishes
        """
        pass



    def test_syntax(self):
        """
        Error conditions to test:

        1. input file does not exist. (2 files, one OK, the other not)

        2. file exists, but not accessible (no access right).

        3. wrong username/password for sftp.

        4. wrong sftp site (non-existing domain).

        5. timeout (file too big).

        6. log file does not exist.
        """
        self.assertEqual(1, 1)
