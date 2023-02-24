import turtle as t # turtle 그래픽을 사용하기 위한 turtle 라이브러리 import

x,y=input("pos_x, pos_y : ").split() # x,y값을 입력받고 split으로 나누어 할당해준다.
radius=float(input("radius = ")) # 반지름 값을 입력받고 float자료형으로 바꾸어준다.

x=int(x) # x값을 int자료형으로 바꾸어준다.
y=int(y) # y값을 int자료형으로 바꾸어준다.

print(f"Drawing a circle of radius ({radius}) at position({x},{y}) at start_position({x},{y-radius})") # 입력받은 중심 위치 값과 반지름을 통해 관련된 정보를 출력해준다

t.shape('classic') # Turtle의 펜 모양을 classic으로 바꾸어준다.

t.penup() # 펜을 든다.(지정 위치까지 가는동안 그림을 그리지 않게 하기 위해)
t.setpos(x,y) # 입력받은 원의 중심까지 이동한다.
t.pendown() # 펜을 내린다.(원의 중심점을 그리기 위해)

t.dot(4,'blue') # 원의 중심에 파란색 점을 찍는다.

t.penup() # 펜을 든다.(지정 위치까지 가는동안 그림을 그리지 않게 하기 위해)
t.write((t.pos()),True) # 현재 펜의 위치를 적는다.

t.penup() # 펜을 든다.(지정 위치까지 가는동안 그림을 그리지 않게 하기 위해)
t.setpos(x,y-radius) # 원을 그리기 시작할 위치까지 이동한다.
t.pendown() # 펜을 내린다.(원을 그리기 위해)

t.circle(radius) # 입력받은 반지름의 원을 그린다.

t.penup() # 펜을 든다.(지정 위치까지 가는동안 그림을 그리지 않게 하기 위해)
t.write((t.pos()),True) # 원을 그리기 시작한(종료한) 펜의 위치를 적는다.

t.ht() # 펜 모양을 안보이도록 바꾼다.

t.done() # Turtle의 그리기가 끝난다.