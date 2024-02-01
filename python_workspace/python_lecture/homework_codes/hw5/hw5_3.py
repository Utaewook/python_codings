
# 파일명: hw5_3.py
# 작성자: 유태욱
# 작성일자: 2022-10-01
# 주요기능: 피보나치 수열을 계산하는 동적 프로그래밍 작성 및 성능 측정
# 최종수정일자: 2022-10-01
# 수정내용: 최초작성

import time
memo = dict() # 동적프로그래밍을 위한 dictionary 변수
def dynFibo(n): # recursive calculation with memoization
    if n == 1 or n == 0: # n이 0이나 1인 경우
        memo[n] = n # memo 변수에 n을 저장한다.
    if n not in memo.keys(): # n이 memo에 저장되지 않은 값이라면
        memo[n] = dynFibo(n - 1) + dynFibo(n - 2) # 재귀적으로 함수를 호출하여 memo값을 계산하여 저장한다
    return memo[n] # memo에 저장된 값으로 반환한다.

# (Application)
(start, stop, step) = tuple(map(int,input("input start, stop, step of Fibonacci series : ").split(' ')))
for n in range(start, stop+1, step):
    t1 = time.time()
    fibo_n = dynFibo(n)# dynFibo() 호출 및 경과시간 측정
    t_elapse_us = time.time() - t1
    print("dynFibo({:3d}) = {:25d}, took {:10.2f}[micro_sec]".format(n, fibo_n, t_elapse_us))