# 파일명: MySortings.py
# 작성자: 유태욱
# 작성일자: 2022-12-11
# 주요기능: 퀵 정렬을 구현한 MySortings 모듈
# 최종수정일자: 2022-12-11
# 수정내용: 최초작성

def _partition(arr, left, right, pi):  # 파티션을 설정하고
    pv = arr[pi]  # 피봇값을 설정한다.
    arr[pi], arr[right] = arr[right], arr[pi]  # 오른쪽 값과 피봇값을 바꾼다.
    new_pi = i = left  # 새로운 i번째 값을 설정한다.
    while (i <= right - 1):  # i의 값이 오른쪽 인덱스-1 보다 작거나 같을때 까지만 반복하는 반복문
        if (arr[i] <= pv):  # i번째 배열값이 피봇값보다 작거나 같다면
            arr[new_pi], arr[i] = arr[i], arr[new_pi]  # 새로운 i번째(new_pi)값과 바꾼다.
            new_pi += 1  # new_pi값을 1 더한다.
        i += 1  # i값을 1 더한다.
        arr[new_pi], arr[right] = arr[right], arr[new_pi]  # 오른쪽 배열의 값과 new_pi의 위치의 배열의 값을 바꾼다.
    return new_pi  # new_pi의 값을 반환한다.


def _quickSortLoop(arr, left, right):  # 재귀적으로 퀵 정렬을 수행할 루프 함수
    if (left >= right):  # 만약 왼쪽 인덱스의 값이 오른쪽 인덱스 값 보다 크거나 같으면
        return  # 재귀를 끝낸다.(돌아가기 시작)
    pi = (left + right) // 2  # pi의 값을 중간값으로 정한다.
    new_pi = _partition(arr, left, right, pi)  # new_pi의 값을 파티션으로 나누어 설정한다.
    if (left < new_pi - 1):  #  만약 new_pi-1이 left보다 크다면
        _quickSortLoop(arr, left, new_pi - 1)  # 가장 왼쪽(처음)부터 new_pi-1까지의 배열의 루프를 수행한다.(파티션 나누며 정렬 반복)
    if (new_pi + 1 < right):  # 만약 new_pi+1이 right보다 작다면
        _quickSortLoop(arr, new_pi + 1, right)  # new_pi+1 부터 가장 오른쪽(끝)까지의 배열의 루프를 수행한다.(파티션 나누며 정렬 반복)


def quickSort(arr):  # 퀵정렬을 수행하는 함수
    size = len(arr)  # 배열의 길이를 저장한다.
    _quickSortLoop(arr, 0, size - 1)  # 퀵 정렬 루프문을 시작한다.
