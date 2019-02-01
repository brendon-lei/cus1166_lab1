from mymodules import models

def average_grade(roster):
    sum = 0
    for student in roster:
        sum += student.get_grade()
    average = sum/len(roster)
    print(f"Average of student's grades {average}")