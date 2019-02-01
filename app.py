from mymodules.models import Student
from mymodules.math_utils import average_grade

def __main__():
    roster = []
    roster.append(Student("Joe", 100))
    roster.append(Student("Doe", 95))
    roster.append(Student("John", 95))
    roster.append(Student("Jane", 83))
    roster.append(Student("Rob", 95))
    roster.append(Student("Bob", 92))
    roster.append(Student("Mary", 83))
    roster.append(Student("Cone", 96))
    roster.append(Student("Mark", 87))
    roster.append(Student("John", 84))
    
    for students in roster:
        students.print_student_info()

    (average_grade(roster))
    
__main__()