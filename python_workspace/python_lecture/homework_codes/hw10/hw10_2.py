# 파일명: hw10_2.py
# 작성자: 유태욱
# 작성일자: 2022-11-15
# 주요기능: Numpy 기반 행렬 연산
# 최종수정일자: 2022-11-15
# 수정내용: 최초작성

import numpy as np  # numpy 모듈을 사용하기 위한 import

def loadtxt():  # 텍스트 파일의 행렬 데이터를 읽어와 2차원 배열로 반환해주는 함수
    f = open('data.txt','r')  # 읽기 전용으로 텍스트 파일을 연다.
    data = []  # 반환할 배열 변수 선언
    while True:  # 무한 루프
        line = f.readline()  # 텍스트 파일에서 1줄 읽어온다.
        if line == '':  # 읽은 값이 없다면
            break  # 반복문을 끝낸다.
        data.append(list(map(int, line.split())))  # 배열 변수에 추가한다

    f.close()  # 사용한 텍스트 파일을 닫는다.
    return data  # 텍스트 파일에서 읽은 배열을 반환해준다.

if __name__ == "__main__":  # 메인 함수인 경우
    A = np.array(loadtxt())  # A에 파일에서 읽은 2차원 배열로 np.array로 만들어준다.
    print("A = \n", A)  # A 출력
    print("A_det = \n", np.linalg.det(A))  # A의 행렬식 계산 및 출력
    print("A_inv = \n", np.linalg.inv(A))  # A의 역행렬 계산 및 출력
    print("E = np.matmul(A,A_inv) = \n", np.matmul(A,np.linalg.inv(A)))  # np.mulmat 함수로 A와 A의 역행렬의 곱을 계산 및 출력