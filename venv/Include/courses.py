class Course:
    def __init__(self, department, number, title, students=0):
        self.department = department
        self.number = number
        self.title = title
        self.students = students

    def mark_attendance(self,*students):
        for x in students:
            if self.is_present(x):
                self.students += 1

    def is_present(self,student):
        if student.present == True:
            return True
        else:
            return False




class CSCourse(Course):
    def __init__(self, department, number, title, recorded=False):
        super().__init__(department, number, title)
        self.is_recorded = recorded

    def __le__ (self,other):
        a = int(self.number)
        b = int(other.number)
        print(a)
        print(b)
        if self.title > other.title:
            return True
        else:
            return False