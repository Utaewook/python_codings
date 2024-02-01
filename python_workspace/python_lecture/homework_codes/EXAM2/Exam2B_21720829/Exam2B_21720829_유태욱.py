# 파일명: Exam2B_21720829_유태욱.py
# 작성자: 유태욱
# 작성일자: 2022-12-11
# 주요기능: Kg과 Pound를 변환하는 변환기 구현 프로그램
# 최종수정일자: 2022-12-11
# 수정내용: 최초작성

from Class_KgPoundConverter import *  # 사용자가 구현한 클래스 import

# 메인 함수의 프로그램
if __name__ == "__main__":
    window = Tk()  # gui의 창 생성
    window.title("2022-2 컴사파 Exam2B 학번 21720829 이름 유태욱")  # 창의 타이틀 설정한다.
    app = KgPoundConverter(window)  # 구현한 클래스를 통해 프로그램을 실행한다.
    window.mainloop()