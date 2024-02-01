# 파일명: hw8_3.py
# 작성자: 유태욱
# 작성일자: 2022-11-02
# 주요기능: 엑셀파일에서 읽어온 학생 점수 데이터를 연산 후, 데이터프레임 엑셀로 저장
# 최종수정일자: 2022-11-02
# 수정내용: 최초작성

import pandas as pd  # pandas의 dataframe을 사용하기 위한 import

df = pd.read_excel('student_scores.xlsx', engine='openpyxl')  # 입력 엑셀파일에서 학생 데이터 입력받는다.

print('df = ')  # 데이터 프레임 출력
print(df)  # 초기 데이터 프레임을 출력한다.

print('\navgs_per_class = ')  # 과목별 평균 점수를 출력
print(f"Eng \t{df['Eng'].mean():.2f}")  # dataframe의 mean() 함수를 통해 영어 과목 평균 계산 값 출력
print(f"Kor \t{df['Kor'].mean():.2f}")  # dataframe의 mean() 함수를 통해 국어 과목 평균 계산 값 출력
print(f"Math\t{df['Math'].mean():.2f}")  # dataframe의 mean() 함수를 통해 수학 과목 평균 계산 값 출력
print(f"Sci \t{df['Sci'].mean():.2f}")  # dataframe의 mean() 함수를 통해 과학 과목 평균 계산 값 출력
print(f"Avg \t{df[['Eng','Kor','Math','Sci']].mean().mean():.2f}")    # dataframe의 mean() 함수를 중첩해 모든 과목 평균 계산 값 출력
print('dtype: float64')  # 데이터 타입 출력

df = df.assign(Avg=lambda x:(x['Eng']+x['Kor']+x['Math']+x['Sci'])/4).sort_values(by='Avg',ascending=False)  # 마지막 열에 평균 컬럼을 추가하기 위해 람다함수 이용하여 평균값 계산 후 저장 / 평균값을 기준으로 내림차순 정렬도 수행
# dataframe의 마지막 행에 평균값 행을 추가
df = df.append({'st_id':'NaN',  # 학번 없음으로 저장
                'st_name':"Total_Avg",  # 이름 지정
                'Eng':df['Eng'].mean(),  # mean() 함수로 영어 과목 평균값 저장
                'Kor':df['Kor'].mean(),  # mean() 함수로 국어 과목 평균값 저장
                'Math':df['Math'].mean(),  # mean() 함수로 수학 과목 평균값 저장
                'Sci':df['Sci'].mean(),  # mean() 함수로 과학 과목 평균값 저장
                'Avg':df[['Eng','Kor','Math','Sci']].mean().mean()},ignore_index=True)  # 총 평균값 저장
print("\ndf_sorted_with_avg = ")
print(df)  #  처리가 끝난 dataframe을 출력

print("Writing df to excel file")
df.to_excel('processed_scores.xlsx')  # 연산 후 출력 엑셀파일에 저장
