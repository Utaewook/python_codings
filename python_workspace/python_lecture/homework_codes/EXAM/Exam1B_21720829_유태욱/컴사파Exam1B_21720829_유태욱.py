
# 파일명: 컴사파Exam1B_21720829_유태욱.py
# 작성자: 유태욱
# 작성일자: 2022-10-23
# 주요기능: 행렬의 생성 및 연산에 사용 할 수 있는 행렬 클래스 구현 검사를 위한 메인 모듈
# 최종수정일자: 2022-10-23
# 수정내용: 최초작성

# Exam1B - Application of class Mtrx for float data type
from Class_Mtrx import * 
#--------------------------
if __name__ == "__main__":
    print("2022-2 컴사파Exam1B_21720829_유태욱")
    La = [0.0, 1.1, 2.2, 3.3,\
          4.4, 5.5, 6.6, 7.7,\
          8.8, 9.9, 1.5, 2.5]
    Lb = [1.0, 0.0, 0.0, 0.0,\
          0.0, 1.0, 0.0, 0.0,\
          0.0, 0.0, 1.0, 0.0]
    Lc = [1.0, 0.0, 0.0,\
          0.0, 1.0, 0.0,\
          0.0, 0.0, 1.0,\
          0.0, 0.0, 0.0,\
          0.0, 0.0, 0.0]
    mA = Mtrx("mA", 3, 4, La); print(mA)
    mB = Mtrx("mB", 3, 4, Lb); print(mB)
    mC = Mtrx("mC", 4, 3, Lc); print(mC)
    mD = mA + mB; mD.set_name("mD = mA + mB"); print(mD)
    mE = mA - mB; mE.set_name("mE = mA - mB"); print(mE)
    mF = mA * mC; mF.set_name("mF = mA * mC"); print(mF)
    mG = mA.transpose(); mG.set_name("mG = mA.transpose()"); print(mG)