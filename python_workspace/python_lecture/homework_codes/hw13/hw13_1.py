# 파일명: hw13_1.py
# 작성자: 유태욱
# 작성일자: 2022-12-04
# 주요기능: Turtle 객체 기반의 아날로그 시계 프로그램
# 최종수정일자: 2022-12-04
# 수정내용: 최초작성

import turtle  # 선 그리기를 위한 터틀 그래픽 모듈 import
from turtle import *  # 선 그리기를 위한 터틀 그래픽 모듈의 메소드, 객체 import
from datetime import datetime  # 시간 정보를 사용하기 위한 datetime 모듈 import


def jump(distance):  # 매개변수로 받은 distance값 만큼 pen을 점프시키는 함수(선 그리기 없이)
    penup()  # pen을 띄운다
    forward(distance)  # 펜을 distance만큼 전진 시킨다
    pendown()  # pen을 내린다.


def rectangle(width, height):  # 입력받은 너비와 높이만큼의 직사각형을 그리는 함수
    fd(width / 2)  # 너비의 반만큼 전진
    lt(90)  # 왼쪽으로 90도 회전한다.
    fd(height)  # 높이만큼 전진
    lt(90)  # 왼쪽으로 90도 회전한다.
    fd(width)  # 너비만큼 전진
    lt(90)  # 왼쪽으로 90도 회전한다.
    fd(height)  # 높이만큼 전진
    lt(90)  # 왼쪽으로 90도 회전한다.
    fd(width / 2)  # 너비의 반만큼 전진


def make_hand_shape(name, width, height):  # 시계의 침을 그리는 함수
    reset()  # pen의 위치정보를 초기화 시킨다(원점으로)
    left(90)  # 왼쪽으로 90도 회전한다.
    jump(-height * 0.15)  # 높이의 0.15배 한 만큼 반대방향으로 점프한다
    right(90)  # 오른쪽으로 90도 회전한다.
    begin_poly()  # 다각형의 꼭짓점 기록을 시작
    rectangle(width, height * 1.15)  # 직사각형을(시계침) 그린다.
    end_poly()  # 꼭지점 기록을 중지한다.
    clock_hand = get_poly()  # 방금 그린 직사각형의 꼭지점들의 정보를 저장한다.
    register_shape(name, clock_hand)  # name으로 방금 그린 시계침 정보를 저장한다.


def clockface(radius):  # 시계판을 그리는 함수
    reset()  # pen의 위치 정보를 초기화한다.(원점으로)
    pensize(7)  # pen의 크기를 7로 조정한다.
    for i in range(60):  # 60번 반복되는 반복문(60분 쓰기)
        jump(radius)  # 반지름만큼 점프한다.
        if i % 5 == 0:  # i가 5단위의 분이라면
            fd(25)  # 25만큼 전진한다.(그린다)
            jump(-radius - 25)  # 반지름+25만큼 반대방향으로 전진한다.
        else:  # 그 외의 경우에는
            dot(3)  # 3크기의 점을 찍는다.
            jump(-radius)  # 반지름만큼 반대방향으로 전진한다.
        rt(6)  # 오른쪽으로 6도만큼 회전한다.


def setup():  # 시계를 세팅한다.
    global sec_hand, min_hand, hour_hand, writer  # 초침,분침,시침,글자적는 객체를 전역변수로 선언
    mode("logo")  # turtle 객체를 위쪽 방향으로 초기화한다.
    make_hand_shape("sec_hand", 5, 150)  # 시침을 그린다.
    make_hand_shape("min_hand", 10, 130)  # 분침을 그린다.
    make_hand_shape("hour_hand", 15, 110)  # 시침을 그린다.
    clockface(160)  # 반지름 160의 시계판을 생성한다.
    hour_hand = Turtle()  # 시침을 Turtle 객체로 생성한다.
    hour_hand.shape("hour_hand")  # make_hand_shape에서 저장된 시침의 모양을 사용한다.
    hour_hand.color("black", "black")  # 검정색으로 설정
    min_hand = Turtle()  # 분침을 Turtle 객체로 생성한다
    min_hand.shape("min_hand")  # make_hand_shape에서 저장된 분침의 모양을 사용한다.
    min_hand.color("blue1", "blue1")  # 파랑색으로 설정
    sec_hand = Turtle()  # 초침을 Turtle 객체로 생성한다
    sec_hand.shape("sec_hand")  # make_hand_shape에서 저장된 초침의 모양을 사용한다.
    sec_hand.color("red", "red")  # 빨강색으로 설정
    clock_hand_ax = Turtle()  # 시계침의 축을 Turtle 객체로 생성한다.
    clock_hand_ax.shape(name="circle")  # 시계침 축의 모양을 원으로 설정한다.
    clock_hand_ax.color("black")  # 시계침 축을 검정색으로 설정
    for hand in sec_hand, min_hand, hour_hand:  # 모든 시계침을 순회하는 반복문
        hand.resizemode("user")  # 크기 조정 모드를 'user'로 설정한다.
        hand.shapesize(1, 1, 3)  # 시계침의 크기를 설정한다.
        hand.speed(0)  # 시계침의 속도를 설정한다.
        ht()  # turtle을 숨긴다
    writer = Turtle()  # 날짜 등의 정보를 적는 Turtle객체를 생성한다.
    writer.ht()  # turtle을 숨긴다
    writer.pu()  # pen을 띄운다
    writer.bk(85)  # 반대방향으로 85만큼 전진한다.


