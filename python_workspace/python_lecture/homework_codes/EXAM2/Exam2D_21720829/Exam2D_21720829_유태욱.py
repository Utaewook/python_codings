# 파일명: Exam2D_21720829_유태욱.py
# 작성자: 유태욱
# 작성일자: 2022-12-11
# 주요기능: 실수자료형 (float) 리스트에 대한 Numpy sort()와 파이썬 기반 퀵정렬 함수 quickSort() 성능 비교 프로그램
# 최종수정일자: 2022-12-11
# 수정내용: 최초작성

import time, numpy, MyList, MySortings, random  # 필요한 모듈 import


def main():  # 메인함수
    print("2022-2 컴사파 기말고사 학번: 21720829, 이름: 유태욱")
    Test_size = [100000, 500000, 1000000, 5000000]  # 테스트 케이스 선언
    for L_size in Test_size:
        print("\nGenerating random list of size ({}) ...".format(L_size))
        L = MyList.genRandFloatList(L_size)

        # testing Numpy.sort()
        print("Before numpy.sort() of L :")
        MyList.printFloatListSample(L, 10, 2)
        t1 = time.time()
        L = numpy.sort(L)
        t2 = time.time()
        print("After numpy.sort() of L :")
        MyList.printFloatListSample(L, 10, 2)
        time_elapsed = t2 - t1
        print("numpy.sort() of list (size={}) took {} sec".format(L_size, time_elapsed))
        # testing Quick Sorting
        random.shuffle(L)
        print("\nBefore MySortings.quickSort() of L :")
        MyList.printFloatListSample(L, 10, 2)
        t1 = time.time()
        MySortings.quickSort(L)
        t2 = time.time()
        print("After MySortings.quickSort() of L :")
        MyList.printFloatListSample(L, 10, 2)
        time_elapsed = t2 - t1
        print("MySortings.quickSort() of list (size={}) took {} sec".format(L_size, time_elapsed))


# 메인 함수 실행문
if __name__ == "__main__":
    main()