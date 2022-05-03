import unittest
from app.models import NewsSource

class SourceTest(unittest.Testcase):
    # test case for behaviour of source class
    def setup(self):
        #method to run before every test
        self.new_source=NewsSource('1234','bbc','we live for news','general','www.bbc.com','en','uk')

    def test_instance(self):      