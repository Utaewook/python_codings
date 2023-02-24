# 파일명: Turtle_Drawing.py
# 작성자: 유태욱
# 작성일자: 2022-11-07
# 주요기능: 정다각형을 그리는 함수를 포함하는 모듈
# 최종수정일자: 2022-11-07
# 수정내용: 최초작성
import math

# 초기에 꼭지점 개수에 맞는 다각형의 이름을 저장한 dict 변수 생성 및 할당
vertex_to_polygon = {}
vertex_to_polygon[3] = 'triangle'
vertex_to_polygon[4] = 'square'
vertex_to_polygon[5] = 'pentagon'
vertex_to_polygon[6] = 'hexagon'
vertex_to_polygon[7] = 'heptagon'
vertex_to_polygon[8] = 'octagon'
vertex_to_polygon[9] = 'nonagon'
vertex_to_polygon[10] = 'decagon'

# 다각형의 이름에 맞는 꼭지점 개수를 저장한 dict 변수 생성
polygon_to_vertex = {}
for key in vertex_to_polygon.keys():  # 반복문을 통해 이전에 생성한 vertex_to_polygon dict를 활용하여 값 할당
    polygon_to_vertex[vertex_to_polygon[key]] = key


def getNumVertex(polygon_name):  # 다각형의 꼭지점 개수를 반환하는 함수
    return polygon_to_vertex[polygon_name]  # 미리 생성해둔 dict 변수의 값을 반환해준다


def getPolygonName(num_vertex):  # 꼭지점의 개수로 다각형의 이름을 반환하는 함수
    return vertex_to_polygon[num_vertex]  # 미리 생성해둔 dict 변수의 값을 반환해준다

def drawCircle(t, center_pos, radius, color): # 컴파일 에러 방지를 위한 drawCircle 함수 선언
    pass

def drawStar(t, center_pos, radius, color): # 컴파일 에러 방지를 위한 drawStar 함수 선언
    pass

def drawPolygon(t,cx,cy,radius,n_vert,color):
    t.pencolor(color)  # 다각형의 펜 색상 입력받은 색상으로 설정
    angle = 180 * (1.0 - 2.0 / n_vert)  # 다각형의 내각
    line_length = 2 * radius * math.cos(math.radians(angle / 2))  # 다각형의 한 변의 길이를 구함
    t.penup()  # 선 없이 이동하기 위한 penup
    t.goto(cx, cy)  # 중심점으로 이동한다.

    # 메인 함수에 중심점을 찍는 기능이 구현되어있어 생략
    # t.dot(10, "blue");
    # t.write(t.pos())  # t 현재위치 좌표 찍기

    # 중심점에 있는 t객체를 오른쪽 아래 첫 꼭짓점으로 이동시키기
    t.right(abs(180 - angle / 2))  # 왼쪽 아래 첫 출발 꼭지점으로 가기위한 회전
    t.forward(radius)  # 외접원 반지름 길이만큼 전진
    t.right(angle / 2)  # (180 - 회전시킨만큼의 각도)로 다시 회전해서 정다각형 그릴 준비
    t.pendown()  # 다각형을 그리기 위한 pendown
    for i in range(n_vert):  # 입력받은 내각의 갯수 만큼 반복문
        t.right(180 - angle)  # 180 - 내각 만큼 오른쪽으로 회전
        t.forward(line_length)  # 입력받은 한 변의 길이 만큼 전진

    t.dot(10, "red") # 현재위치에 붉은 점을 찍는다 (정다각형의 시작점)
    t.write(t.pos())  # t 현재위치 좌표 찍기
    t.setheading(0)  # 거북이의 방향을 원래대로 되돌린다