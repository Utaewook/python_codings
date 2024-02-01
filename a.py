# # def solution(num):
# #     answer = 0
# #     if num == 1:
# #         return 0
# #     while num != 1:
# #         print(num)
# #         if num % 2 == 0:
# #             num = num//2
# #         else:
# #             num = num * 3 + 1
# #         answer += 1
# #
# #     if answer > 500:
# #         return -1
# #     return answer
# #
# #
# # solution(6)
#
#
# import time
#
# num = 100000001
#
# l = [i for i in range(1,num)]
#
# print('for문을 이용한 성능 측정')
# s1 = time.time()
# s = 0
# for i in range(len(l)):
#     s += l[i]
# s1_res = time.time() - s1
# print(f"{s}를 계산하는데 걸린 시간: {s1_res}")
#
#
# print('sum문을 이용한 성능 측정')
# s2 = time.time()
# s = sum(l)
# s2_res = time.time() - s2
# print(f"{s}를 계산하는데 걸린 시간: {s2_res}")
