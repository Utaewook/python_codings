
# 파일명: hw5_1.py
# 작성자: 유태욱
# 작성일자: 2022-09-27
# 주요기능: 정수형 난수 리스트의 정렬 및 경과시간 측정
# 최종수정일자: 2022-09-30
# 수정내용: 함수 작성

from heapq import merge
import random, time

def genBigRandList(n): # 중복되지 않는 정수형 난수를 n개 만큼 생성하는 함수
    ret_list = [x for x in range(n)] # 0부터 n-1 까지의 값을 리스트에 넣는다.
    random.shuffle(ret_list) # 리스트의 값들을 섞는다.(무작위의 난수로 만들어주기 위해)
    return ret_list # 중복되지 않는 정수형 난수를 생성한 리스트를 반환해준다.
    
def printListSample(L, per_line = 10, sample_lines = 2): # 리스트의 견본 값을 출력한다.
    for i in range(per_line*sample_lines): # 앞 부분 20개의 값을 출력하기 위한 반복문
        print("%d"%L[i],end='\t') # 각 숫자를 출력(\t로 구분하여)
        if i % per_line == per_line - 1: # 한 줄의 마지막 숫자를 출력하고 난 경우
            print() # 개행 출력
        
    print(" . . . . . .") # 구분선 출력
    
    for i in range(len(L)-per_line*sample_lines,len(L)): # 뒷 부분 20개의 값을 출력하기 위한 반복문
        print("%d"%L[i],end='\t') # 각 숫자를 출력(\t로 구분하여)
        if i % per_line == per_line - 1: # 한 줄의 마지막 숫자를 출력하고 난 경우
            print() # 개행 출력

def _merge(L_left, L_right): # 두 리스트를 정렬하며 합병하는 함수
    merged_list = [] # 합병할 리스트 변수 하나 초기화
    left_index = right_index = 0 # 왼쪽, 오른쪽 리스트 하나씩 순회하기 위한 인덱스 변수 초기화
    while left_index < len(L_left) and right_index < len(L_right): # 두 리스트 중 하나를 모두 순회 하면 종료되는 반복문
        if L_left[left_index] <= L_right[right_index]: # 왼쪽 리스트의 값이 오른쪽 리스트의 값보다 작거나 같은경우
            merged_list.append(L_left[left_index]) # 해당 값을 합병할 리스트 끝에 삽입
            left_index += 1 # 왼쪽 리스트 인덱스를 1 늘린다.
        else: # 오른쪽 리스트의 값이 왼쪽 리스트의 값보다 작은 경우
            merged_list.append(L_right[right_index]) # 해당 값을 합병할 리스트 끝에 삽입 
            right_index += 1 # 오른쪽 리스트 인덱스를 1 늘린다.
            
    merged_list.extend(L_left[left_index:]) # 나머지 값을 합병할 리스트의 끝에 붙여준다.
    merged_list.extend(L_right[right_index:]) # 나머지 값을 합병할 리스트의 끝에 붙여준다.
        
    return merged_list # 합병 완료된 리스트를 반환 해준다.

def mergeSort(L): # 합병 정렬을 수행할 함수
    if len(L) < 2: # 정렬될 리스트가 크기가 1인 경우 
        return L # 바로 L을 반환해준다
    
    L_left,L_right = L[:len(L)//2],L[len(L)//2:] # 리스트의 왼쪽과 오른쪽으로 나눈다
    L_ = mergeSort(L_left) # 나눠진 왼쪽의 리스트를 재귀적으로 함수 호출하여 합병 정렬한다
    R_ = mergeSort(L_right) # 나눠진 오른쪽의 리스트를 재귀적으로 함수 호출하여 합병 정렬한다
    return _merge(L_,R_) # 합병정렬을 한 두 리스트를 합병하여 반환한다.
        
# 메인함수 부분 - 합병정렬의 성능을 판별한다.
while True:
    print("\nPerformance test of merge sorting algorithm")
    size = int(input("Input size of random list L (0 to quit) = "))
    if size == 0:
        break
    L = genBigRandList(size)
    # testing MergeSorting
    print("\nBefore mergeSort of L :")
    printListSample(L, 10, 2)
    t1 = time.time()
    sorted_L = mergeSort(L)
    t2 = time.time()
    print("After mergeSort of L :")
    printListSample(sorted_L, 10, 2)
    time_elapsed = t2 - t1
    print("Merge sorting took {} sec".format(time_elapsed))
