student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]

    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

for key, value in student_grades.items():
    print(f"{key}: {value}")

# nested_list = ['A', 'B', ['C', 'D']]
# print(nested_list[2][0]) # this prints C
# print(nested_list[2][1]) # this printx D
