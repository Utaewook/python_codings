# 파일명: Exam2C_21720829_유태욱.py
# 작성자: 유태욱
# 작성일자: 2022-12-11
# 주요기능: Numpy기반 선형시스템 해 산출 프로그램
# 최종수정일자: 2022-12-11
# 수정내용: 최초작성

import numpy as np


def printArray(arr):  # 배열을 출력해주는 함수
    for row in range(len(arr)):  # 행의 갯수 만큼 반복
        for col in range(len(arr[0])):  # 열의 갯수 만큼 반복
            print("{:6d}".format(arr[row][col]), end='')  # 출력 형식에 맞추어 출력
        print()  # 개행 출력


def fgetArray(fin_name):  # 매개변수로 받은 파일이름의 파일의 데이터를 입력받아 반환하는 함수
    data = []  # 리스트 선언
    fin = open(fin_name, 'r')  # 파일 open
    while True:  # 무한 루프 반복문
        line = fin.readline()  # 입력 파일에서 1라인을 읽어온다.
        if not line:  # 읽어온 라인이 비어있다면
            break  # 반복문을 빠져나간다.
        data.append(list(map(int, line.split())))  # 데이터 리스트에 읽어온 라인을 정수형 배열로 변환하여 추가한다.
    fin.close()  # 파일 close
    return data  # 데이터 리스트 반환한다.


def main():  # 메인 함수
    print("2022-2 컴사파 Exam2C 학번: 21720829, 이름: 유태욱")  # 출력문
    mA = fgetArray("fA.txt")  # mA값을 파일에서 읽어온다.
    mB = fgetArray("fB.txt")  # mB값을 파일에서 읽어온다.
    print("mA = ")
    printArray(mA)  # 출력 함수를 통해 mA 배열을 출력한다.
    print("mB = ")
    printArray(mB)  # 출력 함수를 통해 mB 배열을 출력한다.

    A = np.array(mA)  # numpy 모듈을 통해 mA 배열을 numpy 배열로 생성한다.
    B = np.array(mB).T  # numpy 모듈을 통해 mB 배열을 numpy 배열로 생성한다. 선형 시스템 해 산출을 위해 전치된 배열울 사용한다.
    print("A = \n", A)
    print("B = \n", B)
    X = np.linalg.solve(A, B)  # Numpy의 solve() 함수를 사용하여 선형 시스템 AㆍX = B의 해 X를 산출
    print("X = \n", X)
    B1 = np.matmul(A, X)  # Numpy의 matmul() 함수를 사용하여 B1 = AㆍX를 계산
    print("B1 = A * X = \n", B1)  # 파일 fB.txt에서 설정된 값과 계산된 B1를 비교하여 볼 것


# 메인 함수 실행
if __name__ == "__main__":
    main()
