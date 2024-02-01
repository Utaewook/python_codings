# 파일명: hw7_3.py
# 작성자: 유태욱
# 작성일자: 2022-10-18
# 주요기능: 시/분/초의 데이터 멤버를 가지는 클래스 구현
# 최종수정일자: 2022-10-18
# 수정내용: 최초작성


class Time:  # 시/분/초 데이터를 가지는 시간 클래스
    def __init__(self, hr, mn, sec):  # 시간 객체의 생성자
        self.hr = None  # 시간 변수 초기화
        self.mn = None  # 분 변수 초기화
        self.sec = None  # 초 변수 초기화
        self.setHour(hr)  # 내부 메소드로 시간을 지정(정상 범위 검사)
        self.setMinute(mn)  # 내부 메소드로 분을 지정(정상 범위 검사)
        self.setSecond(sec)  # 내부 메소드로 초를 지정(정상 범위 검사)

    def __lt__(self, other):  # < 연산자 오버로딩을 위한 less than 함수
        if (self.hr, self.mn, self.sec) < (
        other.hr, other.mn, other.sec):  # self 객체의 세 멤버 변수가 입력받은 other의 세 멤버 변수보다 모두 작은 경우
            return True  # True 반환
        else:  # 그 외의 경우
            return False  # False 반환

    def __str__(self):  # 해당 객체의 print를 위한 문자열 반환
        return f"({self.hr:2d}-{self.mn:2d}-{self.sec:2d})"  # 지정된 양식에 맞춰 fstring으로 반환

    def getHour(self):  # 시간 객체 시간 접근자
        return self.hr  # 시간 반환

    def getMinute(self):  # 시간 객체 분 접근자
        return self.mn  # 분 반환

    def getSecond(self):  # 시간 객체 초 접근자
        return self.sec  # 초 반환

    def setHour(self, hr):  # 시각 객체 시간 변경자
        if isinstance(hr, int) and 0 <= hr <= 23:  # 시간 매개 변수가 정수형이며 0~23사이의 값인 경우
            self.hr = hr  # 해당 객체 시간을 매개 변수 값으로 변경한다.
        else:  # 그 외의 경우
            self.hr = None  # None 지정

    def setMinute(self, mn):  # 시간 객체 분 변경자
        if isinstance(mn, int) and 0 <= mn <= 59:  # 분 매개 변수가 정수형이며 0~59사이의 값인 경우
            self.mn = mn  # 해당 객체 분을 매개 변수 값으로 변경한다.
        else:  # 그 외의 경우
            self.mn = None  # None 지정

    def setSecond(self, sec):  # 시간 객체 초 변경자
        if isinstance(sec, int) and 0 <= sec <= 59:  # 초 매개 변수가 정수형이며 0~59사이의 값인 경우
            self.sec = sec  # 해당 객체 초를 매개 변수 값으로 변경한다.
        else:  # 그 외의 경우
            self.sec = None  # None값 지정


# application
if __name__ == "__main__":
    times = [
        Time(23, 59, 59),
        Time(9, 0, 5),
        Time(13, 30, 0),
        Time(3, 59, 59),
        Time(0, 0, 0), ]
    print("times before sorting : ")
    for t in times:
        print(t)

    times.sort()
    print("\ntimes after sorting : ")
    for t in times:
        print(t)
