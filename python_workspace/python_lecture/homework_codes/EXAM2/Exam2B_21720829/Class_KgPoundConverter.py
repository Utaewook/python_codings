# 파일명: Class_KgPoundConverter.py
# 작성자: 유태욱
# 작성일자: 2022-12-11
# 주요기능: Kg과 Pound를 변환해주는 객체 구현 모듈
# 최종수정일자: 2022-12-11
# 수정내용: 최초작성
from tkinter import *  # GUI 환경을 제작하기 위한 tkinter 모듈의 객체와 메소드 import


class KgPoundConverter():  # kg와 pound를 변환하는 기능을 구현한 클래스
    def __init__(self, master):  # 객체 생성자 (창을 구성하는 요소를 생성한다.)
        frame = LabelFrame(master, text="kg<->pound converter")  # tkinter 창을 생성한다.
        frame.pack()  # 창을 정리
        self.kg_var = DoubleVar()  # 입력받을 kg값을 선언
        self.pound_var = DoubleVar()   # 입력받을 pound값을 선언

        self.entry_kg = Entry(frame,textvariable=self.kg_var)  # kg값을 받아올 entry 선언
        self.entry_kg.grid(row=0, column=0, columnspan=2)  # entry의 위치를 설정한다.
        Label(frame, text="Kg").grid(row=0, column=2)  # "kg" 글자를 frame에 추가한다.
        self.entry_pound = Entry(frame,textvariable=self.pound_var)  # pound값을 받아올 entry 선언
        self.entry_pound.grid(row=0, column=3, columnspan=2)  # entry의 위치를 설정한다.
        Label(frame, text="Pound").grid(row=0, column=5)  # "pound" 글자를 frame에 추가한다.
        self.ktopbutton = Button(frame, text='Kg -> Pound', bg="green", command=self.kg_to_pound)  # kg을 pound로 변환하는 버튼을 생성
        self.ktopbutton.grid(row=1, column=1)  # 버튼의 위치를 설정한다.
        self.ptokbutton = Button(frame, text='Pound -> Kg', bg="yellow", command=self.pound_to_kg)  # pound를 kg로 변환하는 버튼을 생성
        self.ptokbutton.grid(row=1, column=4)  # 버튼의 위치를 설정한다.

    def kg_to_pound(self):  # kg을 pound로 바꾸는 버튼의 command 함수
        kg = float(self.kg_var.get())  # 입력 받아 float으로 저장한다.
        self.entry_pound.delete(0, len(self.entry_pound.get()))  # entry_pound에 적혀 있는 값을 모두 지운다
        self.entry_pound.insert(0, round(kg * 2.20462, 3))  # entry_pound에 계산값을 적는다.


    def pound_to_kg(self):  # pound를 Kg으로 바꾸는 버튼의 command 함수
        pound = float(self.pound_var.get())  # 입력 받아 float으로 저장한다.
        self.entry_kg.delete(0, len(self.entry_kg.get()))  # entry_kg에 적혀 있는 값을 모두 지운다.
        self.entry_kg.insert(0, round(pound / 2.20462, 3))  # entry_kg에 계산값을 적는다.
