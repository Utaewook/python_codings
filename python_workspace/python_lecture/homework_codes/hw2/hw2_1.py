
# 파일명: hw2_1.py
# 작성자: 유태욱
# 작성일자: 2022-09-14
# 주요기능: 원의 반지름을 입력 받은 후, 넓이 및 원 둘레 계산 후 출력
# 최종수정일자: 2022-09-14
# 수정내용: 최초작성

import math as m # pi값을 활용하기 위한 math라이브러리를 import한다

radius=int(input("radius = ")) # 원의 반지름 radius를 입력받는다

print(f"Circle of radius({radius}) : area ({m.pi*radius**2}) , circumference({2*m.pi*radius})") # math 라이브러리의 pi값을 이용하여 계산한 원의 넓이와 둘레 출력