import unittest
from main import wordCounter
import codecs

class TextAnalizing(unittest.TestCase):

    def test_text_article(self):
        with codecs.open('test/article.txt', 'r', 'utf-8') as f:
            file_text = f.read()
        self.assertEqual(('to', 9), wordCounter(file_text))

    def test_text_wiki(self):
        with codecs.open('test/wiki.txt', 'r', 'utf-8') as f:
            file_text = f.read()
        self.assertEqual(('python', 9), wordCounter(file_text))

    def test_text_random(self):
        with codecs.open('test/random.txt', 'r', 'utf-8') as f:
          file_text = f.read()
        self.assertEqual(('random', 4), wordCounter(file_text))

if __name__ == '__main__':
    unittest.main()