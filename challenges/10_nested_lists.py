if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
students = sorted(students, key=lambda student: student[1])

second_highest = sorted(list(set([marks for name, marks in students])))[1]

final_list = []
for student in students:
    if student[1] == second_highest:
        final_list.append(student[0])

for student in sorted(final_list):
    print(student)
