
# 파일명: hw2_2.py
# 작성자: 유태욱
# 작성일자: 2022-09-14
# 주요기능: 직사각형의 가로, 세로 입력, 넓이와 둘레 계산 및 출력
# 최종수정일자: 2022-09-14
# 수정내용: 최초작성

width,length=input("width, length = ").split() # 직사각형의 가로와 세로를 입력 받는 명령어 입력받아 split함수로 나누어 준다.

width=int(width) # string 자료형으로 입력된 가로값을 정수로 바꾸어 준다.
length=int(length) # string 자료형으로 입력된 세로값을 정수로 바꾸어 준다.
print(f"Rectangle of width({width}) and length({length}) : area ({width*length}) , perimeter({2*(width+length)})") # 입력받은 직사각형의 가로 세로값을 출력하고, 넓이와 둘레 계산 후 출력