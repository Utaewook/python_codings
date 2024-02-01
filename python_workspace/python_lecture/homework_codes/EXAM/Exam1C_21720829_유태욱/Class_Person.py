
# 파일명: Class_Person.py
# 작성자: 유태욱
# 작성일자: 2022-10-23
# 주요기능: name을 속성으로 가지는 사람 클래스 작성
# 최종수정일자: 2022-10-23
# 수정내용: 최초작성


# User-defined module - Class_Person.py
class Person:
    def __init__(self, name):  # 사람 객체의 생성자
        self.name = name  # 입력받은 name값으로  이름 속성을 초기화해준다
        
    def __str__(self):  # 객체의 print를 위한 문자열 반환
        return f"Person({self.name})" # fstring으로 서식에 맞추어 반환