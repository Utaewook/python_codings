
# 파일명: MySortings.py
# 작성자: 유태욱
# 작성일자: 2022-10-04
# 주요기능: 리스트 정렬 함수 구현한 모듈
# 최종수정일자: 2022-10-04
# 수정내용: 합병정렬 추가 구현

def selectionSort(L): # 선택정렬을 수행하는 함수
    for i in range(len(L) - 1): # 
        minimun = i
        for j in range(i + 1, len(L)):
            if L[j] < L[minimun]:
                minimun = j
        L[i],L[minimun] = L[minimun],L[i]
    
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