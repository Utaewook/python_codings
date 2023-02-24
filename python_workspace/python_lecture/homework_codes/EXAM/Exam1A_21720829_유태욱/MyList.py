from math import sqrt # 표준편차값을 구하기 위한 math 모듈의 sqrt 함수 import


def get_float_data():  # 표준 입력으로부터 실수형 데이터를 한 줄에 입력받아 반환하는 함수
    L = list(map(float,input("Input float data in a line : ").split()))  # 표준입력으로 입력받은 string값 split한 후, map 함수를 통해 각각의 값을 float 값으로 변경해 준뒤, list()함수를 통해 배열로 저장한다.
    return L # 저장된 실수형 배열을 반환한다.
    

def get_statistics(L):  # 전달된 리스트에 포함된 데이터의 통계 분석값 반환
    L_len = len(L)  # 리스트의 길이를 내부 함수로 구함
    L_min = min(L)  # 리스트의 최소값을 내부 함수로 구함
    L_max = max(L)  # 리스트의 최댓값을 내부 함수로 구함
    L_avg = sum(L)/L_len  # 리스트의 평균값을 미리 구한 리스트의 길이와 내부 함수로 구함
    
    s = 0  # 평균과 각 값을 뺀 것의 제곱 값을 모두 누적으로 더해주기 위한 변수
    for val in L:  # 리스트의 값을 순회 하는 반복문
        s += (val - L_avg)**2  # 평균과 순회하는 리스트의 값을 뺀 후, 제곱을 한 값을 누적 시켜준다
    L_var = s/L_len  # 위의 반복문을 통해 구한 값을 리스트의 길이 만큼 나누어 구한 리스트의 분산
    L_std = sqrt(L_var)  # 리스트의 표준편차를 sqrt함수와 분산 값을 통해 구함
    
    return  (L_len, L_min, L_max, L_avg, L_var, L_std)  # 구한 값들 반환


def sort_list(L):  # 선택정렬을 수행하는 함수
    f_list = L.copy()  # 리스트의 값을 복사한 사본을 만든다
    for i in range(len(f_list)):  # 0부터 리스트의 길이 만큼 반복하는 반복문
        min_idx = i  # 최소값의 인덱스를 현재 인덱스값으로 정한다.
        for j in range(i,len(f_list)):  # i 부터 리스트의 길이 만큼 반복하는 반복문
            if f_list[min_idx] > f_list[j]:  # 현재 최소값 인덱스의 값보다 작은 값이 나오면
                min_idx = j  # 최소값 인덱스를 현재 j 값으로 변경해준다.
        if min_idx != i: # 만약 최소값 인덱스와 i값과 서로 같지않다면
            f_list[min_idx],f_list[i] = f_list[i],f_list[min_idx] # 두 값을 swap 해준다.
        
    return f_list  # 정렬된 사본 반환