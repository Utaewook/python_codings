# 파일명: hw7_1.py
# 작성자: 유태욱
# 작성일자: 2022-10-17
# 주요기능: 사람 정보 및 학생 정보를 갖는 클래스 구현
# 최종수정일자: 2022-10-17
# 수정내용: 최초작성

# Example of class Person, class Student inheritance in Python (1)


class Person:  # 사람의 정보를 갖는 클래스

    def __init__(self, name, reg_id, age):  # 사람 객체의 생성자
        self.age = None  # 나이 변수를 초기화
        self.reg_id = None  # 주민 번호 변수를 초기화
        self.name = None  # 이름 변수를 초기화
        self.setName(name)  # 내부 메소드로 이름을 지정(정상 범위 검사)
        self.setReg_id(reg_id)  # 내부 메소드로 주민 번호를 지정(정상 범위 검사)
        self.setAge(age)  # 내부 메소드로 나이를 지정(정상 범위 검사)

    def __str__(self):  # 해당 객체의 print를 위한 문자열 반환
        return f"Person ({self.name}, {self.reg_id}, {self.age})"  # 지정된 양식에 따라 fstring으로 반환

    def getName(self):  # 사람 객체 이름 접근자
        return self.name  # 이름 반환

    def getReg_id(self):  # 사람 객체 주민 번호 접근자
        return self.reg_id  # 주민 번호 반환

    def getAge(self):  # 사람 객체 나이 접근자
        return self.age  # 나이 반환

    def setName(self, new_name):  # 사람 객체 이름 변경자
        if str.isalpha(new_name):  # 사람 이름 매개 변수가 알파벳으로만 이루어진 경우라면
            self.name = new_name  # 해당 객체 이름을 매개 변수 값으로 변경한다.
        else:  # 그 외의 경우
            self.name = None  # None 지정

    def setReg_id(self, new_reg):  # 사람 객체 주민 번호 변경자
        if isinstance(new_reg, int) and new_reg >= 0:  # 사람 주민 번호 매개 변수가 정수형이며 양수인 경우라면
            self.reg_id = new_reg  # 해당 객체 주민 번호를 매개 변수 값으로 변경한다.
        else:  # 그 외의 경우
            self.reg_id = None  # None 지정

    def setAge(self, new_age):  # 사람 객체 나이 변경자
        if isinstance(new_age, int) and new_age >= 0:  # 사람 나이 매개 변수가 정수형이며 양수인 경우라면
            self.age = new_age  # 해당 객체 나이를 매개 변수 값으로 변경한다.
        else:  # 그 외의 경우
            self.age = None  # None 지정


class Student(Person):  # 학생의 정보를 갖는 클래스로, Person 클래스를 상속받아 만들어짐

    def __init__(self, name, reg_id, age, st_id, major, gpa):  # 학생 객체의 생성자
        super().__init__(name, reg_id, age)  # 부모 클래스의 생성자를 이용해 이름, 주민 번호, 나이를 생성/저장
        self.gpa = None  # 학점 변수 초기화
        self.major = None  # 전공 변수 초기화
        self.st_id = None  # 학번 변수 초기화
        self.setSt_id(st_id)  # 내부 메소드로 학번을 지정(정상 범위 검사)
        self.setMajor(major)  # 내부 메소드로 전공을 지정(정상 범위 검사)
        self.setGpa(gpa)  # 내부 메소드로 학점을 지정(정상 범위 검사)

    def __str__(self) -> str:  # 해당 객체의 print를 위한 문자열 반환
        return f"Student({self.name}, {self.reg_id}, {self.st_id}, {self.age}, \"{self.major}\", {self.gpa:.1f})"  # 지정된 양식에 따라 fstring으로 반환

    def getSt_id(self):  # 학생 객체 학번 접근자
        return self.st_id  # 학번 반환

    def getMajor(self):  # 학생 객체 전공 접근자
        return self.major  # 전공 반환

    def getGpa(self):  # 학생 객체 학점 접근자
        return self.gpa  # 학점 반환

    def setSt_id(self, new_st_id):  # 학생 객체 학번 변경자
        if isinstance(new_st_id, int):  # 학생 학번 매개 변수가 정수형인 경우
            self.st_id = new_st_id  # 해당 객체 학번을 매개 변수 값으로 변경한다.
        else:  # 그 외의 경우
            self.st_id = None  # None 지정

    def setMajor(self, new_major):  # 학생 객체 전공 변경자
        if str.isalpha(new_major):  # 학생 전공 매개 변수가 알파벳으로만 이루어진경우
            self.major = new_major  # 해당 객체 전공을 매개 변수 값으로 변경한다.
        else:  # 그 외의 경우
            self.major = None  # Noene 지정

    def setGpa(self, new_gpa):  # 학생 객체 학점 변경자
        if isinstance(new_gpa, float):  # 학생 학점 매개 변수가 float 형 인경우
            self.gpa = new_gpa  # 해당 객체 학점을 매개 변수 값으로 변경한다.
        else:  # 그 외의 경우
            self.gpa = None  # None으로 지정


def compareStudent(st1, st2, key):  # 두 학생을 비교하는 함수
    if key == 'st_id':  # 만약 비교 기준이 학번인 경우
        if st1.st_id < st2.st_id:  # st1의 학번이 st2의 학번보다 작은 경우
            return True  # True 반환
        else:  # 그 외의 경우
            return False  # False 반환


def sortStudent(L_st, key):  # 학생 정보 배열을 정렬하는 함수
    for i in range(0, len(L_st)):  # 0 부터 끝까지
        min_idx = i  # 최소값의 인덱스를 i로 지정
        for j in range(i + 1, len(L_st)):  # i+1 부터 끝까지
            if compareStudent(L_st[j], L_st[min_idx], key):  # j번째 학생과 j+1번째 학생의 학번을 비교해서 j번째가 작은경우
                min_idx = j  # 최소값의 인덱스에 j 값을 저장
        if min_idx != i:  # 최소값이 i(초기에 지정한값)가 아니라면
            L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]  # 최소 값과 현재 i번째 값과 바꿔 준다


def printStudents(L_st):  # 학생 배열의 데이터를 출력하는 함수
    for s in range(len(L_st)):  # 리스트의 길이 만큼 반복하는 반복문
        print(L_st[s])  # s 인덱스의 학생의 정보를 출력


# application
if __name__ == "__main__":
    students = [
        Student("Kim", 990101, 21, 12345, "EE", 4.0),
        Student("Lee", 980715, 22, 11234, "ME", 4.2),
        Student("Park", 101225, 20, 10234, "ICE", 4.3),
        Student("Hong", 110315, 19, 13123, "CE", 4.1),
        Student("Yoon", 971005, 23, 11321, "ICE", 4.2),
        Student("Wrong", 100000, 23, 15321, "??", 3.2)]
    print("students before sorting : ")
    printStudents(students)
    #
    sortStudent(students, "name")
    print("\nstudents after sorting by name : ")
    printStudents(students)
    #
    sortStudent(students, "st_id")
    print("\nstudents after sorting by student_id : ")
    printStudents(students)
    #
    sortStudent(students, "GPA")
    print("\nstudents after sorting by GPA in decreasing order : ")
    printStudents(students)
