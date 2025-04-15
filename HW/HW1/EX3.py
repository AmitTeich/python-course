def Build_student_records(studentFile,gradesFile):
    f1 = open (studentFile)
    students = list()
    for line in f1:
        line = line.strip()
        students.append(line)
    f1.close()
    f2 = open(gradesFile)
    student_grades = list()
    for line in f2:
        line = line.strip()
        item = line.split()
        student_grades.append(item)
    f2.close()
    student_records = list()
    for j in range(len(students)):
        item=student_grades[j]
        dic = {}
        for i in range(1,len(item)):
            arr = item[i].split(":")
            arr[1] = arr[1].replace(",","")
            dic[arr[0]] = arr[1]
        l = [students[j],dic]
        student_records.append(l)
    return student_records



l = Build_student_records('students.txt','grades.txt')
for lst,d in l:
    print(lst)
    print(f"       ", end="")
    grade = [f"{key}:{d[key]}" for key in d]
    print(", ".join(grade))