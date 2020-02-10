from Person import Student

class Book:
    def __init__(self, book_name, book_auther, book_year):
        self.book_name   = book_name
        self.book_auther = book_auther
        self.book_year   = book_year
        self.is_borrowed = False
        self.student     = None

    def set_borrowed(self, p_student):
        self.student = p_student
        self.is_borrowed = True

    def set_returned(self):
        self.student = None
        self.is_borrowed = False
    
    def print_book(self):
        v_str = "Book Name: " + self.book_name
        v_str = v_str + "\t Book Auther: " + self.book_auther
        v_str = v_str + "\t Book Year: " + self.book_year
        v_str = v_str + "\t Is Borrowed: " + str(self.is_borrowed)
        print(v_str)