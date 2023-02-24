# 파일명: video_client.py
# 작성자: 유태욱
# 작성일자: 2022-11-30
# 주요기능: 멀티스레드, 소켓통신, OpenCV를 통한 양방향 전이중 영상 채팅 프로그램 (클라이언트 부분)
# 최종수정일자: 2022-11-30
# 수정내용: 최초작성

from Class_VideoChat import *  # 영상 채팅 프로그램을 사용하기 위한 모듈 import

if __name__ == "__main__":  # 메인 메소드인 경우
    videoChatt_client = VideoChat("Client")  # 영상 채팅 프로그램을 클라이언트 역할로 생성한다.
    videoChatt_client.run()  # 생성된 영상 채팅 프로그램의 UI를 실행한다.