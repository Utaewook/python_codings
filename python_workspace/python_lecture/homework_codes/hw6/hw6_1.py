
# 파일명: hw6_1.py
# 작성자: 유태욱
# 작성일자: 2022-10-04
# 주요기능: 사용자 정의 모듈을 이용한 선택정렬
# 최종수정일자: 2022-10-04
# 수정내용: 최초작성

# User‐defined package/module
import sys
myPyModules_dir = "C:/MyPyPackage/myPyModules"
sys.path.append(myPyModules_dir)
import MyList, MySortings

L = []
n = 100
MyList.genRandList(L, n)
print("Before Sorting :")
MyList.printListSample(L, 10, 3)
MySortings.selectionSort(L)
print("\nAfter Sorting :")
MyList.printListSample(L, 10, 3)