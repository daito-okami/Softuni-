def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


n = int(input())

student_grade_lines = input_to_list(n)

students_grade = {}

for line in student_grade_lines:
    student, grade = line.split()
    if student not in students_grade:
        students_grade[student] = []
    students_grade[student].append(float(grade))


for students, grades in students_grade.items():
    grades_str = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
    average = sum(grades) / len(grades)
    print(f'{students} -> {grades_str} (avg: {average:.2f})')