
# 파일명: Class_Student.py
# 작성자: 유태욱
# 작성일자: 2022-10-23
# 주요기능: Person을 상속받으며, 학번/전공/성적을 추가 속성으로 가지는 클래스 구현
# 최종수정일자: 2022-10-23
# 수정내용: 최초작성

from Class_Person import *

class Student(Person):
    def __init__(self, name, st_id, major, gpa):  # 학생 클래스의 생성자
        super().__init__(name)  # 부모 클래스의 생성자를 이용해 이름 속성을 초기화
        self.st_id = st_id  # 입력받은 학번으로 학번 속성 초기화
        self.major = major  # 입력받은 전공으로 전공 속성 초기화
        self.gpa = gpa  # 입력받은 학점으로 학점 속성 초기화
        
        
    def __str__(self): # 학생 클래스의 print를 위한 문자열 반환
        return f"Student({self.name}, {self.st_id}, {self.major}, {self.gpa})"  # fstring으로 서식에 맞추어 반환
    
    
    def compareStudents(st1, st2, key):  # key 에 따라 학생을 비교하기 위한 메소드
        if  key == 'name':  # 키가 이름이라면
            if st1.name<st2.name:  # st1의 이름이 st2의 이름보다 알파벳 순서상 낮은 경우
                return True # True 반환
            else:  # 그 외의 경우
                return False # False 반환
        elif  key == 'st_id':  # 키가 학번이라면
            if st1.st_id<st2.st_id:#st1의 학번이 st2의 학번보다 낮은 경우
                return True # True 반환
            else:  # 그 외의 경우
                return False # False 반환
        elif key == 'GPA': # 키가 학점이라면
            if st1.gpa>st2.gpa:  #st1의 학점이 st2의 학점보다 낮은 경우
                return True # True 반환
            elif st1.gpa==st2.gpa:  #st1의 학점이 st2의 학점과 같은 경우
                return not Student.compareStudents(st1,st2,'st_id_rev')  # 학점의 내림차순을 기준으로 한 우선순위를 반환한다.
            else:  # 그 외의 경우
                return False # False 반환
            
        
def sortStudents(L_st, key):  # 입력받은 학생배열과 key를 기준으로 선택정렬을 수행하는 함수
    for i in range(len(L_st)): #  0부터 배열의 길이 만큼 i를 반복하는 반복문
        min_idx = i # 최소값의 인덱스를 현재 i값으로 설정
        for j in range(i,len(L_st)): # i부터 배열의 길이 만큼 j를 반복하는 반복문
            if Student.compareStudents(L_st[j],L_st[min_idx],key): # 학생 클래스에 구현한 두 학생을 key 기준으로 비교하는 함수를 수행한 결과. (더 작은/ 역순일경우 더 큰) 경우에
                min_idx = j  # 최소값의 인덱스를 현재 j값으로 설정한다.
        if min_idx != i:  # 반복문이 끝나고 i와 최소값의 인덱스가 다른경우
            L_st[min_idx],L_st[i] = L_st[i],L_st[min_idx]  # 두 값을 swap해준다.
    
    
def printStudents(L_st):  # 입력받은 학생배열의 원소들을 모두 출력하는 함수
    for stdt in L_st:  # 배열에 각 요소에 접근하며,
        print(stdt)  # 현재 원소의 학생 정보를 출력한다.