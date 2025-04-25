def Build_student_records(studentFile,gradesFile):
    f1 = open (studentFile)
    students_dic = {}
    for line in f1:
        line = line.strip().split(" ",1)
        students_dic[line[0]] = line[1]
    f1.close()
    f2 = open(gradesFile)
    student_grades = list()
    for line in f2:
        line = line.strip().replace(",","").split()
        student_grades.append(line)
    f2.close()
    student_records = list()
    for entry in student_grades:
        student_id = entry[0]
        grades = [x.split(":") for x in entry[1:]]
        dic = {key: val for key,val in grades}
        student_records.append([student_id, students_dic[student_id], dic])
    student_records.sort(key = lambda x:x[0])
    return student_records


def main():
    student_records = Build_student_records('students.txt','grades.txt')
    for student in student_records:
        print(f"{student[0]} {student[1]}")
        print(f"       ", end="")
        grade = [f"{key}:{student[2][key]}" for key in sorted(student[2])]
        print(", ".join(grade))

if __name__ == '__main__':
    main()

