
# 파일명: 컴사파Exam1D_21720829_유태욱.py
# 작성자: 유태욱
# 작성일자: 2022-10-23
# 주요기능: 메인모듈
# 최종수정일자: 2022-10-23
# 수정내용: 최초작성

import turtle
from Turtle_Drawing import *
 #---------------------
if __name__ == "__main__":
    turtle.setup(900, 500)
    turtle.title("2022-2 컴사파Exam1D 학번: 2200000, 이름: 김 00")
    t = turtle.Turtle()
    t.shape("classic")
    L_drawings = \
        [(-300, 100, "triangle", 50, "black"), (-100, 100, "square", 50, "green"),\
        ( 100, 100, "pentagon", 50, "blue"), ( 300, 100, "hexagon", 50, "navy"),\
        ( -300, -100, "heptagon", 50, "brown"), ( -100, -100, "octagon", 50, "darkred"),\
        (100, -100, "nonagon", 50, "orange"), ( 300, -100, "decagon", 50, "magenta")]
    for drawing in L_drawings:
        (cx, cy, shape_name, radius, color) = drawing
        center_pos = (cx, cy)
        print("drawing a {} {} of 외접원 반경 {} at center_pos({}, {}).".format(color, shape_name, radius, cx, cy))
        t.width(5)
        num_vert = getNumVertex(shape_name)
        drawPolygon(t, center_pos, num_vert, radius, color)
        
    turtle.exitonclick() # 도형 확인을 위한 클릭시 창 꺼짐으로 설정