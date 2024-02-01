# 파일명: hw10_1.py
# 작성자: 유태욱
# 작성일자: 2022-11-15
# 주요기능: Numpy 확장 모듈을 사용한 선형 시스템 해 산출 프로그램
# 최종수정일자: 2022-11-15
# 수정내용: 최초작성0

import numpy as np  # Numpy 모듈 사용을 위한 import

A = np.array([[1, 5, 3, 3, 7], [3, 4, 5, 6, 7], [1, 3, 5, 7, 9], [3, 1, 4, 1, 5], [5, 5, 3, 3, 1]])  # 계수 행렬 A 초기화
B = np.array([[105], [135], [145], [74], [75]])  # 각 방정식 해 행렬 B 초기화
det_A = np.linalg.det(A)  # 배열 A의 행렬식 계산
inv_A = np.linalg.inv(A)  # 배열 B의 역행렬 계산
X = np.linalg.solve(A, B)  # 선형 시스템의 해 X 계산
B1 = np.matmul(A, X)  # 행렬 곱셈(A*X) 계산
X1 = np.matmul(inv_A, B)  # 행렬 곱셈(inv_A*B) 계산

# 계산된 값 출력
print("A = \n", A)
print("B = \n", B)
print("det_A = \n", det_A)
print("inv_A = \n", inv_A)
print("X = \n", X)
print("B1 = np.matmul(A, X) = \n", B1)
print("X1 = np.matmul(inv_A, X) = \n", X1)
