
# 파일명: 컴사파Exam1C_21720829_유태욱.py
# 작성자: 유태욱
# 작성일자: 2022-10-23
# 주요기능: 메인 모듈
# 최종수정일자: 2022-10-23
# 수정내용: 최초작성

# # Exam1C - Application of class Student
from Class_Student import * #---------------------------------------
if __name__ == "__main__":
    print("2022-2 컴사파Exam1C_21720829_유태욱")
    L_students = [
        Student("Kim", 33333, "EE", 4.0),
        Student("Lee", 88888, "ME", 4.2),
        Student("Park", 11111, "ICE", 4.3),
        Student("Hong", 22222, "CE", 4.1),
        Student("Yoon", 77777, "ICE", 4.2)
        ]
    print("students before sorting : ")
    printStudents(L_students)
    sortStudents(L_students, "name")
    print("\nstudents after sorting by name : ")
    printStudents(L_students)
    sortStudents(L_students, "st_id")
    print("\nstudents after sorting by student_id : ")
    printStudents(L_students)
    sortStudents(L_students, "GPA")
    print("\nstudents after sorting by GPA in decreasing order : ")
    printStudents(L_students)