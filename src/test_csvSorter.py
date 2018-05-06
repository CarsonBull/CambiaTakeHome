import unittest
from csvSorter import get_line, get_words


class TestCSVSorter(unittest.TestCase):
    def test_getLine(self):
        '''Tests the get_line function actually gets a line and fails on non string inputs, nonexistant files and files without newlines'''
        self.assertEqual(get_line("testFile.csv"),"this is a line\n")
        self.assertRaises(ValueError, get_line, 2)
        self.assertRaises(IOError, get_line, "file that doesnt exist")

    def test_get_words(self):
        '''tests that the get_words function returns a list of words that come from a get line function'''
        self.assertEqual(get_words("this,is,a,Test\n") , ["this","is","a","Test"])
        self.assertEqual(get_words("this,1,a!,test\n") , ["this","1","test"])
        self.assertEqual(get_words("\n") , [])
        self.assertEqual(get_words("this,is,,test\n") , ["this","is","test"])
        self.assertEqual(get_words("this,i1s,a,te st\n") , ["this","i1s","a","te st"])
        self.assertRaises(ValueError, get_words, 2)

    def test_word_sorter(self):
        '''Tests that the word sorter works to sort words'''
        self.assertEqual(word_sorter(["this","is","a","test"]), ["this","test","is","a"])
        self.assertEqual(word_sorter(["z","c","b","a"]), ["z","c","b","a"])
        self.assertEqual(word_sorter(["a","b","c","z"]), ["z","c","b","a"])
        self.assertEqual(word_sorter(["c","a","c","z"]), ["z","c","c","a"])
        self.assertEqual(word_sorter(["the","cat","ca t","z"]), ["z","the","cat","ca t"])
        self.assertEqual(word_sorter(["c1","a","1d","c","2","1","z"]), ["z","c1","c","a","2","1d","1"])
        self.assertRaises(ValueError, word_sorter, 2.13)
