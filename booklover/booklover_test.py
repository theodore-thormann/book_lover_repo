import unittest
from booklover import BookLover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test1 = BookLover('Greg', 'greg@internet', 'horror')
        test1.add_book('Frankenstein', 5)
        self.assertTrue('Frankenstein' in test1.book_list.values)
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test2 = BookLover('Greg', 'greg@internet', 'horror')
        test2.add_book('Frankenstein', 5)
        test2.add_book('Frankenstein', 5)
        self.assertEqual(len(test2.book_list), 1)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test3 = BookLover('Greg', 'greg@internet', 'horror')
        test3.book_list = pd.DataFrame({'book_name' : ['Frankenstein'], 'book_rating' : [5]})
        test_case = test3.has_read('Frankenstein')
        self.assertTrue(test_case)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test4 = BookLover('Greg', 'greg@internet', 'horror')
        test4.book_list = pd.DataFrame({'book_name' : ['Frankenstein'], 'book_rating' : [5]})
        test_case = test4.has_read('Dracula')
        self.assertFalse(test_case)
     
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test5 = BookLover('Greg', 'greg@internet', 'horror')
        test5.book_list = pd.DataFrame({'book_name' : ['Frankenstein', 'Dracula', 'Phantom of the Opera'], 'book_rating' : [5,3,1]})
        self.assertEqual(test5.num_books_read(), 3)
          
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test6 = BookLover('Greg', 'greg@internet', 'horror')
        test6.book_list = pd.DataFrame({'book_name' : ['Frankenstein', 'Dracula', 'Phantom of the Opera'], 'book_rating' : [5,3,1]})
        test_list = test6.fav_book()
        self.assertTrue((test_list.book_rating > 3).all())

if __name__ == '__main__':

    unittest.main(verbosity=3)
