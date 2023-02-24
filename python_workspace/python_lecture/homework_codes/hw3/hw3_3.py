
# 파일명: hw3_3.py
# 작성자: 유태욱
# 작성일자: 2022-09-20
# 주요기능: 날짜를 나타내는 연 월 일의 3 개 정수를 입력 받고, 해당 달의 달력을 출력
# 최종수정일자: 2022-09-20
# 수정내용: 오류 수정(누적 일자 계산)

# 요일 계산을 위한 dictionary 변수 - 누적 일수에 7을 나눈 나머지를 key값으로 함
week_day = {1: "MON", # 월요일
            2: "TUE", # 화요일
            3: "WED", # 수요일
            4: "THR", # 목요일
            5: "FRI", # 금요일
            6: "SAT", # 토요일
            0: "SUN"} # 일요일

# 월 이름 출력을 위한 dictionary 변수
month_name = {1: "January", # 1월
              2: "February", # 2월
              3: "March", # 3월
              4: "April", # 4월
              5: "May", # 5월
              6: "June", # 6월
              7: "July", # 7월
              8: "August", # 8월
              9: "September", # 9월
              10: "October", # 10월
              11: "November", # 11월
              12: "December"} # 12월

# 월 누적 일수를 합하기 위한 list 변수
leap_months = [31,29,31,30,31,30,31,31,30,31,30,31] # 윤년의 경우
months = [31,28,31,30,31,30,31,31,30,31,30,31] # 평년의 경우

def is_leap(year): # 매개변수로 입력받은 연도가 윤년인지 반환하는 함수
    if year%4 == 0: # 연도가 4로 나누어지면서,
        if year%400 != 0 and year%100 == 0: # 연도가 400으로 나누어 떨어지지 않으며 100으로는 나누어 떨어지는 경우
            return False # 윤년이 아님을 반환
        else: # 그 외의 경우에는 윤년임을 반환함
            return True
    else: # 연도가 4로 나누어지지 않는 경우엔
       return False # 윤년이 아님을 반환한다.
        
def how_many_leapYear(year): # 매개변수로 입력받은 연도 전까지 윤년의 갯수를 반환하는 함수
    sum = 0 # 합계 변수 초기화
    for y in range(1,year): # 1~ 입력받은 연도 - 1 년 까지 반복문
        if is_leap(y): sum += 1 # 해당 연도가 윤년이면 합계에 누적
    return sum # 합계 출력

def week_day_calculate(year, month): # 요일을 구하기 위한 함수
    elapsed_day = 0 # 누적 일수 변수 초기화
    if is_leap(year): # 해당 연도가 윤년인 경우
        if month == 1: # 입력받은 월이 1월인 경우
            elapsed_day = 365 * (year - 1) + how_many_leapYear(year) + 1 # 누적 일수 계산 = 연도 * 365일 + 윤년 개수만큼의 일수 + 1
        else: # 그 외의 경우
            elapsed_day = 365 * (year - 1) + how_many_leapYear(year) + sum(leap_months[:month-1]) + 1 # 누적 일수 계산 = 연도 * 365일 + 윤년 개수만큼의 일수 + 개월수-1 까지의 일수 합 + 1
    else: # 해당 연도가 평년인 경우
        if month == 1: # 입력 받은 월이 1월인 경우
            elapsed_day = 365 * (year - 1) + how_many_leapYear(year) + 1 # 누적 일수 계산 = 연도 * 365일 + 윤년 개수만큼의 일수 + 1
        else: # 그 외의 경우
            elapsed_day = 365 * (year - 1) + how_many_leapYear(year) + sum(months[:month-1]) + 1 # 누적 일수 계산 = 연도 * 365일 + 윤년 개수만큼의 일수 + 개월수-1 까지의 일수 합 + 1
    return elapsed_day%7 # 요일 반환

year, month, day = map(int,input("input year month day : ").split()) # 연도, 월, 날짜 정수형으로 입력

print(f"\n{month_name[month]} of Year {year}") # 입력받은 연도와 월 출력
print("="*28) # 구분선 "=" 출력
for d in range(7): # 요일 출력을 위한 반복문
    print(f" {week_day[d]}",end="") # week_day에 저장된 값의 value를 출력
    
print("\n"+"-"*28) # 구분선 "-" 출력

selected_month = 0 # 달력에 표시될 일수 선택
if is_leap(year) and month == 2: # 윤년이며 해당 월이 2월인 경우
    selected_month = leap_months[1] # 윤년의 2월인 29일 저장
else: # 그 외의 경우
    selected_month = months[month-1] # 해당 월에 맞는 일수 저장


week_loop = week_day_calculate(year,month) # 함수를 통해 계산된 요일 저장
day_count = 1 # 날짜 오름차순 출력을 위한 변수
print("    " * week_loop, end='') # 월 초 1일 전까지의 공백 출력
while True: # 1일 ~ 월 말 까지의 출력 반복문
    if day_count > selected_month: # 선택된 월의 날짜 만큼 출력을 완료하면
        print() # 줄바꿈을 해준다음
        break # 반복문을 종료한다
    if week_loop == 6: # 토요일(하나의 열에 출력될 마지막 요일)이 되면
        print("%4d"%day_count) # 날짜를 출력하고 줄바꿈을 한 다음
        week_loop = 0 # 요일을 일요일로 초기화 한다
    else: # 그 외의 요일의 경우에는
        print("%4d"%day_count,end='') # 날짜를 출력하고 한칸 띄운다
        week_loop += 1 # 요일을 하나 증가 시켜준다
    day_count += 1 # 날짜를 1 증가 시킨다
        
print("="*28) # 구분선 "=" 출력