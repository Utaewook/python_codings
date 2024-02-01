
# 파일명: hw4_3.py
# 작성자: 유태욱
# 작성일자: 2022-09-23
# 주요기능: 집합과 딕셔너리를 사용한 정보 검색
# 최종수정일자: 2022-09-23
# 수정내용: 최초작성

input_data = {} # 문자열 자료형으로 나라-수도 데이터를 저장할 변수 선언

while True: # 데이터를 입력받기 위한 반복문
    inputs = input("Input nation and its capital (. to quit) : ").split() # 국가 및 수도 정보를 입력받아 inputs 변수에 split해서 저장
    if inputs == '.' or len(input_data) == 10: # 종료 시그널인 . 가 입력이되거나 10개의 정보가 입력되는 경우
        break # 입력받는 반복문을 빠져나간다.
    input_data[inputs[0]] = inputs[1] # 입력받은 정보를 키: 국가 / 값: 수도 형식으로 딕셔너리에 저장

print(input_data) # 저장된 정보 확인차 출력

while True: # 국가 데이터를 입력받아 수도를 출력하는 반복문
    nation = input("Input nation to find its capital (. to quit) : ") # 국가 데이터를 입력받아 nation 변수에 저장
    if nation == '.': # 만약 입력된 정보가 . (종료시그널)인 경우
        break # 반복문을 종료한다.
    if nation in input_data.keys(): # 입력받은 데이터(국가)가 딕셔너리에 키값으로 존재하는경우
        print(f"The capital of {nation} is {input_data[nation]}") # 해당 정보를 출력한다.
    else: # 입력받은 국가가 저장되지 않은 정보인 경우
        print("There is no data.") # 데이터가 존재하지 않음을 알리는 문장 출력