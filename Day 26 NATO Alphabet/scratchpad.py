from random import randint

numbers = [1, 2, 3]
# new_list = [new_item for item in list]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Adam"
new_name = [letter for letter in name]
print(new_name)

double_list = [i * 2 for i in range(1, 5)]
print(double_list)

names = ['Adam', 'Dave', 'Alex', 'Serena', 'Devil Woman', 'Caroline', 'Bethany']
short_names = [name for name in names if len(name) < 5]
print(short_names)

uppercase_names = [name.upper() for name in names if len(name) > 4]
print(uppercase_names)

names = ['Adam', 'Dave', 'Alex', 'Serena', 'Devil Woman', 'Caroline', 'Bethany']
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
student_scores = {student:randint(1, 100) for student in names}
print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
print(passed_students)
