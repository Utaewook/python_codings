
# 파일명: hw7_2.py
# 작성자: 유태욱
# 작성일자: 2022-10-18
# 주요기능: 연/월/일 데이터 멤버를 가지는 클래스 구현
# 최종수정일자: 2022-10-18
# 수정내용: 최초작성


class Date:  # 연/월/일 데이터 가지는 date 클래스
    def __init__(self, yr, mn, dy): # date 객체의 생성자
        self.dy = None # 날짜 변수를 초기화
        self.mn = None # 월 변수를 초기화
        self.yr = None # 연도 변수를 초기화
        self.setYear(yr) # 내부 메소드로 연도를 지정(정상 범위 검사)
        self.setMonth(mn) # 내부 메소드로 월을 지정(정상 범위 검사)
        self.setDay(dy) # 내부 메소드로 날짜를 지정(정상 범위 검사)

    def __lt__(self, other): # < 연산자 오버로딩을 위한 less than 함수
        if (self.yr, self.mn, self.dy) < (other.yr, other.mn, other.dy): # 만약 self 객체의 세 멤버 변수가 other의 세 멤버 변수보다 모두 작은 경우
            return True # True 반환
        else: # 그 외의 경우
            return False # False 반환

    def __str__(self): # 해당 객체의 print를 위한 문자열 반환
        return f"({self.yr}-{self.mn:2d}-{self.dy:2d})" # 지정된 양식에 따라 fstring으로 반환

    def getYear(self): # Date 객체 연도 접근자
        return self.yr # 연도 반환

    def getMonth(self): # Date 객체 월 접근자
        return self.mn # 월 반환

    def getDay(self): # Date 객체 날짜 접근자
        return self.dy # 날짜 반환

    def setYear(self, yr): # Date 객체 연도 변경자
        if isinstance(yr, int) and yr>0: # 연도 매개 변수가 정수형이며 양수인 경우
            self.yr = yr # 해당 객체 연도를 매개 변수 값으로 변경한다.
        else: # 그 외의 경우
            self.yr = None # None 지정

    def setMonth(self, mn): # Date 객체 월 변경자
        if isinstance(mn, int) and 0<mn<13: # 월 매개 변수가 정수형이며 1~12까지의 값인 경우
            self.mn = mn # 해당 객체 월을 매개 변수 값으로 변경한다.
        else: # 그 외의 경우
            self.mn = None # None 지정

    def setDay(self, dy): # Date 객체 날짜 변경자
        if isinstance(dy, int) and (self.mn in [1,3,5,7,8,10,12] and 0<dy<32) or (self.mn in [4,6,9,11] and 0<dy<31): # 날짜 매개 변수가 각 개월에 맞는 날짜의 범위인 경우
            self.dy = dy # 해당 객체 날짜를 매개 변수 값으로 변경한다.
        elif isinstance(dy, int) and self.isLeapYear(self.yr) and self.mn == 2 and 0<dy<30: # 윤년이며 객체의 월이 2월이며, 날짜 매개변수가 1~29일인 경우
            self.dy = dy # 해당 객체 날짜를 매개 변수 값으로 변경한다.
        elif isinstance(dy, int) and not self.isLeapYear(self.yr) and self.mn == 2 and 0<dy<29: # 윤년이 아니며 객체의 월이 2월이며, 날짜 매개변수가 1~28일인 경우
            self.dy = dy # 해당 객체 날짜를 매개 변수 값으로 변경한다.
        else: # 그 외의 경우
            self.dy = None # None 지정

    def isLeapYear(self, yr): # 윤년인지 판별하는 객체 메소드
        if ((yr % 4 == 0) and (yr % 100 != 0)) or (yr % 400 == 0): # 연도 매개 변수가 4로 나누어떨어지며 100으로 안나누어 떨어지거나, 400으로 나누어 떨어지는 경우
            return True # 윤년이 맞음을 반환
        else: # 그 외의 경우
            return False # 윤년이 아님을 반환

# application
if __name__ == "__main__":
    dates = [
        Date(2000, 9, 15),
        Date(1997, 2, 20),
        Date(2001, 5, 2),
        Date(2001, 5, 1),
        Date(1999, 3, 1)
    ]
    print("dates before sorting : ")
    for d in dates:
        print(d)

    dates.sort()
    print("\nstudents after sorting : ")
    for d in dates:
        print(d)
