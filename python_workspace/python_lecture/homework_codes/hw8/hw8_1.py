# 파일명: hw8_1.py
# 작성자: 유태욱
# 작성일자: 2022-11-01
# 주요기능: 학생 점수 파일 입출력 구현
# 최종수정일자: 2022-11-01
# 수정내용: 최초작성

f = open('student_records.txt','r')  # 입력 파일 열기
f_output = open('output.txt','w')  # 출력 파일 열기
data = []  # 학생 정보를 담을 data 리스트 변수 선언
while True:  # 입력 파일에서 데이터를 반복적으로 입력받게할 반복문
    line = f.readline()  # 1라인을 읽어 line에 저장한다.
    if not line:  # 입력된 값이 없다면
        break  # 반복문 종료
    list_data = list(line.split())  # line의 값을 split해서 배열로 만들어 저장한다.
    score_data = list(map(int,list_data[1:]))  # 이름 외의 점수 값이 포함된 리스트의 부분을 int로 매핑하여 저장한다.
    list_data = [list_data[0]]+score_data  # 이름과 int로 변환된 점수를 합쳐 리스트에 저장한다.
    list_data += [sum(score_data),sum(score_data)/4]  # 저장된 리스트의 끝에 총점, 평균값 또한 미리 계산하여 저장해 둔다.
    data.append(list_data)  # 계산된 학생 데이터를 data 리스트에 넣어준다.

for student in data:  # data 내의 student를 순회하며 출력하기 위한 반복문
    print(student[:5])  # 계산 되기 전의 각 학생의 점수까지만 출력

print('\nAfter calculate_scores(students)')  # 총점과 평균이 계산된 데이터 출력
print('='*38)  # 쌍 구분선 출력
print('name : kor  eng  math  sci  sum  avg')  # 각 행 이름 출력
f_output.write('name : kor  eng  math  sci  sum  avg\n')  # 각 행의 이름 출력 파일에 적기
print('-'*38)  # 구분선 출력
f_output.write('-'*38+'\n')  # 구분선 출력 파일에 적기

avgs = [0] * 4  # 평균값 저장을 위한 리스트 변수 선언
for student in data:  # data 내의 student를 순회하며 출력하기 위한 반복문
    out_str = f"{student[0]:<5}:{student[1]:4d},{student[2]:4d},{student[3]:4d},{student[4]:4d},{student[5]:4d},  {student[6]:.2f}"  # 출력 될 문자열을 형식에 맞추어 만들어둔다.
    print(out_str)  # 만들어둔 출력 문자열을 표준 출력으로 print한다.
    f_output.write(out_str+'\n')  # 만들어둔 출력 문자열을 출력 파일에 적는다.
    # 순회하면서 평균값 또한 계산해서 저장해준다.
    avgs[0] += student[1]/len(data)  # 국어 과목의 점수에 학생수(len(data)) 만큼 나누어 평균 값에 더해준다.
    avgs[1] += student[2]/len(data)  # 영어 과목의 점수에 학생수(len(data)) 만큼 나누어 평균 값에 더해준다.
    avgs[2] += student[3]/len(data)  # 수학 과목의 점수에 학생수(len(data)) 만큼 나누어 평균 값에 더해준다.
    avgs[3] += student[4]/len(data)  # 과학 과목의 점수에 학생수(len(data)) 만큼 나누어 평균 값에 더해준다.

print('=' * 38)  # 쌍 구분선 출력

print('\nAverage score of each class :')  # 각 과목의 평균 점수 출력
print(f'Kor_avg  = {avgs[0]:.2f}')  # 계산해 둔 국어 과목 평균 점수 출력
print(f'Eng_avg  = {avgs[1]:.2f}')  # 계산해 둔 영어 과목 평균 점수 출력
print(f'Math_avg = {avgs[2]:.2f}')  # 계산해 둔 수학 과목 평균 점수 출력
print(f'Sci_avg  = {avgs[3]:.2f}')  # 계산해 둔 과학 과목 평균 점수 출력


f.close()  # 입력 파일 닫기
f_output.close()  # 출력 파일 닫기