# 파일명: Class_Mtrx.py
# 작성자: 유태욱
# 작성일자: 2022-10-23
# 주요기능: 행렬의 생성 및 연산에 사용 할 수 있는 행렬 클래스 구현
# 최종수정일자: 2022-10-23
# 수정내용: 최초작성

class Mtrx:
    def __init__(self, name, n_row, n_col, L_data):  # 행렬 객체의 생성자
        self.name = None  # 이름 변수 초기화
        self.set_name(name)  # 내부 메소드로 이름 지정(정상 범위 검사)
        self.n_row = n_row  # 열 변수 지정
        self.n_col = n_col  # 행 변수 지정
        self.L_data = L_data  # 1차원 리스트 변수 지정
        self.mat_data = [[L_data[i + n_col * j] for i in range(self.n_col)] for j in range(self.n_row)]  # 편리한 행렬 계산을 위한 2차원 배열로 변경

    def set_name(self, name):  # 행렬 객체 이름 변경자
        if isinstance(name, str):  # 이름이 문자열인경우
            self.name = name  # 해당 객체 이름을 매개 변수 값으로 변경한다.
        else:  # 그 외의 경우
            self.name = None  # None 지정

    def __str__(self):  # 행렬의 출력을 위한 문자열 반환
        s = f'{self.name} = \n'  # 초기 문자열 "[행렬_이름] = \n" 꼴 초기화
        for i in range(self.n_row):  # 행렬 열의 갯수 만큼 반복하는 반복문
            for j in range(self.n_col):  # 행렬 행의 갯수 만큼 반복하는 반복문
                s += '%5.2f' % self.mat_data[i][j]  # 인덱스에 맞는 행렬의 값을 소수점 둘째자리까지 맞추어 초기 문자열에 더해준다.
            s += '\n'  # 하나의 열이 모두 더해졌다면 개행 추가로 열을 구분해준다
        return s  # 반복문이 모두 끝난 후 문자열 반환

    def __add__(self, other):  # operator overloading of '+'
        data = []  # 행렬 덧셈의 값을 저장하기 위한 리스트 변수 초기화
        for i in range(self.n_row):  # 열의 갯수 만큼 반복하는 반복문
            for j in range(self.n_col):  # 행의 갯수 만큼 반복하는 반복문
                data.append(self.mat_data[i][j] + other.mat_data[i][j])  # 리스트 변수에 각 인덱스에 해당하는 행렬 값 덧셈의 결과를 저장
        return Mtrx(self.name, self.n_row, self.n_col, data)  # 결과가 저장된 행렬 객체 반환

    def __sub__(self, other):  # operator overloading of '-'
        data = []  # 행렬 덧셈의 값을 저장하기 위한 리스트 변수 초기화
        for i in range(self.n_row):  # 열의 갯수 만큼 반복하는 반복문
            for j in range(self.n_col):  # 행의 갯수 만큼 반복하는 반복문
                data.append(self.mat_data[i][j] - other.mat_data[i][j])  # 리스트 변수에 각 인덱스에 해당하는 행렬 값 뺄셈의 결과를 저장
        return Mtrx(self.name, self.n_row, self.n_col, data)  # 결과가 저장된 행렬 객체 반환

    def __mul__(self, other):   # operator overloading of '*'
        data = [[0 for _ in range(other.n_col)] for _ in range(self.n_row)]  # 행렬의 행과 열의 갯수에 맞게 0으로 초기화 된 새로운 행렬 생성
        for row in range(self.n_row):  # 첫번째 행렬의 열의 갯수 만큼 반복
            for i in range(other.n_col):  # 두번째 행렬의 행의 갯수 만큼 반복
                for j in range(self.n_col):  # 두번째 행렬의 열의 갯수 만큼 반복
                    data[row][i] += self.mat_data[row][j] * other.mat_data[j][i]  # 행렬 곱셈값을 누적시켜 저장

        return Mtrx(self.name, len(data), len(data[0]), sum(data, []))  # 계산 완료된 행렬을 1차원 배열로 만들어 Mtrx객체로 만들어서 반환한다.
    
    def transpose(self):  # returns transposed matrix
        temp = [[0 for _ in range(self.n_row)] for _ in range(self.n_col)]  # 전치된 행렬의 값을 저장하기 위한 임시 배열을 self 행렬의 행과 열이 교환된 배열로 생성한다.
        for i in range(self.n_row):  # i를 row의 값 만큼 반복하게하는 반복문
            for j in range(self.n_col):  # j를 col의 값 만큼 반복하게 하는 반복문
                temp[j][i] = self.mat_data[i][j]  # 인덱스의 값이 바뀐 행렬의 위치로 전치된 값을 넣어준다
        return Mtrx(self.name, len(temp), len(temp[0]), sum(temp, []))  # 전치된 행렬을 Mtrx 객체에 넣어서 반환한다.