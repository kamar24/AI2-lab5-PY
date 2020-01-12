from courses import Course, CSCourse
from student import Student
stanford_python = Course("CS", "41", "hap.py code: The python programming language")
print(stanford_python.title)
print(stanford_python.number)

a = Course("CS", "106A", "Programming Methodology")
b = CSCourse("CS", "106B", "Programming Abstractions")

print()
print(type(a))
print(isinstance(a,Course))
print(isinstance(b,Course))
print(type(a) == type(b))
print(a==b)

student1 = Student("aa","ss",True)
student2 = Student("bb","aa",False)

print()
print(stanford_python.students)
stanford_python.mark_attendance(student1,student2)
print(stanford_python.students)
print(a.students)
print()

cs107 = CSCourse("CS", "107", "Computer Organzation and Systems")
cs110 = CSCourse("CS", "110", "Principles of Computer Systems")

print(cs107.__le__(cs110))