def calculate_gpa(letter_grades):
    grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    total_grade_points = sum(grade_points[grade] for grade in letter_grades)
    num_grades = len(letter_grades)
    gpa = total_grade_points / num_grades
    return gpa

def grader(scores):
    grades = []
    for score in scores:
        if score >= 90:
            grades.append('A')
        elif score >= 80:
            grades.append('B')
        elif score >= 70:
            grades.append('C')
        elif score >= 60:
            grades.append('D')
        else:
            grades.append('F')

    return grades