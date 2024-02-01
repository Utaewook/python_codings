
# 파일명: hw3_2.py
# 작성자: 유태욱
# 작성일자: 2022-09-15
# 주요기능: 연 월 일 입력 후, 1년 1월 1일부터 몇 번째 날짜, 요일 인지 출력( 0 0 0 까지 반복)
# 최종수정일자: 2022-09-19
# 수정내용: 오류 수정(누적 일자 계산)


# 요일 계산을 위한 dictionary 변수 - 누적 일수에 7을 나눈 나머지를 key값으로 함
week_day = {1: "MON", # 월요일
            2: "TUE", # 화요일
            3: "WED", # 수요일
            4: "THR", # 목요일
            5: "FRI", # 금요일
            6: "SAT", # 토요일
            0: "SUN"} # 일요일

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
    
while True: # 프로그램 입력, 출력 반복될 반복문
    year, month, day = map(int,input("input year month day : ").split()) # 연도, 월, 날짜 정수형으로 입력
    if year < 0 or month < 0 or month > 12 or day < 0 or day > 31: # 잘못된 입력시 반복문을 건너뛰기 위한 조건문
        print("invalid value input") # 잘못된 입력임을 명시
        continue # 반복문 재시작
    print(f"Input yr_mn_dy_strings : {list(map(str,[year,month,day]))}") # 입력받은 연도, 월, 날짜 형식에 맞게 출력
    if year == month == day == 0: # 종료 조건인 연도, 월, 날짜가 모두 0인 경우
        break # 반복문 종료
    else: # 종료 조건이 아닌경우
        elapsed_day = 0 # 누적 일수 변수 초기화
        if is_leap(year): # 해당 연도가 윤년인 경우
            if month == 1: # 입력받은 월이 1월인 경우
                elapsed_day = 365 * (year - 1) + how_many_leapYear(year) + day # 누적 일수 계산 = 연도 * 365일 + 윤년 개수만큼의 일수 + 입력받은 일수
            else: # 그 외의 경우
                elapsed_day = 365 * (year - 1) + how_many_leapYear(year) + sum(leap_months[:month-1]) + day # 누적 일수 계산 = 연도 * 365일 + 윤년 개수만큼의 일수 + 개월수-1 까지의 일수 합 + 입력받은 일수
        else: # 해당 연도가 평년인 경우
            if month == 1: # 입력 받은 월이 1월인 경우
                elapsed_day = 365 * (year - 1) + how_many_leapYear(year) + day # 누적 일수 계산 = 연도 * 365일 + 윤년 개수만큼의 일수 + 입력받은 일수
            else: # 그 외의 경우
                elapsed_day = 365 * (year - 1) + how_many_leapYear(year) + sum(months[:month-1]) + day # 누적 일수 계산 = 연도 * 365일 + 윤년 개수만큼의 일수 + 개월수-1 까지의 일수 합 + 입력받은 일수
        print(f"Day (year({year}), month({month}), day({day})) : week_day ({week_day[elapsed_day%7]}), elapsed {elapsed_day} days from Jan01AD01") # 계산된 누적 일수를 통해 요일과 누적 일수 출력