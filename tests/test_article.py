import unittest
from app.models import NewsArticle

class ArticleTest(unittest.TestCase):
    #test case for behaviour of article class
    def setUp(self):
        #method to run beforeevery test
        self.new_article=NewsArticle('bbc','john doh','covid updates','www.bbc.com','www.covidimage.com','covid is slowly dying out','2.5.2022','covid is dying thanks to vaccines')

    def test_init(self):
        #method to check instanciation of objects
        self.assertEqual(self.new_article.source,'bbc')
        self.assertEqual(self.new_article.author,'john doh')
        self.assertEqual(self.new_article.title,'covid updates')
        self.assertEqual(self.new_article.url,'www.bbc.com')
        self.assertEqual(self.new_article.image,'www.covidimage.com')
        self.assertEqual(self.new_article.description,'covid is slowly dying out')
        self.assertEqual(self.new_article.published,'2.5.2022')
        self.assertEqual(self.new_article.content,'covid is dying thanks to vaccines')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,NewsArticle))