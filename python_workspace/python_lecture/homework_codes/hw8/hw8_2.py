# 파일명: hw8_2.py
# 작성자: 유태욱
# 작성일자: 2022-11-01
# 주요기능: 파일에 저장된 행렬 데이터를 입력 받아 처리한 뒤, 출력 값을 출력 파일에 쓰는 프로그램
# 최종수정일자: 2022-11-01
# 수정내용: 최초작성

from Class_Mtrx import Mtrx  # 행렬의 계산을 구현한 Mtrx모듈을 사용하기 위한 import


def fget_MtrxData(fin):  # 파일에서 행렬 데이터를 읽어와 Mtrx 객체로 반환하는 함수
    row, col = map(int, fin.readline().split())  # 행렬의 각 첫 줄의 행과 열을 입력 받아 저장한다.
    l_data = list()  # 파일에서 읽어온 행렬 데이터를 저장하기 위한 배열 선언
    for _ in range(row):  # 열의 갯수만큼 line을 읽기 위한 반복문
        l_data += list(map(float, fin.readline().split()))  # 읽어온 한 line을 split한 다음, float으로 매핑한 리스트를 l_data에 추가해준다.
    return Mtrx(None, row, col, l_data)  # 파일에서 입력 받은 값으로 Mtrx 객체를 반환한다.


if __name__ == '__main__':  # 메인 함수 동작

    # 파일 open 입력받는 파일(f)과 출력할 파일(f_out)을 모두 열어 준다.
    f = open('matrix_data.txt', 'r')  # 읽기 전용으로 open
    f_out = open('result.txt', 'w')  # 쓰기 전용으로 open

    mA = fget_MtrxData(f)  # 첫번째 행렬 데이터 파일에서 읽어온다.
    mA.setName('mA')  # 해당 행렬의 이름을 설정해준다.
    mB = fget_MtrxData(f)  # 두번째 행렬 데이터 파일에서 읽어온다
    mB.setName('mB')  # 해당 행렬의 이름을 설정해준다.
    mC = fget_MtrxData(f)  # 세번째 행렬 데이터 파일에서 읽어온다
    mC.setName('mC')  # 해당 행렬의 이름을 설정해준다.
    mD = mA + mB  # 행렬의 합
    mD.set_name('mD = mA + mB')  # 해당 행렬의 이름을 설정해준다.
    mE = mA - mB  # 행렬의 차
    mE.set_name('mE = mA - mB')  # 해당 행렬의 이름을 설정해준다.
    mF = mA * mC  # 행렬의 곱
    mF.set_name('mF = mA * mC')  # 해당 행렬의 이름을 설정해준다.

    # 출력 부분 각 행렬의 표준출력으로의 print와, 출력 파일으로의 write
    print(mA)
    f_out.write(mA.__str__())
    print(mB)
    f_out.write(mB.__str__())
    print(mC)
    f_out.write(mC.__str__())
    print(mD)
    f_out.write(mD.__str__())
    print(mE)
    f_out.write(mE.__str__())
    print(mF)
    f_out.write(mF.__str__())

    # 사용한 파일을 닫아준다.
    f.close()
    f_out.close()

