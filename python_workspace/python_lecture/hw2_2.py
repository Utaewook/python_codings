width,length=input("width, length = ").split() # 직사각형의 가로와 세로를 입력 받는 명령어 입력받아 split함수로 나누어 준다.

width=int(width) # string 자료형으로 입력된 가로값을 정수로 바꾸어 준다.
length=int(length) # string 자료형으로 입력된 세로값을 정수로 바꾸어 준다.
print(f"Rectangle of width({width}) and length({length}) : area ({width*length}) , perimeter({2*(width+length)})") # 입력받은 직사각형의 가로