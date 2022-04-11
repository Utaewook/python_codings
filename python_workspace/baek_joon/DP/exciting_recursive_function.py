
# def w(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     if a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20)
#     if a < b < c:
#         return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#     return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

m = {}
def w_dp(a, b, c):
    temp = 0
    if (a, b, c) not in m.keys():
        if a <= 0 or b <= 0 or c <= 0:
            temp = 1
        elif a > 20 or b > 20 or c > 20:
            temp = w_dp(20, 20, 20)
        elif a < b < c:
            temp = w_dp(a, b, c - 1) + w_dp(a, b - 1, c - 1) - w_dp(a, b - 1, c)
        else:
            temp = w_dp(a-1, b, c) + w_dp(a-1, b-1, c) + w_dp(a-1, b, c-1) - w_dp(a-1, b-1, c-1)
        m[(a, b, c)] = temp
    return m[(a, b, c)]

a, b, c = 0, 0, 0
inputs = []

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1: break
    inputs.append((a, b, c))

for i in inputs:
    print(f"w({i[0]}, {i[1]}, {i[2]}) = {w_dp(i[0],i[1],i[2])}")
