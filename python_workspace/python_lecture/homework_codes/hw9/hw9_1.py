# 파일명: hw9_1.py
# 작성자: 유태욱
# 작성일자: 2022-11-07
# 주요기능: 파일에서 정다각형 정보를 읽은 후, turtle 그래픽으로 그리는 프로그램
# 최종수정일자: 2022-11-07
# 수정내용: 최초작성

import turtle
from Turtle_Drawing import *

def fget_drawings(fin):  # 파일에서 다각형의 정보를 읽어 리스트로 반환하는 함수
    L_drawings = []  # 반환할 정보 리스트 선언
    while True:  # 반복문 반복
        line = fin.readline()  # 파일에서 1줄 입력받는다
        if line == '':  # 만약 빈줄이라면
            break  # 반복문을 끝낸다
        c,s,x,y,r = line.split()  # 읽어들인 데이터를 분리한다.
        data = (int(x),int(y),s,int(r),c)  # 리스트에 추가할 튜플 데이터를 만든다
        L_drawings.append(data)  # 튜플 데이터를 리스트에 추가한다.

    return L_drawings  # 반복문을 돌며 입력받은 튜플의 배열을 반환한다.

if __name__ == "__main__":
    turtle.setup(900, 500)
    turtle.title("Drawing polygons with user-defined Turtle_Drawing.py")
    t = turtle.Turtle()
    t.shape("classic")
    fin = open("drawings.txt")  # Homework 9.1의 지시에 따라 drawing.txt로 수정
    L_drawings = fget_drawings(fin)
    fin.close()
    for drawing in L_drawings:
        (cx, cy, shape, radius, color) = drawing
        center_pos = (cx, cy)
        print("drawing a {} {} of circumscribed circle's radius {} at center_pos({}, {}).".format(color, shape, radius, cx, cy))
        t.up(); t.goto(center_pos); t.down()
        t.dot(10, "red"); t.write(center_pos)
        t.width(5)
        if (shape == "circle"):
            drawCircle(t, center_pos, radius, color)
        elif (shape == "star"):
            drawStar(t, center_pos, radius, color)
        else:
            num_vert = getNumVertex(shape)
        if num_vert != None:
            drawPolygon(t, cx, cy, radius, num_vert, color)  # Homework 9.1의 지시에 따라 center_pos -> cx,cy로, num_vert,radius순서 수정
        else:
            print("Drawing shape {} is not implemented yet !!".format(shape))
    turtle.exitonclick()  # 그려진 그림 확인을 위한 turtle 그래픽 창 종료 모드