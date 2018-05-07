import unittest
from csvSorter import get_line, get_words, sort_words, compare_words, output_CSV


class TestCSVSorter(unittest.TestCase):
    def test_get_line(self):
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

    def test_sort_words(self):
        '''Tests that the word sorter works to sort words'''
        self.assertEqual(sort_words(['a']), ['a'])
        self.assertEqual(sort_words(['a','b']), ['b','a'])
        self.assertEqual(sort_words(["this","is","a","test"]), ["this","test","is","a"])
        self.assertEqual(sort_words(["z","c","b","a"]), ["z","c","b","a"])
        self.assertEqual(sort_words(["a","b","c","z"]), ["z","c","b","a"])
        self.assertEqual(sort_words(["c","a","c","z"]), ["z","c","c","a"])
        self.assertEqual(sort_words(["the","cat","ca t","z"]), ["z","the","cat","ca t"])
        self.assertEqual(sort_words(["c1","a","1d","c","2","1","z"]), ["z","c1","c","a","2","1d","1"])
        self.assertRaises(ValueError, sort_words, ["this","is",1,"bad","situation"])
        self.assertRaises(ValueError, sort_words, 2.13)

    def test_compare_word(self):
        '''Tests that the compare_words function returns true when word1 should be placed before word2 and false otherwise'''
        self.assertEqual(compare_words("b","a"), True)
        self.assertEqual(compare_words("a","b"), False)
        self.assertEqual(compare_words("1","1a"), False)
        self.assertEqual(compare_words("cat","ca t"), True)
        self.assertEqual(compare_words("testy","test"), True)
        self.assertRaises(ValueError, compare_words, 2.13 , 321)

    def test_output_csv(self):
        '''Tests that the output_CSV function puts the output in the correct file'''
        outputName = "output.csv"
        output_CSV(outputName, ["z","a"])
        with open(outputName) as outputFile:
            self.assertEqual(outputFile.readline(), "z,a\n")

        outputName = "output1.csv"
        output_CSV(outputName, [])
        with open(outputName) as outputFile:
            self.assertEqual(outputFile.readline(), "\n")

        self.assertRaises(IOError, output_CSV, "testFile.csv", [])
