
# 파일명: hw6_3.py
# 작성자: 유태욱
# 작성일자: 2022-10-04
# 주요기능: 사용자 정의 패키지를 이용한 행렬 계산
# 최종수정일자: 2022-10-04
# 수정내용: 최초작성

# HW 6.3 Testing user‐defined module MyMatrix
import random, time, sys 
sys.path.append("C:/MyPyPackage/myPyModules") 
import MyMatrix

A = [[1,2,3,4], [5,6,7,8], [9,10,0,1]]
B = [[1,0,0,0], [0,1,0,0], [0,0,1,1]]
C = [[1,0,0], [0,1,0], [0,0,1], [0,0,0]]
MyMatrix.printMtrx("A", A) 
MyMatrix.printMtrx("B", B) 
MyMatrix.printMtrx("C", C)
D = MyMatrix.addMtrx(A, B) 
MyMatrix.printMtrx("A + B", D)
E = MyMatrix.subMtrx(A, B)
MyMatrix.printMtrx("A ‐ B", E)
F = MyMatrix.mulMtrx(A, C)
MyMatrix.printMtrx("A * C", F)