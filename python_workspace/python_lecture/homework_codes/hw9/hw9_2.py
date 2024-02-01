# 파일명: hw9_2.py
# 작성자: 유태욱
# 작성일자: 2022-11-07
# 주요기능: gui 환경의 km와 mile을 변환해주는 변환 계산기 프로그램
# 최종수정일자: 2022-11-07
# 수정내용: 최초작성

from tkinter import *  # gui 구성을 위한 tkinter 모듈 import

def km_to_mile():  # km를 mile로 바꾸는 버튼의 command 함수
    if entry_km.get().isnumeric():  # entry_km의 입력 값이 숫자라면
        km = float(entry_km.get())  # 입력 받아 float으로 저장한다.
        entry_mile.delete(0,len(entry_mile.get()))  # entry_mile에 적혀 있는 값을 모두 지운다
        entry_mile.insert(0, round(km / 1.60934,3))  # entry_mile에 계산값을 적는다.


def mile_to_km():  # mile을 Km로 바꾸는 버튼의 command 함수
    if entry_mile.get().isnumeric():  # entry_mile의 입력 값이 숫자라면
        mile = float(entry_mile.get())  # 입력 받아 float으로 저장한다.
        entry_km.delete(0,len(entry_km.get()))  # entry_km에 적혀 있는 값을 모두 지운다.
        entry_km.insert(0, round(1.60934 * mile,3))  #  entry_km에 계산값을 적는다.


root = Tk()  # gui의 창 생성
root.title("Km <-> Mile Converter")  # 창의 타이틀 설정한다.

entry_km = Entry(root)  # km 값을 입력 받을 entry 선언
entry_km.grid(row=0,column=0,columnspan=2)  # entry_km의 위치를 격자 형식으로 정한다. 두 칸의 크기로 지정한다.

kmLabel = Label(root,text="Km")  # Km라는 글자를 보여주는 Label 선언
kmLabel.grid(row=0, column=2)  # kmLabel의 위치를 격자 형식으로 정한다.

entry_mile = Entry(root)  # mile 값을 입력 받을 entry 선언
entry_mile.grid(row=0,column=3,columnspan=2)  # entry_mile의 위치를 격자 형식으로 정한다. 두 칸의 크기로 지정한다.

mileLabel = Label(root,text="Mile")  # Mile이라는 글자를 보여주는 Label 선언
mileLabel.grid(row=0,column=5)  # mileLabel의 위치를 격자 형식으로 정한다.

ktombutton = Button(root,text="Km -> Mile",command=km_to_mile)  # Km -> Mile 버튼을 생성해주어, km_to_mile함수에 연결해준다.
ktombutton.grid(row=1,column=1)  # ktombutton의 위치를 격자 형식으로 정한다.

mtokbutton = Button(root,text="Mile -> Km",command=mile_to_km)  # Mile -> Km 버튼을 생성해주어, mile_to_km함수에 연결해준다.
mtokbutton.grid(row=1,column=4)  # mtokbutton의 위치를 격자 형식으로 정한다.

root.mainloop()  # 생성된 창을 띄워 유지한다.