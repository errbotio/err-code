# coding=utf-8
from errbot.backends.test import FullStackTest

class TestCommands(FullStackTest):
    @classmethod
    def setUpClass(cls, extra=None):
        super().setUpClass(__file__)

    def test_python(self):
        self.assertCommand('!python print 1+1', '2', timeout=15)
