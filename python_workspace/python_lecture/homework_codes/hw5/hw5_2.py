
# 파일명: hw5_2.py
# 작성자: 유태욱
# 작성일자: 2022-09-30
# 주요기능: 다각형의 한변의 길이/중심점/각의 갯수를 입력받은뒤 turtle 모듈로 출력
# 최종수정일자: 2022-09-30
# 수정내용: 최초작성

# Homework 5.2 Turtle graphic - Polygon with given center position
import turtle, math

def drawPolygon(t, center_x, center_y, line_length, num_vertices): # 다각형을 그리기 위한 
    angle = 180*(1.0 - 2.0 / num_vertices) # 다각형의 내각
    rad = line_length   / 2 / math.cos(math.radians(angle/2)) # 외접원 반지름 길이
    # 중심점에 있는 t객체를 오른쪽 아래 첫 꼭짓점으로 이동시키기
    t.penup() # 선 없이 이동하기 위한 penup
    t.right(angle/2) # 내각의 반틈만큼 오른쪽으로 회전
    t.forward(rad) # 외접원 반지름 길이만큼 전진
    t.right(180-angle/2) # 180 - 오른쪽으로 회전했던 각 만큼 오른쪽으로 회전
    t.pendown() # 다각형을 그리기 위한 pendown
    for i in range(num_vertices): # 입력받은 내각의 갯수 만큼 반복문
        t.dot(10, "red"); t.write(t.pos()) # t 현재위치 좌표 찍기
        t.forward(line_length) # 입력받은 한 변의 길이 만큼 전진
        t.right(180-angle) # 180 - 내각 만큼 오른쪽으로 회저
    
# Application of drawPolygon
t = turtle.Turtle()# turtle 기본 정보 설정

center_x, center_y, num_vertices, line_length = map(int, input("input center_x, center_y, num_vertices, and line_length : ").split(' '))
center_pos = (center_x, center_y)
line_width = 3
t.up(); t.goto(center_pos); t.down()
t.dot(10, "red"); t.write(center_pos)
t.width(line_width)
t.pencolor("blue")
drawPolygon(t, center_x, center_y, line_length, num_vertices)

turtle.exitonclick() # 도형 확인을 위한 클릭시 창 꺼짐으로 설정