import unittest
from app.models import NewsSource

class SourceTest(unittest.Testcase):
    # test case for behaviour of source class
    def setUp(self):
        #method to run before every test
        self.new_source=NewsSource('1234','bbc','we live for news','general','www.bbc.com','en','uk')

    def test_init(self):
        #chech instanciation of object
        self.assertEqual(self.new_source.index,1234)   
        self.assertEqual(self.new_source.org_name,'bbc')
        self.assertEqual(self.new_source.description,'we live for news') 
        self.assertEqual(self.new_source.category,'general')
        self.assertEqual(self.new_source.url,'www.bbc.com')
        self.assertEqual(self.new_source.language,'en')
        self.assertEqual(self.new_source.country,'uk')  

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,NewsSource))