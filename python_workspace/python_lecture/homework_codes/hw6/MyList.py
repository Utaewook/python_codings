# 파일명: MyList.py
# 작성자: 유태욱
# 작성일자: 2022-10-04
# 주요기능: 리스트를 생성하고 출력하기 위한 함수를 포함한 모듈
# 최종수정일자: 2022-10-04
# 수정내용: 최초작성

import random

def genRandList(L,size): # 난수값을 갖는 배열을 생성하는 함수
    for i in range(size): # 입력받은 배열의 크기만큼 반복
        L.append(i) # 배열에 인덱스 저장
    L = shuffleList(L) # 배열을 무작위로 섞는다

def printListSample(L,per_line,sample_lines):# 리스트의 견본 값을 출력하는 함수
    for i in range(per_line*sample_lines): # 앞 부분의 값을 출력하기 위한 반복문
        print("%d"%L[i],end='\t') # 각 숫자를 출력(\t로 구분하여)
        if i % per_line == per_line - 1: # 한 줄의 마지막 숫자를 출력하고 난 경우
            print() # 개행 출력
        
    print(" . . . . . .") # 구분선 출력
    
    for i in range(len(L)-per_line*sample_lines,len(L)): # 뒷 부분의 값을 출력하기 위한 반복문
        print("%d"%L[i],end='\t') # 각 숫자를 출력(\t로 구분하여)
        if i % per_line == per_line - 1: # 한 줄의 마지막 숫자를 출력하고 난 경우
            print() # 개행 출력

def shuffleList(L): # 배열을 무작위로 섞기위한 함수
    return random.shuffle(L) # random 모듈의 shuffle 함수를 이용해 섞인 상태의 배열을 반환한다.
