# 파일명: Class_TextChat.py
# 작성자: 유태욱
# 작성일자: 2022-11-30
# 주요기능: 파이썬 스레드 기반 채팅 프로그램 구현 모듈
# 최종수정일자: 2022-11-30
# 수정내용: 최초작성

import socket  # socket 통신을 위한 socket 모듈 import
from threading import Thread  # 멀티 스레드 기반으로 구현하기 위한 Thread 모듈 import
import tkinter as tk  # 프로그램 UI를 제작하기 위한 tkinter 모듈 import
from tkinter import ttk, scrolledtext, END  # 프로그램 UI에 사용되는 클래스 import

LocalHost = "127.0.0.1"  # 루프백 ip 주소 (자기 자신)
SocketChat_PortNumber = 24000  # 포트 번호를 선언한다.


class TextChat:  # 채팅 프로그램 클래스
    def __init__(self, role):  # 객체 생성자 함수 채팅 프로그램의 기초 부분을 생성한다.
        global hostAddr  # 호스트 ip주소를 저장할 변수를 전역변수로 선언한다.
        self.win = tk.Tk()  # UI 창을 멤버변수로 생성한다.
        self.myRole = role  # 역할(서버 or 클라이언트) 매개변수로 받은 값을 초기화한다.

        self.win.title("Python Socket-based TextChatt ({})".format(self.myRole))  # UI 창의 제목을 설정한다.
        hostname = socket.gethostname()  # 호스트의 이름을 가져온다.
        hostAddr = socket.gethostbyname(hostname)  # 가져온 이름으로 호스트의 주소를 가져온다.
        print("My ({}) IP address = {}".format(self.myRole, hostAddr))  # 가져온 변수 확인 출력
        self.myAddr = hostAddr  # 내 주소 멤버변수에 호스트 주소 선언
        self.createWidgets()  # UI 창 생성하는 메소드로 프로그램 UI 생성
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 통신을 위한 소켓 멤버 변수 선언

        if self.myRole == "Server":  # 서버 역할인 경우
            self.mySocket.bind((hostAddr, SocketChat_PortNumber))  # 소켓 통신 단계 중 하나인 bind 실행 (IP_addr(local_host), port_number)
            self.scrDisplay.insert(tk.INSERT, "TCP server is waiting for a client .... \n")  # UI의 채팅 디스플레이에 문자열 삽입(대기중 표현)
            self.mySocket.listen(1)  # 소켓 통신 대기열을 하나 생성한다.
            self.conn, self.cliAddr = self.mySocket.accept()  # 소켓 통신 완료되면 통신의 정보를 가져와서 멤버변수로 둔다. cliAddr : (IPaddr, port_no)
            print("TCP Server is connected to client ({})\n".format(self.cliAddr))  # 클라이언트와 연결된 통신 결과를 콘솔에 출력한다.
            self.scrDisplay.insert(tk.INSERT, "TCP server is connected to client\n")  # UI의 채팅 디스플레이에 문자열 삽입(통신 연결 완료)
            self.scrDisplay.insert(tk.INSERT, "TCP client IP address : {}\n".format(self.cliAddr[0]))  # UI의 채팅 디스플레이에 문자열 삽입(통신 연결 정보)
            self.cliAddr_entry.insert(END, self.cliAddr[0])  # 클라이언트 ip 주소 표시 UI에 클라이언트 주소 출력
        elif self.myRole == "Client":  # 클라이언트 역할인 경우
            self.cliAddr = self.myAddr  # 클라이언트 ip 주소에 자기 자신의 주소를 넣는다.
            self.cliAddr_entry.insert(END, self.myAddr)  # 클라이언트 ip 주소 표시 UI에 클라이언트 주소(내 주소) 출력
            servAddr_str = input("Server IP Addr (e.g., '127.0.0.1') = ")  # 서버 주소를 입력받는다.
            self.mySocket.connect((servAddr_str, SocketChat_PortNumber))  # TCP 서버로 연결 요청을 보낸다.
            self.servAddr = self.mySocket.getpeername()  # 생성된 소켓 멤버 변수를 통해 서버 주소를 가져온다.
            print("TCP Client is connected to server ({})\n".format(self.servAddr))  # 클라이언트의 서버 연결 결과 출력
            self.scrDisplay.insert(tk.INSERT, "TCP client is connected to server \n")  # UI의 채팅 디스플레이에 문자열 삽입(클라이언트가 서버에 연결 완료)
            self.scrDisplay.insert(tk.INSERT, "TCP server IP address : {}\n".format(self.servAddr[0]))  # UI의 채팅 디스플레이에 문자열 삽입(통신 연결 정보)
            self.servAddr_entry.insert(END, self.servAddr[0])  # 서버 주소 표시 UI에 서버 주소 출력
            self.conn = self.mySocket  # 연결 정보를 socket으로 저장.

        thread_sockRecvMsg = Thread(target=self.sockRecvMsg, daemon=True)  # 메시지를 받아오는 메소드를 스레딩으로 생성한다.
        thread_sockRecvMsg.start()  # 스레드를 실행한다.

    def sockRecvMsg(self):  # 메시지를 받는 메소드
        while True:  # 무한루프
            recvMsg = self.conn.recv(512).decode()  # 수신한 메시지를 바이트로 디코딩해서 저장한다.
            if not recvMsg:  # 메시지가 비어있다면
                break  # 무한루프를 끝낸다.
            self.scrDisplay.insert(tk.INSERT, ">> " + recvMsg)  # 수신 메시지를 UI의 채팅 디스플레이에 삽입한다.
        self.conn.close()  # 연결을 종료한다.

    def _quit(self):  # 프로그램 종료를 위한 메소드
        self.win.quit()  # UI를 종료하고
        self.win.destroy()  # UI 창을 닫는다
        exit()  # 파이썬 프로그램을 종료한다.

    def sockSendMsg(self):  # 메시지를 보내는 메소드
        msgToPeer = str(self.scrTextInput.get(1.0, END))  # peer에게 보낼 메시지를 UI를 통해 입력 받는다.
        self.scrDisplay.insert(tk.INSERT, "<< " + msgToPeer)  # UI의 채팅 디스플레이에 대가 보낸 메시지를 표시한다.
        self.conn.send(bytes(msgToPeer.encode()))  # 생성된 연결을 통해 메시지를 byte로 인코딩해 보낸다.
        self.scrTextInput.delete('1.0', END)  # 메시지 입력 부분을 지워준다

    def createWidgets(self):  # 프로그램의 UI를 생성하는 메소드
        frame = ttk.LabelFrame(self.win, text="Frame(Socket-based Text Chatting)")  # frame을 생성한다.
        frame.grid(column=0, row=0, padx=8, pady=4)  # grid 레이아웃 사용한다.

        frame_addr_connect = ttk.LabelFrame(frame, text="")  # frame에 연결 주소들을 표시할 LabelFrame을 만든다.
        frame_addr_connect.grid(column=0, row=0, padx=40, pady=20, columnspan=2)  # grid 레이아웃 사용한다.

        servAddr_label = ttk.Label(frame_addr_connect, text="Server Addr")  # 생성된 LabelFrame에 서버 주소 글자 Label을 생성한다.
        servAddr_label.grid(column=0, row=0, sticky='W')  # 라벨도 grid 레이아웃 사용 하고, west 방향 정렬한다.
        cliAddr_label = ttk.Label(frame_addr_connect, text="Client Addr")  # 생성된 LabelFrame에 클라이언트 주소 글자 Label을 생성한다.
        cliAddr_label.grid(column=1, row=0, sticky='W')  # 라벨도 grid 레이아웃 사용 하고, west 방향 정렬한다.

        self.servAddr = tk.StringVar()  # tkinter String 값 변수 선언
        self.servAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable=self.myAddr)  # 서버 주소 표시 Entry 생성
        self.servAddr_entry.insert(END, hostAddr)  # 서버 주소를 표시해준다.
        self.servAddr_entry.grid(column=0, row=1, sticky='W')  # 서버 주소 표시 Entry grid 레이아웃으로 배치
        self.cliAddr = tk.StringVar()  # tkinter String 값 변수 선언
        self.cliAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable="")  # 클라이언트 주소를 표시해준다.
        self.cliAddr_entry.grid(column=1, row=1, sticky='W')  # 클라이언트 주소 표시 Entry grid 레이아웃으로 배치

        scrol_w, scrol_h = 40, 20  # 스크롤 너비와 높이 변수 초기화
        msgDisplay_label = ttk.Label(frame, text="Mesage Display ({})".format(self.myRole))  # 메시지 표시 라벨을 생성한다.
        msgDisplay_label.grid(column=0, row=1)  # 라벨 grid 레이아웃으로 배치
        self.scrDisplay = scrolledtext.ScrolledText(frame, width=scrol_w, height=scrol_h, wrap=tk.WORD)  # UI 채팅 디스플레이를 생성한다.(ScrollText)
        self.scrDisplay.grid(column=0, row=2, sticky='E')  # 채팅 디스플레이 grid 레이아웃으로 배치
        msgInput_label = ttk.Label(frame, text="Input Text Message ({}) :".format(self.myRole))  # 메시지 입력 표시 라벨을 생성한다.
        msgInput_label.grid(column=0, row=3)  # 라벨 grid 레이아웃으로 배치
        self.scrTextInput = scrolledtext.ScrolledText(frame, width=40, height=3, wrap=tk.WORD)  # 메시지 입력 받을 창을 생성한다.(ScrollText)
        self.scrTextInput.grid(column=0, row=4)  # 메시지 입력 창 grid 레이아웃으로 배치

        txButton = ttk.Button(frame, text="Send Message to Peer", command=self.sockSendMsg)  # 전송 버튼을 생성하고, 메시지가 발신되는 메소드를 연결한다.
        txButton.grid(column=0, row=5, sticky='E')  # 버튼 grid 레이아웃으로 배치한다. east 방향 정렬한다.

        self.scrTextInput.focus()  # 메시지 입력 창에 focus를 설정한다.