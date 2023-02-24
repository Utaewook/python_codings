
# 파일명: hw6_2.py
# 작성자: 유태욱
# 작성일자: 2022-10-04
# 주요기능: 사용자 정의 모듈을 이용한 병합정렬
# 최종수정일자: 2022-10-04
# 수정내용: 최초작성

# Comparison of mergeSort and selectionSort with user‐defined modules

import random, time, sys
myPyModules_dir = "C:/MyPyPackage/myPyModules"
sys.path.append(myPyModules_dir)

import MyList, MySortings

while True:
    size = int(input("\nsize of list (0 to terminate) = "))
    if size == 0:
        break
    L = []
    MyList.genRandList(L, size)
    print("List (size : {}) before merge sorting : ".format(size))
    MyList.printListSample(L, 10, 2)
    t1 = time.time()
    L = MySortings.mergeSort(L)
    t2 = time.time()
    print("\nList (size : {}) after merge sorting : ".format(size))
    MyList.printListSample(L, 10, 2)
    print("\nMerge sorting for list of {} integers took {} sec".format(size, t2-t1))
    MyList.shuffleList(L)
    print("\nList (size : {}) before selection sorting : ".format(size))
    MyList.printListSample(L, 10, 2)
    t1 = time.time()
    MySortings.selectionSort(L)
    t2 = time.time()
    print("\nList (size : {}) after selection sorting : ".format(size))
    MyList.printListSample(L, 10, 2)
    print("Selection sorting for list of {} integers took {} sec".format(size, t2-t1))