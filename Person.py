class Person:
    def __init__(self, full_name, birth_date, mobile_num):
        self.full_name  = full_name
        self.birth_date = birth_date
        self.mobile_num = mobile_num

class Student(Person):
    def __init__(self, full_name, birth_date, mobile_num, reg_date):
        super().__init__(full_name, birth_date, mobile_num)
        self.reg_date = reg_date
        self.books_count = 0

    def reg_book(self):
        self.books_count = self.books_count + 1

    def remove_book(self):
        self.books_count = self.books_count - 1
    
    def print_student(self):
        v_str = "Student Name : " + self.full_name
        v_str = v_str + "\t Mobile Number : " + self.mobile_num
        v_str = v_str + "\t Register Date : " + self.reg_date
        v_str = v_str + "\t Books Count : " + str(self.books_count)
        print(v_str)

class Manager(Person):
    def __init__(self, full_name, birth_date, mobile_num, working_date):
        super().__init__(full_name, birth_date, mobile_num)
        self.working_date = working_date

    def print_manager(self):
        v_str = "Manager Name : " + self.full_name
        v_str = v_str + "\t Mobile Number : " + self.mobile_num
        v_str = v_str + "\t Working Date : " + self.working_date
        print(v_str)