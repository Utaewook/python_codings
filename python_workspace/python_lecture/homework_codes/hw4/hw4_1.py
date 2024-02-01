
# 파일명: hw4_1.py
# 작성자: 유태욱
# 작성일자: 2022-09-22
# 주요기능: 
# 최종수정일자: 2022-09-22
# 수정내용: 최초작성

input_data = []
print("Input 10 dates in (year month day) format : ")

for _ in range(10):
    input_data.append(tuple(map(int, input("input year, month, day : ").split())))
    print("L_dates =",input_data,sep=' ')

print("After input of 10 dates :",input_data,sep=' ')
input_data.sort()
print("After sorting, L_dates =",input_data,sep=' ')