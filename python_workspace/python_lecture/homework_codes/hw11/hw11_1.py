# 파일명: hw11_1.py
# 작성자: 유태욱
# 작성일자: 2022-11-16
# 주요기능: 학생 정보 레코드의 Hashmap 탐색 프로그램
# 최종수정일자: 2022-11-16
# 수정내용: 최초작성

import myHashMap  # myHashMap을 사용하기위한 import

if __name__ == "__main__":  # 메인 함수
    HashMap_Capacity = 7  # HashMap의 크기를 7로 설정한다.
    print("Creating a HashMap of capacity ({})".format(HashMap_Capacity))  # 설정한 HashMap의 크기를 출력
    hsMap = myHashMap.HashMap(capacity=HashMap_Capacity)  # HashMap을 생성한다.
    Entries = [("Kim", 19345, "ICE", 4.0), ("Park", 18234, "CS", 4.2), ("Hong", 20456, "EE", 3.9),("Lee", 20987, "ME", 3.8), ("Yoon", 21654, "ICE", 3.7), ("Moon", 21001, "CHEM", 4.1),("Hwang", 21123, "CE", 3.7), ("Choi", 19003, "EE", 4.3), ("Yeo", 20234, "ME", 3.8),("Jeong", 18005, "PH", 4.3)]  # 데이터 준비
    for i in range(len(Entries)): # 준비해둔 데이터를 순회하는 반복문
        entry = Entries[i]  # i번째 데이터를 가져온다
        key = entry[0]  # 데이터의 0번째 값을 키로 가져온다(이름)
        hsMap._setitem(key, entry)  # HashMap에 데이터를 삽입한다.
        print("Entry[{:2}] : {}".format(i, Entries[i]))  # 삽입 결과를 출력한다.
    print("Current HashMap Internal Structure:\n", hsMap, sep='')  # HashMap의 구조를 출력한다.

    print("Checking entry searching in HashMap")
    while True:  # 무한 루프
        key = input("Input student name to search (. to quit) : ")  # HashMap에서 검색을 위한 key를 입력받는다.
        if key == '.':  # 입력값이 '.'이라면
            break  # 루프문을 빠져나간다
        v = hsMap._getitem(key)  # HashMap에 key를 넣어 value값을 가져온다.
        if v == None:  # 가져온 value값이 None이라면
            print("key ({}) is not found in hashmap !!".format(key))  # key값이 HashMap에 존재하지 않음을 알린다
        else:  # 그 외의 경우
            print("key ({}) : Value ({})".format(key, v))  # key값과 key값을 통해 찾은 value값을 출력한다.