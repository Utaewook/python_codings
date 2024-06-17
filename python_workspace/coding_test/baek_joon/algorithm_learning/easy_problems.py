def merge(arr, temp, left_start, right_end):
    global count, K, answer
    if answer is not None:
        return

    left_end = (left_start + right_end) // 2
    right_start = left_end + 1
    left = left_start
    right = right_start
    index = left_start

    while left <= left_end and right <= right_end:
        if arr[left] <= arr[right]:
            temp[index] = arr[left]
            left += 1
        else:
            temp[index] = arr[right]
            right += 1
        index += 1
        count += 1
        if count == K:
            answer = temp[index - 1]
            return

    # Copy the remaining elements
    while left <= left_end:
        temp[index] = arr[left]
        left += 1
        index += 1
        count += 1
        if count == K:
            answer = temp[index - 1]
            return

    while right <= right_end:
        temp[index] = arr[right]
        right += 1
        index += 1
        count += 1
        if count == K:
            answer = temp[index - 1]
            return

    # Copy sorted temp back to original array
    for i in range(left_start, right_end + 1):
        arr[i] = temp[i]


def merge_sort(arr, temp, left, right):
    if left < right:
        q = (left + right) // 2
        merge_sort(arr, temp, left, q)
        merge_sort(arr, temp, q+1, right)
        merge(arr, temp, left, right)

# 초기화
count = 0
answer = None

# 메인 로직에서 merge_sort를 호출
import sys
input = sys.stdin.readline

n, K = map(int,input().split())
a = list(map(int,input().split()))

merge_sort(a, [0]*len(a), 0, len(a)-1)
print(answer if answer else -1)