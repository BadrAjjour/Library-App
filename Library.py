from Book import Book
from Person import Student
from Person import Manager

class Library:
    def __init__(self, p_lib_name, p_books_list, p_lib_manager):
        self.lib_name = p_lib_name
        self.books    = p_books_list
        self.manager  = p_lib_manager
        self.students = list()
    
    def set_manager(self, p_lib_manager):
        self.manager = p_lib_manager

    # 1: book added 
    # 0: book already exists
    def add_book(self, p_book):
        for item in self.books:
            if item.book_name == p_book.book_name:
                return 0
        self.books.append(p_book)
        return 1

    #  1: book deleted
    # -1: book borrowed
    #  0: book not exists
    def delete_book(self, p_book_name):
        idx = 0
        for item in self.books:
            if item.book_name == p_book_name:
                if item.is_borrowed:
                    return -1
                self.books.pop(idx)
                return 1
            idx = idx + 1
        return 0

    #  1: book borrowed
    # -1: book already borrowed
    #  0: book does not exists
    def borrow_book(self, p_book_name, p_student):
        idx = 0
        for item in self.books:
            if item.book_name == p_book_name:
                if item.is_borrowed:
                    return -1
                item.set_borrowed(p_student)
                p_student.reg_book()
                return 1
            idx = idx + 1
        return 0

    #  1: book returned
    # -1: book is not borrowed yet
    #  0: book does not exists
    def return_book(self, book_name):
        idx = 0
        for item in self.books:
            if item.book_name == book_name:
                if item.is_borrowed:
                    item.student.remove_book()
                    item.set_returned()
                    return 1
                return -1
            idx = idx + 1
        return 0

    def print_library(self):
        print("------- " + self.lib_name + " info -------")
        self.manager.print_manager()
        
        print("Books List : ")
        for item in self.books:
            item.print_book()
        
        print("Students List : ")
        for item in self.students:
            item.print_student()