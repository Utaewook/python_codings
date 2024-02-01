# 파일명: MyList.py
# 작성자: 유태욱
# 작성일자: 2022-12-11
# 주요기능: 실수 난수 리스트를 생성/출력하는 함수를 구현한 모듈
# 최종수정일자: 2022-12-11
# 수정내용: 최초작성
import random  # 난수를 생성하기 위한 random 모듈 import


def genRandFloatList(N):  # 실수 난수 리스트를 반환해주는 함수
    data = []  # 초기 데이터 리스트 선언
    for _ in range(N):  # 입력받은 N값만큼 반복하는 함수
        data.append(random.uniform(-1*N/200,N/200))  # -N/200 ~ N/200 범위 내의 실수 난수 추가
    return data  # 생성한 리스트 반환


def printFloatListSample(L, per_line, sample_lines):  # 리스트의 견본 값을 출력하는 함수
    for i in range(per_line * sample_lines):  # 앞 부분의 값을 출력하기 위한 반복문
        print("%10.2f" % L[i], end='\t')  # 각 숫자를 출력(\t로 구분하여)
        if i % per_line == per_line - 1:  # 한 줄의 마지막 숫자를 출력하고 난 경우
            print()  # 개행 출력

    print(" . . . . . .")  # 구분선 출력

    for i in range(len(L) - per_line * sample_lines, len(L)):  # 뒷 부분의 값을 출력하기 위한 반복문
        print("%10.2f" % L[i], end='\t')  # 각 숫자를 출력(\t로 구분하여)
        if i % per_line == per_line - 1:  # 한 줄의 마지막 숫자를 출력하고 난 경우
            print()  # 개행 출력
