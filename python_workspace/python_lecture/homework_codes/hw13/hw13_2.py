# 파일명: hw13_2.py
# 작성자: 유태욱
# 작성일자: 2022-12-04
# 주요기능: CNN 구조의 머신러닝 모델을 통한 필기체 숫자 인식 프로그램
# 최종수정일자: 2022-12-04
# 수정내용: 최초작성

import cv2  # 이미지를 다루기 위한 cv2 모듈 import
import numpy as np  # 데이터 셋 처리를 위한 numpy 모듈 import
from tkinter import *  # 프로그램 GUI를 생성하기 위한 tkinter 모듈의 메소드와 변수 import
from PIL import ImageGrab  # 이미지를 추출하기위한 ImageGrab import
from keras.models import load_model  # 모델을 로드하기 위한 load_model 메소드 import

model = load_model("CNN_model_Digits")  # 미리 생성해둔 CNN 모델을 로드 한다.
model.summary()  # model의 요악을 출력한다.
print("Model is loaded successfully ...")  # 모델이 성공적으로 load되었음을 콘솔에 출력한다.

# create a main window first (named as root)
root = Tk()  # 메인 화면을 생성한다.
root.resizable(0, 0)  # 메인 화면을 크기 조절이 불가능 하도록 설정한다.
root.title("Handwritten Digits Recognition GUI App")  # 메인 화면의 타이틀을 설정한다.

# Initialize variables
lastx, lasty = None, None  # x,y 좌표 초기화
image_number = 0  # 이미지의 번호 초기화

# Create a canvas for drawing digits
cv = Canvas(root, width=640, height=480, bg='white')  # 필기체 숫자를 적기 위한 캔버스 생성
cv.grid(row=0, column=0, pady=2, sticky=W, columnspan=2)  # 캔버스 객체의 위치 설정(격자 형식)


# GUI for handwritten digits recognition (2)
def draw_lines(event):  # 캔버스에 선을 그리는 함수
    global lastx, lasty  # 전역 변수 x,y 좌표를 사용한다.
    x, y = event.x, event.y  # 이벤트로 가져온 좌표를 저장한다.
    cv.create_line((lastx, lasty, x, y), width=8, fill='black', capstyle=ROUND, smooth=TRUE, splinesteps=12)  # 전역 변수 x,y(지난 좌표)와 현재 x,y 좌표를 선으로 잇는다
    lastx, lasty = x, y  # 지난 좌표(전역 변수 x,y)에 현재 x,y 좌표를 저장한다.


def clear_widget():  # 캔버스를 지우는 함수
    global cv  # 전역 변수 cv 객체를 사용한다.
    cv.delete("all")  # cv의 모든 요소를 지운다.


def activate_event(event):  # 캔버스에 이벤트를 처리하는 함수
    global lastx, lasty  # 전역변수 x,y 좌표를 사용한다(이전 위치 좌표)
    cv.bind('<B1-Motion>', draw_lines)  # 마우스가 왼쪽 버튼을 누르면서 움직일때, 캔버스에 선을 그리는 함수를 실행한다.
    lastx, lasty = event.x, event.y  # 지난 좌표(전역 변수 x,y)에 현재 x,y 좌표를 저장한다.


def recognize_digit():  # 필기체 숫자를 인식하는 함수
    global image_number  # 전역 변수 이미지 번호를 사용한다.
    filename = f'image_{image_number}.png'  # 이미지 번호를 갖는 파일 이름을 생성한다.
    widget = cv  # 위젯을 캔버스에서 받아온다.
    # get the widget coordinates
    x = root.winfo_rootx() + widget.winfo_x()  # 왼쪽 x 좌표를 계산한다.
    y = root.winfo_rooty() + widget.winfo_y()  # 위 y 좌표를 계산한다.
    x1 = x + widget.winfo_width()  # 오른쪽 x 좌표를 계산한다.
    y1 = y + widget.winfo_height()  # 아래 y 좌표를 계산한다.
    # grab the image, crop it
    ImageGrab.grab().crop((x, y, x1, y1)).save(filename)  # 계산한 좌표로 이미지를 인식해서 가져온 후, 파일 이름으로 저장한다.
    # read the image in color format
    image = cv2.imread(filename, cv2.IMREAD_COLOR)  # 저장된 이미지를 가져온다.
    # convert the image in grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 이미지를 흑백 이미지로 변환한다.
    # applying thresholding (Bobuyuki Otsu’s method: greyscale to monochrome)
    ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # 임계값에 해당하는 픽셀을 처리하는 함수를 통해 이미지를 정리한다.
    # findContour() function helps in extracting the contours from the image
    contours = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]  # 이미지의 경계선을 가져온다.
    for cnt in contours:  # 이미지의 경계선을 순회하는 반복문
        x, y, w, h = cv2.boundingRect(cnt)  # 경계선을 포함하는 최소 크기 사각형을 가져온다.
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)  # 이미지에 사각형을 그린다.
        top = int(0.05 * th.shape[0])  # 관심 영역의 위아래 여유값을 설정
        bottom = top  # 관심 영역의 위아래 여유값을 설정
        left = int(0.05 * th.shape[1])  # 관심 영역의 좌우 여유값을 설정
        right = left   # 관심 영역의 좌우 여유값을 설정
        roi = th[y - top:y + h + bottom, x - left:x + w + right]  # 이미지의 관심 영역을 설정한다.
        img = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)  # 관심 영역을 28*28픽셀 크기로 사이즈 조절한다.
        img = img.reshape(1, 28, 28, 1)  # 이미지의 데이터를 재배열한다. (CNN 모델의 input에 맞게)
        img = img / 255.0  # 이미지를 일반화 한다.
        pred = model.predict([img])[0]  # 이미지를 모델에 적용해 예상 결과를 저장한다.
        final_pred = np.argmax(pred)  # 예상 결과의 가장 유력한 값을 가져온다.
        data = str(final_pred) + ' ' + str(int(max(pred) * 100)) + '%'  # 가장 유력한 값과 해당 값일 확률을 문자열로 만든다.
        font = cv2.FONT_HERSHEY_SIMPLEX  # 폰트를 설정한다.
        fontScale = 0.5  # 폰트의 크기
        color = (255, 0, 0)  # 폰트의 색상
        thickness = 1  # 폰트의 굵기
        cv2.putText(image, data, (x, y - 5), font, fontScale, color, thickness)  # 이미지에 생성한 문자열을 입력한다.(폰트적용)
    cv2.imshow("image", image)  # 모델을 통해 각 필기체가 예상된 결과를 가진 이미지를 출력한다
    cv2.waitKey(0)  # 무한 대기



cv.bind('<Button-1>', activate_event)  # 캔버스 창에 이벤트를 받아 선을 그리는 함수를 연결한다.
btn_save = Button(text="Recognize Digits", command=recognize_digit)  # 필기체 인식 버튼을 생성한다.
btn_save.grid(row=2, column=0, padx=1, pady=1)  # 필기체 인식 버튼을 메인 창에 배치한다.
btn_clear = Button(text="Clear widget", command=clear_widget)  # 창 지우기 버튼을 생성한다.
btn_clear.grid(row=2, column=1, padx=1, pady=1)  # 창 지우기 버튼을 메인 창에 배치한다.
root.mainloop()  # 메인 화면 창을 유지한다.