def getWeekDayString(t):  # 요일 문자열을 반환해주는 함수
    weekday_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # 요일 문자열 배열
    return weekday_name[t.weekday()]  # 매개변수로 받은 date를 요일값(0~7)로 바꾼 후 배열에서 문자열 값 반환


def getDateString(date):  # 날짜 문자열을 반환해 주는 함수
    month_name = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June", "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]  # 월의 이름 배열
    yr = date.year   # 입력받은 date의 연도값 저장
    mn = month_name[date.month - 1]  # 입력받은 date의 월 저장
    dy = date.day  # 입력받은 data의 일 저장
    return "%s %d %d" % (mn, dy, yr)  # 문자열 값으로 반환


def tick():  # 시간이 가는것을 시계침으로 표현하기 위한 함수
    t = datetime.today()  # 오늘의 date 정보를 가져온다
    sec = t.second + t.microsecond * 0.000001  # 가져온 오늘의 date정보에서 초를 가져온다
    minute = t.minute + sec / 60.0  # 가져온 오늘의 date정보에서 분을 가져온다
    hour = t.hour + minute / 60.0  # 가져온 오늘의 date정보에서 시간을 가져온다
    try:
        tracer(False)  # 거북이 애니메이션을 끈다
        writer.clear()  # writer로 그린 그림을 모두 없앤다
        writer.home()  # writer를 원점으로 이동하고 방향을 시작 방향으로 초기화
        writer.pencolor("darkred")  # writer의 펜 색상을 darkred로 설정
        writer.forward(65)  # writer 앞으로 65만큼 전진
        writer.write(getWeekDayString(t), align="center", font=("Courier", 14, "bold"))  # 요일을 시계에 출력한다.
        writer.back(150)  # writer 뒤로 150만큼 이동
        writer.pencolor("brown")  # writer의 펜 색상을 brown으로 설정
        writer.write(getDateString(t), align="center", font=("Courier", 14, "bold"))  # 날짜 문자열을 시계에 출력한다.
        writer.back(30)  # writer 뒤로 30만큼 이동
        hhmmss = "(%2d : %2d : %2d)" % (hour, minute, sec)  # hhmmss형식의 시간,분,초 문자열 생성
        writer.pencolor("red")  # writer의 펜 색상을 red로 설정
        writer.write(hhmmss, align="center", font=("Tahoma", 14, "bold"))  # hhmmss 문자열 시계에 출력한다.
        writer.forward(115)  # writer 앞으로 115만큼 전진
        tracer(True)  # 거북이 애니메이션을 킨다.
        sec_hand.setheading(6 * sec + 90)  # 초침의 방향을 설정한다.
        min_hand.setheading(6 * minute + 90)  # 분침의 방향을 설정한다.
        hour_hand.setheading(30 * hour + 90)  # 시침의 방향을 설정한다.
        tracer(True)  # 거북이 애니메이션을 킨다
        ontimer(tick, 100)  # 0.1 초 후에 tick 함수를 반복
    except Terminator:  # 예외 발생시
        pass  # 함수 pass


def main():  # 메인 함수
    tracer(False)  # 거북이 애니메이션 끈다.
    setup()  # 시계
    tracer(True)   # 거북이 애니메이션 킨다.
    tick()  # 시간 가는 함수 최초 실행
    return "Analog clock demo"  # 메인 함수 문자열 리턴


if __name__ == "__main__":  # 프로그램의 실행문
    mode("logo")  # turtle 객체가 위쪽을 보고 시계방향으로 회전하게 설정한다.
    turtle.setup(500, 500)  # 메인 창의 크기를 설정한다.
    turtle.title("My Analog Clock with Python")  # 메인 창의 제목을 설정한다.
    msg = main()  # 선언 해둔 메인 함수를 통해 시계를 작동시킨다.
    mainloop()  # turtle 메인 창을 유지한다.
