import pandas as pd
import numpy as np

class BookLover:

    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre

    def add_book(self, book_name, book_rating):
        
        if book_rating < 0 or book_rating > 5:
            print("Your book rating must be greater than 0, but less than 5.")
        else:
            test = self.book_list[self.book_list.book_name == book_name]
        
            if len(test) > 0:
                print("This book is already in there.")
            else:
                new_book = pd.DataFrame({
                    'book_name': [book_name], 
                    'book_rating': [book_rating]
                })
        
                self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            
    def has_read(self, book_name):
        if book_name in self.book_list.values:
            return True
        else:
            return False
        
    def num_books_read(self):
        return len(self.book_list)

    def fav_book(self):
        fav_books = self.book_list[self.book_list.book_rating > 3]
        return fav_books
# %%
