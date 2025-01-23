#For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#List Comprehension
new_list = [n + 1 for n in numbers]

#String as List
name = "Angela"
letters_list = [letter for letter in name]
# Output == ['A', 'n', 'g', 'e', 'l', 'a']

#Range as List
range_list = [n * 2 for n in range(1, 5)]
# Output == [2, 4, 6, 8]

#Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
upper_case_names = [name.upper() for name in names if len(name) > 4]
# Output == ['Alex', 'Beth', 'Dave']
# Output == ['CAROLINE', 'ELANOR', 'FREDDIE']

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}

print(passed_students)
# Output == {'Alex': 81, 'Beth': 28, 'Caroline': 49, 'Dave': 58, 'Elanor': 18, 'Freddie': 69}
# Output == {'Alex': 81, 'Freddie': 69}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {words: words.__len__() for words in sentence.split()}
print(result)
# Output == {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}