# 파일명: hw10_3.py
# 작성자: 유태욱
# 작성일자: 2022-11-15
# 주요기능: 정규분포함수 특성 분석 프로그램
# 최종수정일자: 2022-11-15
# 수정내용: 최초작성

import numpy as np  # numpy 모듈을 사용하기 위한 import
import matplotlib.pyplot as plt  # matplot 모듈의 pyplot을 사용하기 위한 import


def gauss(mu, sigma, X):  # 정규분포값을 계산하여 반환 해주는 함수
    Y = [1.0 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((X[i] - mu) ** 2) / (2 * sigma ** 2)) for i in range(len(X))]  # X 리스트의 각 값에 정규분포화한 값을 Y리스트로 만들어준다.
    return Y  # 정규분포로 만든 리스트를 반환


if __name__ == "__main__":  # 메인 함수인 경우
    list_X = np.linspace(-8, 8, num=100)  # -8부터 8까지 100개의 등 간격으로 나누는 리스트 생성
    sigma_half = gauss(0, 0.5, list_X)  # 평균 = 0 이고 표준편차가 0.5인 정규분포 생성
    sigma_one = gauss(0, 1, list_X)  # 평균 = 0 이고 표준편차가 1인 정규분포 생성
    sigma_two = gauss(0, 2, list_X)  # 평균 = 0 이고 표준편차가 2인 정규분포 생성

    plt.figure(1)  # 첫 번째 창(표준편차 비교) 생성
    plt.plot(list_X, sigma_half, color='red', label="sigma=0.5")  # 평균 = 0 이고 표준편차가 0.5인 정규분포곡선 그래프에 추가
    plt.plot(list_X, sigma_one, color='blue', label="sigma=1")  # 평균 = 0 이고 표준편차가 1인 정규분포곡선 그래프에 추가
    plt.plot(list_X, sigma_two, color='green', label="sigma=2")  # 평균 = 0 이고 표준편차가 2인 정규분포곡선 그래프에 추가

    plt.title("Normal Distribution Graph 1 - mu = 0.0, sigma = [0.5, 1, 2]")  # 첫 번째 창 제목 설정
    plt.legend(loc="best")  # 범례 표시 및 위치 지정
    plt.grid(True)  # 격자 표시

    mu_minus_2 = gauss(-2, 1, list_X)  # 평균 = -2 이고 표준편차가 1인 정규분포 생성
    mu_0 = gauss(0, 1, list_X)  # 평균 = 0 이고 표준편차가 1인 정규분포 생성
    mu_plus_2 = gauss(2, 1, list_X)  # 평균 = 2 이고 표준편차가 1인 정규분포 생성

    plt.figure(2)  # 두 번째 창(평균 비교) 생성
    plt.plot(list_X, mu_minus_2, color='red', label='mu=-2')
    plt.plot(list_X, mu_0, color='blue', label='mu=0')
    plt.plot(list_X, mu_plus_2, color='green', label='mu=2')

    plt.title("Normal Distribution Graph 2 - mu = [-2.0, 0.0, 2.0], sigma = 1")  # 두 번째 창 제목 설정
    plt.legend(loc="best")   # 범례 표시 및 위치 지정
    plt.grid(True)  # 격자 표시
    plt.show()  # plt 창 화면에 띄우기
