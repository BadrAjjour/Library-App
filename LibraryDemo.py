from Library import Library
from Book import Book
from Person import Student
from Person import Manager

print("Welcome To Library Manager")
print("firs step: initializing the library")

v_books = list()
v_books.append(Book("Book 1", "Auther 1", "2019"))
v_books.append(Book("Book 2", "Auther 2", "2019"))
v_books.append(Book("Book 3", "Auther 2", "2018"))

v_manager = Manager("Bader Ajjour", "28-07-1989", "0599141732", "01-01-2020")
v_library = Library("Library One", v_books, v_manager)

while True:
    print("select Operation: ")
    print("1- Add Book")
    print("2- Set Manager")
    print("3- Add Student")
    print("4- Borrow Book")
    print("5- Return Book")
    print("6- Print Report")
    print("7- Exit")

    v_user_input = input("your input : ")
    
    if v_user_input == "1":
        v_book_name   = input("Book Name : ")
        v_book_auther = input("Book Auther : ")
        v_book_year   = input("Book Year : ")
        v_books.append(Book(v_book_name, v_book_auther, v_book_year))
        print("Book Added Successfully")

    elif v_user_input == "2":
        v_full_name    = input("Manager Full Name : ")
        v_birth_date   = input("Manager Birth Date : ")
        v_mobile_num   = input("Manager Mobile Number : ")
        v_working_date = input("Manager First Working Date : ")
        v_library.set_manager(Manager(v_full_name, v_birth_date, v_mobile_num, v_working_date))
        print("Manager Edited Successfully")

    elif v_user_input == "3":
        v_full_name  = input("Student Full Name : ")
        v_birth_date = input("Student Birth Date : ")
        v_mobile_num = input("Student Mobile Number : ")
        v_reg_date   = input("Student Registration Date : ")
        v_library.students.append(Student(v_full_name, v_birth_date, v_mobile_num, v_reg_date))
        print("Student Added Successfully")

    elif v_user_input == "4":
 
        for idx, item in enumerate(v_library.students, start=1):
            print(str(idx) + "- " + item.full_name, end = '\t')

        v_std_idx = int(input("\nEnter Student Index : "))
        
        if v_std_idx > 0 and  v_std_idx <= len(v_library.students):

            for item in v_library.books:
                print("- " + item.book_name, end = '\t')
            v_book_name = input("\nEnter Book Name : ")
            
            v_res = v_library.borrow_book(v_book_name, v_library.students[v_std_idx - 1])
            if v_res == 1:
                print("Book Borrowed Successfully ")
            elif v_res == 0:
                print("Book Does Not Exists")
            elif v_res == -1:
                print("Book Already Borrowed, please try again later")
        else:
            print("InCorrect Student Index")
    
    elif v_user_input == "5":
        for item in v_library.books:
            print("- " + item.book_name, end = '\t')
        v_book_name = input("\nEnter Book Name : ")
        
        v_res = v_library.return_book(v_book_name)
        if v_res == 1:
            print("Book Returned Successfully ")
        elif v_res == 0:
            print("Book Does Not Exists")
        elif v_res == -1:
            print("Book Is Not Borrowed Yet, please try again later")

    elif v_user_input == "6":
        v_library.print_library()
    
    elif v_user_input == "7":
        break

    else:
        print("Incorrect Option")

print("Thank you for using library manager app")