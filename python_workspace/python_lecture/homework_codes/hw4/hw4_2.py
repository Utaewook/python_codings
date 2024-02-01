
# 파일명: hw4_2.py
# 작성자: 유태욱
# 작성일자: 2022-09-23
# 주요기능: 튜플로 표현되는 학생 정보를 표준 입력장치로 부터 10개 입력하여 리스트에 포함한 후, 오름차순으로 정렬하는 파이썬 프로그램
# 최종수정일자: 2022-09-23
# 수정내용: 최초작성

input_data = [] # 입력 데이터를 저장할 리스트 변수

input_data.append(("Kim, S.C.", 12001234, "CE", 4.10)) # 학생데이터 1 입력
input_data.append(("Choi, Y.B.", 119003234, "EE", 3.78)) # 학생데이터 2 입력
input_data.append(("Hong, C.H.", 21001542, "ICE", 4.13)) # 학생데이터 3 입력
input_data.append(("Yoon, J.H.", 17002571, "ME", 3.55)) # 학생데이터 4 입력
input_data.append(("Lee, S.H.", 20003257, "ICE", 4.45)) # 학생데이터 5 입력
input_data.append(("Kim, H.Y.", 19001234, "CE", 4.17)) # 학생데이터 6 입력
input_data.append(("Lee, J.K.", 18003234, "EE", 3.78)) # 학생데이터 7 입력
input_data.append(("Park, S.Y.", 21001643, "ICE", 4.13)) # 학생데이터 8 입력
input_data.append(("Jang, S.H.", 19002567, "ME", 3.35)) # 학생데이터 9 입력
input_data.append(("Yeo, C.S.", 20005243, "CE", 4.45)) # 학생데이터10 입력
    
for i in range(10): # 학생데이터 준비 결과 출력 반복문
    print(f"students[{i:2d}] : name({input_data[i][0]}), st_id({input_data[i][1]}), major({input_data[i][2]} , GPA ( {input_data[i][3]:.2f}))") # f string을 통해 형식 맞추어 학생데이터 출력
    
input_data.sort()

print("\nAfter sorting in increasing order :") # 정렬된 후 학생데이터 출력 구분 문장
for i in range(10): # 학생데이터 출력 반복문
    print(f"students[{i:2d}] : name({input_data[i][0]}), st_id({input_data[i][1]}), major({input_data[i][2]} , GPA ( {input_data[i][3]:.2f}))") # f string을 통해 형식 맞추어 학생데이터 출력

input_data.sort(key=lambda x:x[3],reverse=True)
print("\nAfter sorting according to GPA in decreasing order :") # 학점 기준 역순 정렬된 후 학생데이터 출력 구분 문장
for i in range(10): # 학생데이터 출력 반복문
    print(f"students[{i:2d}] : name({input_data[i][0]}), st_id({input_data[i][1]}), major({input_data[i][2]} , GPA ( {input_data[i][3]:.2f}))") # f string을 통해 형식 맞추어 학생데이터 출력
