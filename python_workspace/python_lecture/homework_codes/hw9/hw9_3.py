# 파일명: hw9_2.py
# 작성자: 유태욱
# 작성일자: 2022-11-07
# 주요기능: gui 환경의 스톱 워치 프로그램
# 최종수정일자: 2022-11-07
# 수정내용: 최초작성
from tkinter import *  # gui 구성을 위한 tkinter 모듈 import

time = 0  # 출력할 시간을 저장한 변수
signal = None  # 현재 진행중인 버튼의 기능을 저장할 변수


def time_go():  # 시간이 가도록 하는 변수 start와 pause로 쓰인다
    global time  # 전역변수인 time을 사용
    label['text'] = f"{time // 1000}.{time%1000}"  # label에 초를 출력한다.
    time += 1 # 1 밀리초 더한다.
    if signal == "start":  # 현재 진행해야할 버튼의 기능이 start라면
        root.after(1, time_go)  # 1밀리초 이후에 해당함수를 재귀 호출한다.
    elif signal == "pause":  # 현재 진행해야할 버튼의 기능이 pause라면
        return  # 재귀 호출 하지 않고 끝낸다


def start_btn():  # start 버튼이 눌렸을 때 수행될 함수
    global signal  # 전역변수인 signal을 사용
    if signal == 'start':  # 만약 이미 start가 진행중인데 start 시그널이 한번 더들어왔다면
        return # 함수를 끝낸다 (끝내지 않으면 시간이 빠르게 간다 - start 버튼을 n회 누른다면 시간이 n배로 빨리간다 n회만큼의 time_go 함수가 돌아가기 때문)
    signal = 'start'  # 진행해야할 버튼의 기능이 start라면
    time_go()  # 시간이 가도록하는 함수를 실행 시킨다.


def pause_btn():  # pause 버튼이 눌렸을 때 수행될 함수
    global signal  # 전역변수인 signal을 사용
    signal = 'pause'  # 진행해야할 버튼의 기능을 pause로 설정한다 -> 이미 이전에 실행된 time_go 함수에서 signal의 변경을 인지하고 일시정지 하게 된다.


def reset_btn():  # reset 버튼이 눌렸을 때 수행될 함수
    global signal, time  # 전역 변수인 signal과 time을 사용
    signal = 'reset'  # 진행해야할 signal을 reset으로 정하고
    time = 0  # 시간을 초기화 하고
    label['text'] = "0.0"  # 초기화 한 화면을 출력한다.


root = Tk()  # gui의 창 생성
root.title("My Simple Stop Watch")  # 창의 타이틀 설정한다.

label = Label(root,text='0.0',height=6)  # 초가 출력될 label을 생성한다.
label.configure(font=('Arial,',35))  # 글자의 크기와 폰트를 설정한다.
label.grid(row=0,column=0,columnspan=3)  # label의 위치를 격자 형식으로 정한다.

start = Button(root, text='Start', width=10,bg='green',command=start_btn) # 시작 버튼을 생성한다.(start_btn 함수와 연결)
start.grid(row=1,column=0)  # 시작 버튼의 위치를 격자 형식으로 정한다.

pause = Button(root, text="Pause", width=10,bg='red',command=pause_btn) # 일시정지 버튼을 생성한다.(pause_btn 함수와 연결)
pause.grid(row=1,column=1)  # 일시정지 버튼의 위치를 격자 형식으로 정한다.

reset = Button(root,text="Reset", width=10,bg='yellow',command=reset_btn) # 초기화 버튼을 생성한다.(reset_btn 함수와 연결)
reset.grid(row=1,column=2)  # 초기화 버튼의 위치를 격자 형식으로 정한다.

root.mainloop()  # 생성된 창을 띄워 유지한다.