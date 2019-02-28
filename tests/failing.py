import unittest

class TestFailing(unittest.TestFailing):

    def failing(self):
        self.fail("failing...")
