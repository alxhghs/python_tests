from operator import itemgetter

if __name__ == '__main__':
    list_of_students = []
    for i in range(int(input("number of students: "))):
        name = input("name: ")
        score = float(input("score: "))
        list_of_students.append([name, score])

list_of_students.sort(key=itemgetter(1))

for student in list_of_students:
    print("student[1] = {}".format(student[1]))
    print("list_of_students[0][1] = {}".format(list_of_students[0][1]))
    if student[1] == list_of_students[0][1]:
        pass
    else:
        second_lowest = student[1]

list_of_second_lowest = []

for student in list_of_students:
    if student[1] == second_lowest:
        list_of_second_lowest.append(student[0])
sorted(list_of_second_lowest)
for student in list_of_second_lowest:
    print(student)
#
# print(list_of_students)
# print(list_of_second_lowest)
