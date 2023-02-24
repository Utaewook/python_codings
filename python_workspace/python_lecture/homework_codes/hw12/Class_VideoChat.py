# 파일명: Class_VideoChat.py
# 작성자: 유태욱
# 작성일자: 2022-11-30
# 주요기능: 파이썬 멀티스레드, 소켓통신, OpenCV 기반 전이중 영상 채팅 구현 모듈
# 최종수정일자: 2022-11-30
# 수정내용: 최초작성

import socket, cv2, time  # 소켓 통신, OpenCV, 시간 사용을 위한 모듈 import
import numpy as np  # 이미지 데이터(영상의 부분)의 배열을 다루기 위한 numpy 모듈 import
import threading  # 멀티 스레딩 사용을 위한 모듈 import
from queue import Queue  # 스레딩에 사용될 queue 모듈 import

PORT = 9999  # 포트 번호 선언


class VideoChat:  # 영상 채팅 프로그램 클래스
    def __init__(self, role):  # 객체 생성자 함수 영상 채팅 프로그램의 기초 부분을 생성한다.
        self.myRole = role  # 역할 (서버 or 클라이언트) 매개변수로 받은 값을 초기화한다.
        print("VideoChat initiated as {} ...".format(role))  # 역할 콘솔에 출력
        hostname = socket.gethostname()  # 호스트의 이름을 가져온다
        self.myAddr = socket.gethostbyname(hostname)  # 가져온 이름으로 호스트의 주소를 가져와 멤버변수로 선언한다.
        print("My IP address = {}".format(self.myAddr))  # 내 주소 콘솔에 출력
        if self.myRole == "Server":  # 서버 역할인 경우
            self.myWebCam = 0  # SERVER_WEBCAM = 0 으로 설정한다
        else:  # 그 외의 경우(클라이언트 역할인 경우)
            self.myWebCam = 1  # CLIENT_WEBCAM = 1 으로 설정한다.
        self.op_state = "RUN"  # 상태 flag 변수에 RUN을 넣는다.

    def run(self):  # 스레드가 실행될 때 실행될 함수 부분.
        if self.myRole == "Server":  # 서버 역할인 경우
            self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 통신을 위한 소켓 멤버 변수 선언
            self.mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 소켓 통신의 옵션을 지정한다.
            self.mySocket.bind((self.myAddr, PORT))  # 소켓 통신 단계 중 하나인 bind 실행
            self.mySocket.listen()  # 소켓 통신 대기열을 생성한다.
            print('Server::Video chatting server started')  # 서버 시작을 콘솔에 출력
            print('Server::Waiting for client .... ')  # 클라이언트 기다리고 있음을 콘솔에 출력
            self.peerSocket, self.peerAddr = self.mySocket.accept()  # 통신 대기열에 클라이언트가 있다면 연결을 수락한 후, 연결 정보를 가져온다.
            print('Server::connected to client ({} : {})'.format(self.peerSocket, self.peerAddr))  # 클라이언트와 연결됨을 콘솔에 출력한다.
        elif self.myRole == "Client":  # 클라이언트 역할인 경우
            self.peerAddr = input("Input server IP address = ")  # 서버 주소를 콘솔로 입력받는다.
            print('Client::Connecting to Server')  # 서버와 연결을 시도함을 콘솔에 출력한다.
            self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 통신을 위한 소켓 멤버 변수 선언
            self.mySocket.connect((self.peerAddr, PORT))  # 서버와 통신을 연결한다.
            print('Client::Connected to Server({}:{})'.format(self.peerAddr, PORT))  # 연결이 완료되면 서버와 포트 번호를 콘솔에 출력한다.
            self.peerSocket = self.mySocket  # peerSocket에 연결된 소켓을 저장한다.
        self.queue = Queue()  # 대기열을 하나 생성한다.
        thrd_CaptureVideo = threading.Thread(target=self.captureVideo, args=(self.queue,))  # 영상을 찍는 스레드를 생성한다.
        thrd_CaptureVideo.start()  # 영상을 찍는 스레드를 실행한다.
        thrd_TxVideo = threading.Thread(target=self.txVideo, args=(self.peerSocket, self.peerAddr, self.queue,))  # 영상을 전송하는 스레드를 생성한다.
        thrd_TxVideo.start()  # 영상을 전송하는 스레드를 실행한다.
        thrd_RxVideo = threading.Thread(target=self.rxVideo, args=(self.peerSocket,))  # 영상을 수신하는 스레드를 생성한다.
        thrd_RxVideo.start()  # 영상을 수신한느 스레드를 실행한다.
        thrd_TxVideo.join()  # 스레드를 종료 대기 상태로 둔다. (자식 스레드의 종료를 기다림)
        thrd_RxVideo.join()  # 스레드를 종료 대기 상태로 둔다. (자식 스레드의 종료를 기다림)
        thrd_CaptureVideo.join()  # 스레드를 종료 대기 상태로 둔다. (자식 스레드의 종료를 기다림)
        print("VideoChatt( {}) is closing socket and quit video chatt".format(self.myRole))  # 스레드가 모두 종료되면 끝남을 콘솔에 출력
        self.mySocket.close()  # 소켓 통신 종료

    def recvall(self, sock, count):  # 소켓을 통해 버퍼로 데이터를 받아오는 함수
        if count == 0 or count == None:  # 카운트가 존재하지 않으면
            return None  # None 반환
        buf = b''  # 바이트 단위의 누적 버퍼 생성
        while count:  # 카운트가 존재할 때까지 반복하는 반복문
            try:
                newbuf = sock.recv(count)  # 소켓을 통해 count의 데이터를 버퍼로 받아오기 시도
            except:  # 예외가 생긴 경우
                self.op_state = "QUIT"  # 상태 flag 변수에 "QUIT"을 넣는다.
                break  # 반복문 종료
            if not newbuf:  # 데이터를 받아온 버퍼가 비어있다면
                return None  # None 반환
            buf += newbuf  # 누적 버퍼에 더해준다.
            count -= len(newbuf)  # 소켓을 통해 받아온 버퍼의 길이만큼 카운트를 줄여준다.
        return buf  # 누적된 버퍼를 반환해준다.

    def txVideo(self, peerSocket, addr, queue):  # 영상을 전송하는 기능을 구현한 메소드
        while True:  # 무한 루프 반복문
            if self.op_state == "QUIT":  # 만약 상태 flag 변수가 "QUIT"이라면
                break  # 반복문을 나간다.
            if queue.empty():  # 만약 대기열이 비어있다면
                # print("{}::queue is empty, self.op_state = {}".format(self.myRole, self.op_state))
                time.sleep(0.1)  # 0.1초 대기한다.
            try:
                stringData = queue.get()  # 대기열에서 데이터 가져온 후
                peerSocket.send(str(len(stringData)).ljust(16).encode())  # 가져온 데이터의 왼쪽에 16개의 길이만큼 공백을 채운 후 인코딩한 후 피어 소켓으로 전송한다.
                peerSocket.send(stringData)  # 가져온 raw 데이터도 전송해준다.
            except:  # ConnectionResetError, ConnectionAbortedError의 예외가 발생한 경우
                self.op_state = "QUIT"  # 상태 flag 변수를 "QUIT"로 둔다.
                break  # 반복문을 종료한다.
            time.sleep(0.1)  # 0.1초 대기한다.
        print("{}:: closing peerSocket() ...".format(self.myRole))  # 소켓을 닫음을 콘솔에 출력한다.
        peerSocket.close()  # 피어 소켓을 종료한다.
        print("{}:: terminating thread_txVideo() ...".format(self.myRole))  # 영상 전송 스레드를 종료함을 콘솔에 출력한다.

    def captureVideo(self, queue):  # 영상을 촬영하는 기능을 구현한 메소드
        server_webcam = cv2.VideoCapture(self.myWebCam)  # 웹캠을 cv2 모듈을 통해 가져온다.
        server_webcam.set(cv2.CAP_PROP_FPS, 8)  # FPS를 30에서 8로 낮춘다.
        fr_width, fr_height, fps = server_webcam.get(3), server_webcam.get(4), server_webcam.get(cv2.CAP_PROP_FPS)  # 영상의 정보(프레임 가로세로,fps)를 가져온다.
        print("{}_webcam frame width ({}), height({}), fps({})".format(self.myRole, fr_width, fr_height, fps))  # 영상의 정보를 콘솔에 출력한다.
        while True:  # 무한 루프 반복문
            if self.op_state == "QUIT":  # 상태 flag 변수가 "QUIT"인 경우
                break  # 반복문을 종료한다.
            ret, serv_frame = server_webcam.read()  # 가져온 웹캠 모듈을 통해 영상 데이터(결과, 이미지)를 가져온다.
            if ret == False:  # 가져온 데이터의 return값이 없다면
                continue  # 반복문 다시 시작
            resized_svrfr = cv2.resize(serv_frame, (int(serv_frame.shape[1] / 2), int(serv_frame.shape[0] / 2)))  # 서버의 프레임을 재지정한다.
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]  # 데이터 인코딩 파라미터를 생성한다.
            result, imgencode = cv2.imencode('.jpg', resized_svrfr, encode_param)  # 이미지를 인코딩한다.
            img_data = np.array(imgencode)  # 이미지 데이터를 배열로 저장한다.
            stringData = img_data.tobytes()  # 배열로 저장된 이미지 데이터를 바이트 시퀸스로 바꾼다.
            queue.put(stringData)  # 대기열에 바이트 데이터를 저장한다.
            # cv2.imshow('Server:: Resized_Server_Video', resized_svrfr)
            key = cv2.waitKey(1)  # cv 모듈을 1ms 대기시켜 키 입력 이벤트를 받는다.
            if key == 27:  # ESC 키가 눌렸다면
                print("{} :: ESC key pressed => exit".format(self.myRole))  # ESC키가 눌림을 콘솔에 출력한 후
                self.op_state = "QUIT"  # 상태 flag 변수를 "QUIT"로 설정한다.
                break  # 반복문을 종료한다.
            time.sleep(0.05)  # 0.05초 대기 한 후
        print("{}:: terminating thread_captureVideo() ...".format(self.myRole))  # 영상 촬영 스레드를 종료함을 콘솔에 출력한다.

    def rxVideo(self, peerSocket):  # 영상을 받는 기능을 구현한 메소드
        while True:  # 무한 루프 반복문
            if self.op_state == "QUIT":  # 상태 flag 변수가 "QUIT"인 경우
                break  # 반복문을 종료한다.
            length = self.recvall(peerSocket, 16)  # 데이터 버퍼를 가져오는 함수를 통해 데이터를 가져온다(처음엔 공백이 가져와진다.)
            if length == 0 or length == None or length == b'':  # 데이터 버퍼가 비어있는 경우
                self.op_state = "QUIT"  # 상태 flag 변수를 "QUIT"로 설정한다.
                break  # 반복문을 종료한다.
            stringData = self.recvall(peerSocket, int(length))  # 데이터 버퍼를 다시 가져온다
            data = np.frombuffer(stringData, dtype='uint8')  # 받아온 데이터를 8비트 부호없는 정수형 배열로 생성한다.
            decimg = cv2.imdecode(data, 1)   # 생성한 정수형 데이터 배열을 이미지로 인코딩한다.
            cv2.imshow('{} :: received video from peer'.format(self.myRole), decimg)  # cv2 모듈을 통해 인코딩 한 이미지를 출력한다.
            key = cv2.waitKey(1)  # cv 모듈을 1ms 대기시켜 키 입력 이벤트를 받는다.
            if key == 27:  # ESC 키가 눌렸다면
                print("{} :: ESC key pressed => exit".format(self.myRole))  # ESC키가 눌림을 콘솔에 출력한 후
                self.op_state = "QUIT"  # 상태 flag 변수를 "QUIT"로 설정한다.
                break  # 반복문을 종료한다.
            time.sleep(0.05)  # 0.05초 대기 한 후
        print("{}:: terminating thread_rxVideo() ...".format(self.myRole))  # 영상 수신 스레드를 종료함을 콘솔에 출력한다.
