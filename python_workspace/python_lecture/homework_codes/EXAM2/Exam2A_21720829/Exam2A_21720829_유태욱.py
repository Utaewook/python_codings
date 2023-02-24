# 파일명: Exam2A_21720829_유태욱.py
# 작성자: 유태욱
# 작성일자: 2022-12-11
# 주요기능: 파일에서 행렬 데이터를 읽어와 연산하는 프로그램 구현
# 최종수정일자: 2022-12-11
# 수정내용: 최초작성
import Class_Mtrx as MyMtrx

def fget_MtrxData(fin):  # 파일에서 행렬 데이터를 읽어오는 함수
    row, col = map(int, fin.readline().split())  # 행렬의 각 첫 줄의 행과 열을 입력 받아 저장한다.
    l_data = list()  # 파일에서 읽어온 행렬 데이터를 저장하기 위한 배열 선언
    for _ in range(row):  # 열의 갯수만큼 line을 읽기 위한 반복문
        l_data += list(map(float, fin.readline().split()))  # 읽어온 한 line을 split한 다음, float으로 매핑한 리스트를 l_data에 추가해준다.
    return row, col, l_data  # 파일에서 입력 받은 값으로 Mtrx 객체를 반환한다.

# 메인 프로그램 함수
if __name__ == "__main__":
    print("2022-2 Exam2A 학번: 21720829, 성명: 유태욱")
    fin = open("matrix_data.txt", "r")
    n_row, n_col, f_data_lst = fget_MtrxData(fin)
    mA = MyMtrx.Mtrx("mA", n_row, n_col, f_data_lst)
    print(mA)
    n_row, n_col, f_data_lst = fget_MtrxData(fin)
    mB = MyMtrx.Mtrx("mB", n_row, n_col, f_data_lst)
    print(mB)
    n_row, n_col, f_data_lst = fget_MtrxData(fin)
    mC = MyMtrx.Mtrx("mC", n_row, n_col, f_data_lst)
    fin.close()
    print(mC)
    mD = mA + mB
    mD.set_name("mD = mA + mB"); print(mD)
    mE = mA - mB
    mE.set_name("mE = mA - mB"); print(mE)
    mF = mA * mC
    mF.set_name("mF = mA * mC"); print(mF)
    mG = mA.transpose()
    mG.set_name("mG = mA.transpose()"); print(mG)