# 파일명: MyMatrix.py
# 작성자: 유태욱
# 작성일자: 2022-10-04
# 주요기능: 행렬의 합/차/곱 을 계산하는 함수를 포함한 모듈
# 최종수정일자: 2022-10-04
# 수정내용: 최초작성

def printMtrx(name, M): # 행렬을 출력하는 함수
    print(f"{name} = ") # 행렬의 이름을 출력한다.
    for row in range(len(M)): # 행렬의 열의 갯수 만큼 반복
        for col in range(len(M[0])): # 행렬의 행의 갯수 만큼 반복
            if col == (len(M[0]) - 1): # 반복하는 행이 마지막이라면
                print(f"{M[row][col]:3d}") # 개행을 포함하여 출력
            else: # 그외의 경우
                print(f"{M[row][col]:3d}", end='') # 개행 없이 출력
        
def addMtrx(M1, M2): # 두 행렬의 합을 반환하는 함수
    M = [list(0 for _ in range(len(M1[0]))) for _ in range(len(M1))] # 행렬의 행과 열의 갯수에 맞게 0으로 초기화된 새로운 행렬 생성
    for row in range(len(M)): # 행렬의 열의 갯수 만큼 반복
        for col in range(len(M[0])): # 행렬의 행의 갯수 만큼 반복
            M[row][col] = M1[row][col] + M2[row][col] # 각 행과 열에 맞게 덧셈 결과값을 저장
    return M # 계산 완료된 행렬 반환
    

def subMtrx(M1, M2): # 두 행렬의 차를 반환하는 함수
    M = [list(0 for _ in range(len(M1[0]))) for _ in range(len(M1))] # 행렬의 행과 열의 갯수에 맞게 0으로 초기화된 새로운 행렬 생성
    for row in range(len(M)): # 행렬의 열의 갯수만큼 반복
        for col in range(len(M[0])): # 행렬의 행의 갯수만큼 반복
            M[row][col] = M1[row][col] - M2[row][col] # 각 행과 열에 맞게 뺄셈 결과값을 저장
    return M # 계산 완료된 행렬 반환

def mulMtrx(M1, M2): # 두 행렬의 곱을 반환 하는 함수
    M = [list(0 for _ in range(len(M2[0]))) for _ in range(len(M1))] # 행렬의 행과 열의 갯수에 맞게 0으로 초기화 된 새로운 행렬 생성
    for row in range(len(M1)): # 첫번째 행렬의 열의 갯수 만큼 반복
        for i in range(len(M2[0])): # 두번째 행렬의 행의 갯수 만큼 반복
            for j in range(len(M2)): # 두번째 행렬의 열의 갯수 만큼 반복
                M[row][i] += M1[row][j] * M2[j][i] # 행렬 곱셈값을 누적시켜 저장
    return M # 계산 완료된 행렬 반환