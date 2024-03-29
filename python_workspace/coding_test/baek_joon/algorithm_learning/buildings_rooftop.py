# n = int(input())
# buildings = list()
#
# for _ in range(n):
#     buildings.append(int(input()))
#
# buildings.reverse()
# count = 0
#
# while buildings:
#     curr_building = buildings.pop()
#
#     for i in range(len(buildings)-1, -1, -1):
#         if buildings[i] >= curr_building:
#             break
#         else:
#             count += 1
#
# print(count)


# 입력값
buildings = []
for i in range(int(input())): buildings.append(int(input()))

# 스택, 결과변수
stack = []
result = 0

for b in buildings:
  while stack and stack[-1]<=b:
    stack.pop()
  stack.append(b)

  result += len(stack)-1

print(result)